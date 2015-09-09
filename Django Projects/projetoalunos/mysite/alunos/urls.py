from django.conf.urls import url
from django.conf.urls import include
from django.http import HttpResponse
from django.contrib import admin
from . import views
from alunos.models import Student, Teacher, Grade
from alunos.views import StudentList, TeacherList, StudentCreate, StudentUpdate, StudentDelete, TeacherCreate, TeacherUpdate, TeacherDelete, StudentAddUser

urlpatterns = [
	url(r'^',include('django.contrib.auth.urls')),
        url(r'^students/all', StudentList.as_view(),name ='student-list'),	
        url(r'^teachers/all', TeacherList.as_view(),name ='teacher-list'),
	#url(r'^alunos/', TemplateView.as_view(template_name="alunos.html")),
    url(r'students/adduser', views.StudentAddUser, name == 'add_student_user'),
    url(r'students/add/$', StudentCreate.as_view(), name='student_add'),
    url(r'students/(?P<pk>[0-9]+)/$', StudentUpdate.as_view(), name='student_update'),
    url(r'students/(?P<pk>[0-9]+)/delete/$', StudentDelete.as_view(), name='student_delete'),
    url(r'teachers/add/$', TeacherCreate.as_view(), name='teacher_add'),
    url(r'teachers/(?P<pk>[0-9]+)/$', TeacherUpdate.as_view(), name='teacher_update'),
    url(r'teachers/(?P<pk>[0-9]+)/delete/$', TeacherDelete.as_view(), name='teacher_delete'),
]
