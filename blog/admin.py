from django.contrib import admin
from azhsite.blog.models import Category, Entry

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

admin.site.register(Category, CategoryAdmin)

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['head']}

admin.site.register(Entry, EntryAdmin)
