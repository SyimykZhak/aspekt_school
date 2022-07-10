from modeltranslation.translator import register, TranslationOptions
from .models import Category, News


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name','description')


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'tagline','desccription')

