from encodings import search_function
from django.contrib import admin
from .models import Books, Quiz, Answer, Subject

# Register your models here.


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    verbose_name = "Books"
    list_display = ['title', 'grade', 'subject']
    search_fields = ['title', 'grade', 'subject']


class AnswersInline(admin.TabularInline):
    model = Answer


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['question']
    inlines = [AnswersInline]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(Answer)
