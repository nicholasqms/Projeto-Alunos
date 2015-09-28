from django.contrib import admin
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
#from .backends import studentbackend
# Register your models here.

from alunos.models import StudentStatus,StudentBolsa,Student,Orientador,orientadorFieldsList,studentFieldsList

#admin.site.register(Student)
#admin.site.register(Orientador)
#admin.site.register(Grade)
#@admin.register(Student)
admin.site.register(StudentStatus)
admin.site.register(StudentBolsa)
class StudentAdmin(admin.ModelAdmin):
    fields = studentFieldsList
    list_display = ('name','tipo')
    pass
    
#@admin.register(Orientador, verbose_name = 'Orientadores')
class OrientadorAdmin(admin.ModelAdmin):
    name = 'Orientadores'
    fields = orientadorFieldsList
    list_display = ('name','is_active','is_admin')

admin.site.register(Student,StudentAdmin)
admin.site.register(Orientador,OrientadorAdmin)

# Now register the new UserAdmin...
#admin.site.register(Student)# ,MyUserAdmin)
#admin.site.register(TeacherUser)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
#admin.site.unregister(Group)

	
