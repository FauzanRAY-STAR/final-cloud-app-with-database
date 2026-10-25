
from django.contrib import admin
from .models import (
    Course,
    Lesson,
    Instructor,
    Learner,
    Question,
    Choice,
    Submission,
)


# Inline lessons inside a course
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Inline choices inside a question
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


# Course administration
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# Question administration
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'course', 'grade']
    search_fields = ['question_text']


# Lesson administration
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
    search_fields = ['title']


# Register models in Django Admin
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
