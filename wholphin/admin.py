from django.contrib import admin
from .models import CoursesDetail, Courses, UsersComment, StudentRegistered, Carousel


class CoursesPriceInline(admin.StackedInline):
    model = CoursesDetail


class CoursesAdmin(admin.ModelAdmin):
    inlines = [CoursesPriceInline]
    list_display = ['course_title', 'description', 'date_pub']
    list_filter = ['date_pub']
    search_fields = ['title']


class CoursesDetailAdmin(admin.ModelAdmin):
    list_display = ['course_subtitle']
    list_filter = ['course_subtitle']
    search_fields = ['course_subtitle']


admin.site.register(Courses, CoursesAdmin)
admin.site.register(CoursesDetail, CoursesDetailAdmin)
admin.site.register(UsersComment)
admin.site.register(StudentRegistered)
admin.site.register(Carousel)