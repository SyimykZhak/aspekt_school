from sys import maxsize
from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin 

from .models import Benefits, Information, Reviews, SchoolShots, License,Questions

admin.site.site_header = ("Aspekt админ")

@admin.register(Information)
class ConferenceAdmin(TranslationAdmin):
    list_display = ("title",)
    # inlines = [BenefitsInline]
    search_fields = ("title",)
    save_on_top = True
    save_as = True
    actions = ["publish", "unpublish"]
    fieldsets = (
        (None, {
            "fields": (("title", "backround"),)
        }),
        (None, {
            "fields": (("about", "image_for_about"),)
        }),
        (None, {
            "fields": (("address","street","email","telephone","whatsapp","instagram","facebook","twitter","map"),)
        }),
    )

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change', )

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)


@admin.register(Benefits)
class BenefitssAdmin(TranslationAdmin):
    list_display =("description","logo","get_logo",)
    list_filter = ("main",)
    readonly_fields = ("get_logo",)

    def get_logo(self, obj):
        return mark_safe(f'<img src={obj.logo.url} width="60" height="40"')

    get_logo.short_description = "логотип"


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "school", "id")
    readonly_fields = ("get_logo",)

    def get_logo(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="60" height="40"')

    get_logo.short_description = "фото"

@admin.register(SchoolShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "school", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(License)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "school", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.logo.url} width="50" height="60"')

    get_image.short_description = "Изображение"

@admin.register(Questions)
class RegisterAdmin(admin.ModelAdmin):
    list_display =("name","created",)
    readonly_fields = ("name", "telephone", "created","question")
    list_filter = ("created",)
    fieldsets = (
        (None,{
            "fields": ("name","telephone",)
        }),
        (None,{
            "fields": ("question",)
        }),
    )