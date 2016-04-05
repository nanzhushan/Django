#coding:utf8
from django.contrib import admin
from .models import Question,Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')

##加入到后台
admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)