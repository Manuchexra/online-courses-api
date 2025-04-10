from django.contrib import admin
from .models import Course, Chapter, Lesson, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'created_by', 'created_at')
    search_fields = ('title',)
    list_filter = ('level', 'created_at')
    ordering = ('-created_at',)

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    search_fields = ('title', 'course__title')
    ordering = ('course',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'is_free_preview')
    search_fields = ('title', 'chapter__title')
    list_filter = ('is_free_preview',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at')
    search_fields = ('user__username', 'course__title')
    list_filter = ('enrolled_at',)
