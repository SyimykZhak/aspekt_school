from modeltranslation.translator import register, TranslationOptions
from .models import Category, Coursess


@register(Category)
class CoursesCategoryTranslationOptions(TranslationOptions):
    fields = ('name','description')


@register(Coursess)
class CoursesTranslationOptions(TranslationOptions):
    fields = ('title', 'tagline','description')