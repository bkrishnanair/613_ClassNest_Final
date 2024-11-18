from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'thumbnail')

admin.site.register(Course, CourseAdmin)
