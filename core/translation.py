from modeltranslation.translator import register, TranslationOptions
from .models import Information,Benefits




@register(Information)
class CoreInformationTranslationOptions(TranslationOptions):
    fields = ('about', 'title')


@register(Benefits)
class BenefitsTranslationOptions(TranslationOptions):
    fields = ('description','logo')