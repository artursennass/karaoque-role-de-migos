from django.contrib import admin

from apps.music_module.models import Author

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)

admin.site.register(Author, AuthorsAdmin)
