from django.conf.urls import url
from django.conf.urls import include
from django.http import HttpResponse
from django.contrib import admin
from . import views
from alunos.models import Student, Teacher
from alunos.views import StudentList, TeacherList

urlpatterns = [
        url(r'^students/', StudentList.as_view('./templates/alunos/student_list.html')),	
        url(r'^teachers/', TeacherList.as_view('./templates/alunos/teacher_list.html')),
	#url(r'^alunos/', TemplateView.as_view(template_name="alunos.html")),
]
