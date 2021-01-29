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

class answerInLine(NestedStackedInline):
    model = auditionAnswers
    extra = 1

class questionInLine(NestedStackedInline):
    model = auditionQuestions
    extra = 1
    inlines = [answerInLine]

class roundInLine(NestedStackedInline):
    model = auditionRounds
    extra = 1
    inlines = [questionInLine]




class auditionQuestionsAdmin(NestedModelAdmin):
    inlines = [answerInLine]


class auditionRoundsAdmin(NestedModelAdmin):
    inlines = [questionInLine]

class CandidatesAdmin(NestedModelAdmin):
    inlines = [roundInLine]




admin.site.register(blog, blogAdmin)
admin.site.register(Members)
admin.site.register(event)
admin.site.register(Candidates, CandidatesAdmin)
admin.site.register(auditionRounds, auditionRoundsAdmin)
admin.site.register(auditionQuestions, auditionQuestionsAdmin)
admin.site.register(auditionAnswers)