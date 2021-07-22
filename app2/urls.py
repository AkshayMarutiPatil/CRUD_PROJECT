from django.conf.urls import  url
from .views import create_test_record,update_test_record,delete_one_record,get_one_record


urlpatterns=[
    url(r'addrecord',create_test_record),
    url(r'update',update_test_record),
    url(r'delete',delete_one_record),
    url(r'get',get_one_record),

]