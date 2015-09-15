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
from django.conf.urls import include
from django.http import HttpResponse
from alunos.views import StudentUserUpdate, StudentUserDelete, TeacherUserUpdate, TeacherUserDelete, StudentAddUser
from alunos.views import StudentCreateUser,StudentUserLogin,StudentUserList,TeacherCreateUser,TeacherUserLogin,TeacherUserList, HomePageView, StudentUserLogout
from alunos import views

urlpatterns = [
#	url(r'^',StudentList.as_view(),name='main'),
#	url(r'^',include('django.contrib.auth.urls')),
    url(r'^students/login/$', views.StudentUserLogin, name='login'),
    url(r'^logout$', views.StudentUserLogout, name ='logout'),
	#url(r'^alunos/', TemplateView.as_view(template_name="alunos.html")),
#    url(r'students/adduser', views.StudentAddUser, name = 'add_student_user'),
    url(r'students/create', views.StudentCreateUser, name = 'create_student_user'),
    url(r'students/(?P<pk>[0-9]+)$', StudentUserUpdate.as_view(), name='student_update'),
    url(r'students/(?P<pk>[0-9]+)/delete/$', StudentUserDelete.as_view(), name='student_delete'),
    url(r'teachers/create', views.TeacherCreateUser, name = 'create_teacher_user'),
    url(r'teachers/', TeacherUserList.as_view(), name = 'teacheruser-list'),
    url(r'teachers/(?P<pk>[0-9]+)$', TeacherUserUpdate.as_view(), name='teacher_update'),
    url(r'teachers/(?P<pk>[0-9]+)/delete/$', TeacherUserDelete.as_view(), name='teacher_delete'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'students/',StudentUserList.as_view(),name='studentuser-list'),
#    url(r'^',include('django.contrib.auth.urls')),
    url(r'home',HomePageView.as_view(),name='homepage'),
#    url(r'^',HomePageView.as_view(),name='main'),
]
