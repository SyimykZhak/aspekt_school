from django import forms
from django.contrib import admin
from .models import News,Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin 

class NewsAdminForm(forms.ModelForm):
    desccription_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    desccription_ky = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display =("title", "category", "add_time","draft")
    save_on_top = True
    save_as = True
    form = NewsAdminForm
    list_editable = ("draft",)
    fieldsets = (
        (None,{
            "fields": ("category","title", "tagline","image",)
        }),
        (None,{
            "fields": ("desccription",)
        }),
        ("Options",{
            "fields": ("url","draft",)
        }),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    list_display_links = ("name",)
