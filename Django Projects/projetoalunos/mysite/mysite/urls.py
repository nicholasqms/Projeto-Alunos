"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from django.http import HttpResponse
from django.contrib import admin
from alunos.models import Student, Teacher
from alunos.views import StudentList, TeacherList, StudentCreate, StudentUpdate, StudentDelete, TeacherCreate, TeacherUpdate, TeacherDelete

urlpatterns = [
	url(r'^',include('django.contrib.auth.urls')),
        url(r'^students/all', StudentList.as_view(), name='student-list'),	
        url(r'^teachers/all', TeacherList.as_view(),name='teacher-list'),
	#url(r'^alunos/', TemplateView.as_view(template_name="alunos.html")),
    
    url(r'students/add/$', StudentCreate.as_view(), name='student_add'),
    url(r'students/(?P<pk>[0-9]+)/$', StudentUpdate.as_view(), name='student_update'),
    url(r'students/(?P<pk>[0-9]+)/delete/$', StudentDelete.as_view(), name='student_delete'),
    url(r'teachers/add/$', TeacherCreate.as_view(), name='teacher_add'),
    url(r'teachers/(?P<pk>[0-9]+)/$', TeacherUpdate.as_view(), name='teacher_update'),
    url(r'teachers/(?P<pk>[0-9]+)/delete/$', TeacherDelete.as_view(), name='teacher_delete'),
    url(r'^admin/', include(admin.site.urls)),
]
