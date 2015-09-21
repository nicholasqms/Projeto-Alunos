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
from alunos.views import StudentList, StudentCreate, StudentUpdate, StudentDelete
from alunos import views
from django.contrib.auth import views as auth_views


urlpatterns = [
#	url(r'^',StudentList.as_view(),name='main'),
    url(r'students/create/$', StudentCreate.as_view(), name='student_add'),
    url(r'students/(?P<pk>[0-9]+)/$', StudentUpdate.as_view(), name='student_update'),
    url(r'students/(?P<pk>[0-9]+)/delete/$', StudentDelete.as_view(), name='student_delete'),
	#url(r'^',include('django.contrib.auth.urls')),
    url(r'^login/$', auth_views.login),
    url(r'^password_change/$',auth_views.password_change,name='password_change'),
    url(r'^password_reset/$',auth_views.password_reset,name='password_reset'),
    url(r'^password_reset/done/$',auth_views.password_reset_done,name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm,name='password_reset_confirm'),
#    url(r'^students/login/$', views.StudentUserLogin, name='login'),
    url(r'^logout/$', auth_views.logout,{'next_page':'homepage'}, name ='logout'),
	#url(r'^alunos/', TemplateView.as_view(template_name="alunos.html")),
#    url(r'students/adduser', views.StudentAddUser, name = 'add_student_user'),
    url(r'students/create', views.StudentCreateUser, name = 'create_student_user'),
    url(r'students/users/(?P<pk>[0-9]+)$', StudentUserUpdate.as_view(), name='studentuser_update'),
    url(r'students/users/(?P<pk>[0-9]+)/delete/$', StudentUserDelete.as_view(), name='studentuser_delete'),
    url(r'teachers/users/create', views.TeacherCreateUser, name = 'create_teacher_user'),
    url(r'teachers/users/', TeacherUserList.as_view(), name = 'teacheruser-list'),
    url(r'teachers/users/(?P<pk>[0-9]+)$', TeacherUserUpdate.as_view(), name='teacheruser_update'),
    url(r'teachers/users/(?P<pk>[0-9]+)/delete/$', TeacherUserDelete.as_view(), name='teacheruser_delete'),
    url(r'students/(?P<pk>[0-9]+)$', StudentUpdate.as_view(), name='student_update'),
    url(r'students/(?P<pk>[0-9]+)/delete/$', StudentDelete.as_view(), name='student_delete'),
    #url(r'^logoutlogin/', auth_views.logout_then_login{'login_url':'login'},name='logout-login')
    url(r'^admin/', include(admin.site.urls)),
    url(r'^students/users/$',StudentUserList.as_view(),name='studentuser-list'),
    url(r'^students/$',StudentList.as_view(),name='student-list'),
#    url(r'^',include('django.contrib.auth.urls')),
    url(r'^home/$',HomePageView.as_view(),name='homepage'),
    url(r'^',HomePageView.as_view(),name='main'),
]