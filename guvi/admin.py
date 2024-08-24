from django.contrib import admin
from guvi.models import Courses


class CourseAdmin(admin.ModelAdmin):
    list_display=['cname','author']


admin.site.register(Courses,CourseAdmin)
# Register your models here.

