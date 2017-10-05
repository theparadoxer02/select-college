from django.contrib import admin
from .models import College, City, Location, Courses, CollegeInfo
# Register your models here.

admin.site.register(College)
admin.site.register(Location)
admin.site.register(City)
admin.site.register(Courses)
admin.site.register(CollegeInfo)


# class CollegeAdmin(admin.ModelAdmin):
#     list_display = ['name', 'location', 'get_city', 'courses_offered']
