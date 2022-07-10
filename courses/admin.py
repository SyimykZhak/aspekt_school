from django import forms
from django.contrib import admin
from .models import Coursess, Teachers, Category, Group, Register
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget 
from modeltranslation.admin import TranslationAdmin 


class CoursesAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    description_ky = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = Coursess
        fields = '__all__'


class GroupInline(admin.StackedInline):
    model = Group
    extra = 1

@admin.register(Coursess)
class CoursesAdmin(TranslationAdmin):
    list_display =("title", "tagline", "draft")
    inlines = [GroupInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    form = CoursesAdminForm
    fieldsets = (
        (None,{
            "fields": ("title", "tagline","image","description")
        }),
        (None,{
            "fields": (("teacher","category"),)
        }),
        (None,{
            "fields": (("term", "modul", "time","price"),)
        }),
        ("Options",{
            "fields": ("url","draft",)
        }),
    )

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display =["name", "age", "get_image"]
    readonly_fields =("get_image",)

    def get_image(self,obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50"')

    get_image.short_description = "Изображение"

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("name", "url")
    list_display_links = ("name",)

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display =("name","email","created")
    list_filter = ("course",)
    readonly_fields = ("course",'name', 'lastname', 'email','telephone','goal','group','created',)
    fieldsets = (
        (None,{
            "fields": ("course",)
        }),
        (None,{
            "fields": ("name", "lastname",)
        }),
        (None,{
            "fields": ("email","telephone","goal","group",)
        }),
    )