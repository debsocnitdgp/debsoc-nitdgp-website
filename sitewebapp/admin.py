from django.contrib import admin
from .models import Members, blog, Comments, event
# Register your models here.


class commentInLine(admin.TabularInline):
    model = Comments
    extra = 1


class blogAdmin(admin.ModelAdmin):
    inlines = [commentInLine]
    list_display = ('title', 'author', 'created_on')
    search_fields = ['title']


admin.site.register(blog, blogAdmin)
admin.site.register(Members)
admin.site.register(event)
