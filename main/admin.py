from django.contrib import admin

from .models import News





@admin.register(News)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug', 'image')

