from django.conf.urls import  url
from .views import create_record,get_record,update,delete,StudentList,ProfessorList


urlpatterns=[
    url(r'test/add',create_record),
    url(r'test/get_data',get_record),
    url(r'test/update',update),
    url(r'test/delete',delete),
    url(r'test/student_list',StudentList),
    url(r'test/professor_list',ProfessorList)
]