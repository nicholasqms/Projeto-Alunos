from django.contrib import admin

# Register your models here.

from .models import Student, Teacher, Grade

#admin.site.register(Student)
#admin.site.register(Grade)
admin.site.register(Teacher)


class GradeInLine (admin.TabularInline):
	model = Grade
	extra = 3

class StudentAdmin (admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['subject']}),
	('Birth Date', {'fields': ['birth_date']}),
	('DRE', {'fields': ['dre']}),
	('Course', {'fields': ['course']}),
 ]
	inlines = [GradeInLine]

admin.site.register(Student,StudentAdmin)	
