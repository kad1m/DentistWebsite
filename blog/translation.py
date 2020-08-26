from modeltranslation.translator import register, TranslationOptions
from .models import Post, TaggableManager

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('meta', 'title', 'description', 'body')
