from django.contrib import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'thumbnail')

admin.site.register(Course, CourseAdmin)

admin.site.register(Module)
admin.site.register(Recording)
admin.site.register(Assignment)
admin.site.register(Material)