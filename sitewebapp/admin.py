from django.contrib import admin
from .models import Members, blog, Comments, event, Candidates, auditionRounds, auditionQuestions, auditionAnswers
from nested_inline.admin import NestedStackedInline, NestedModelAdmin 
# Register your models here.

class commentInLine(admin.TabularInline):
    model = Comments
    extra = 1

class blogAdmin(admin.ModelAdmin):
    inlines = [commentInLine]
    list_display = ('title', 'author', 'created_on')
    search_fields = ['title']

class answerInLine(admin.TabularInline):
    model = auditionAnswers
    extra = 1

class questionInLine(admin.TabularInline):
    model = auditionQuestions
    extra = 1
    inlines = [answerInLine]

class roundInLine(admin.TabularInline):
    model = auditionRounds.candidate.through
    extra = 1
    inlines = [questionInLine]

class auditionQuestionsAdmin(admin.ModelAdmin):
    inlines = [answerInLine]

class auditionRoundsAdmin(admin.ModelAdmin):
    inlines = [questionInLine]

class CandidatesAdmin(admin.ModelAdmin):
    inlines = [roundInLine]




admin.site.register(blog, blogAdmin)
admin.site.register(Members)
admin.site.register(event)
admin.site.register(Candidates, CandidatesAdmin)
admin.site.register(auditionRounds, auditionRoundsAdmin)
admin.site.register(auditionQuestions, auditionQuestionsAdmin)
admin.site.register(auditionAnswers)