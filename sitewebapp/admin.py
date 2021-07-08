from django.contrib import admin
from .models import Alumni, Members, access_tokens, blog, Comments, event
from nested_inline.admin import NestedStackedInline, NestedModelAdmin 
# Register your models here.

class commentInLine(admin.TabularInline):
    model = Comments
    extra = 1

class blogAdmin(admin.ModelAdmin):
    inlines = [commentInLine]
    list_display = ('title', 'author', 'created_on')
    search_fields = ['title']

#admin.site.register(Members)



admin.site.register(blog, blogAdmin)
admin.site.register(Members)
admin.site.register(event)
admin.site.register(Alumni)
admin.site.register(access_tokens)