from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article, Drinks,Editor,Article,tags

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Drinks)
admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(tags)