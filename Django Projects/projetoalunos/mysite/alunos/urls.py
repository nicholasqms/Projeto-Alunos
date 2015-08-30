from django.conf.urls import url
from django.conf.urls import include
from django.http import HttpResponse
from django.contrib import admin
from . import views
from alunos.models import Student, Teacher
from alunos.views import StudentList, TeacherList, StudentCreate, StudentUpdate, StudentDelete, TeacherCreate, TeacherUpdate, TeacherDelete

urlpatterns = [
        url(r'^students/', StudentList.as_view()),	
        url(r'^teachers/', TeacherList.as_view()),
	#url(r'^alunos/', TemplateView.as_view(template_name="alunos.html")),
    
    url(r'student/add/$', StudentCreate.as_view(), name='student_add'),
    url(r'student/(?P<pk>[0-9]+)/$', StudentUpdate.as_view(), name='student_update'),
    url(r'student/(?P<pk>[0-9]+)/delete/$', StudentDelete.as_view(), name='student_delete'),
    url(r'teacher/add/$', TeacherCreate.as_view(), name='teacher_add'),
    url(r'teacher/(?P<pk>[0-9]+)/$', TeacherUpdate.as_view(), name='teacher_update'),
    url(r'teacher/(?P<pk>[0-9]+)/delete/$', TeacherDelete.as_view(), name='teacher_delete'),
]
