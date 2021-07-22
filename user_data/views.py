from .serializer import UserSerializer,LimitedSerializer,ProfessorSerializer,StudentListSerializer,ProfessorListSerializer
from .models import UserModel,StudentModel,Professor
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination


# Create your views here.

@api_view(['POST'])
def create_record(request):
    data=request.data
    serializer=UserSerializer(data=data)
    if serializer.is_valid():
        serializer.create(validated_data=data)
        return JsonResponse({"message":"success","responce":data},status=201)
    else:
        return JsonResponse(serializer.errors,status=400)

from django.core import serializers
import json
@api_view(['POST'])
def get_record(request):
    re=request.data
    id=re['user_id']
    print(id)
    check=UserModel.objects.filter(user_id=id).exists()
    if check:
        check2=StudentModel.objects.filter(user_id=id).exists()
        check3=Professor.objects.filter(user_id=id).exists()
        # user=UserModel.objects.get(user_id=id)
        # qs_json = serializers.serialize('json', stud)
        if check2:
            # stud = StudentModel.objects.get(user_id=id)
            # data = {"user_type":stud.user_id.user_type,"full_name": stud.full_name, "gender": stud.gender, "dob": stud.dob, "std": stud.std,
            #         "email":stud.user_id.email,"caste": stud.caste, "specilization": stud.specilization, "mobile": stud.user_id.mobile}

            record=StudentModel.objects.get(user_id=id)
           # print(record)
            serializer=LimitedSerializer(record)
            #print(serializer)
            return JsonResponse({"message":"success","responce":serializer.data})
        elif check3:
            record=Professor.objects.get(user_id=id)
            serializer=ProfessorSerializer(record)
            #prof=Professor.objects.get(user_id=id)
            #data={"user_type":prof.user_id.user_type,"full_name":prof.full_name,"city":prof.city,"professor_specilization":prof.professor_specilization,"email":prof.user_id.email,"mobile":prof.user_id.mobile}
            return JsonResponse({"message":"success","responce":serializer.data})

    else:
        return JsonResponse({"message": "record does not exits"})

@api_view(['PATCH'])
def update(request):
    re=request.data
    id=re['user_id']
    print(id)
    check1=UserModel.objects.filter(user_id=id).exists()
    if check1:
        check2 = StudentModel.objects.filter(user_id=id).exists()
        check3 = Professor.objects.filter(user_id=id).exists()
        if check2:
            record=StudentModel.objects.get(user_id=id)
            print(record)
            serializer=LimitedSerializer(record,data=re,partial=True)
            if serializer.is_valid():
                serializer.save()
                print(serializer)
                return JsonResponse({"message": "Success", "Status": 200, "responce": serializer.data})
            else:
                return JsonResponse({"message": "failed", "Status": 500, "responce": serializer.errors})
        elif check3:
            record = Professor.objects.get(user_id=id)
            serializer = ProfessorSerializer(record, data=re, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Success", "Status": 200, "responce": serializer.data})
            else:
                return JsonResponse({"message": "failed", "Status": 500, "responce": serializer.errors})


    else:
        return JsonResponse({"message": "record does not exits"})

@api_view(['POST'])
def delete(request):
    re=request.data
    id=re['user_id']
    check1=UserModel.objects.filter(user_id=id).exists()
    if check1:
        record=UserModel.objects.get(user_id=id)
        record.delete()
        return JsonResponse({"message": "Record Deleted"})
    else:
        return JsonResponse({"message": "Record Does Not Exist", "status": 200, "responce": []})

    # re = request.data
    #
    # check_type_1 = CrudModel.objects.filter(id=re['id']).exists()
    # if check_type_1:
    #     record = CrudModel.objects.get(id=re['id'])
    #     record.delete()
    #     return JsonResponse({"message": "Record Deleted"})
    # else:
    #     return JsonResponse({"message": "Record Does Not Exist", "status": 200, "responce": []})

@api_view(['GET'])
def StudentList(request):
    paginator=PageNumberPagination()
    paginator.page_size=2
    student_object=StudentModel.objects.all().order_by('-user_id')
    #print(student_object)
    # stu=[]
    # for i in student_object:
    #     stu.extend([i.full_name,i.city,i.gender])


    result_page=paginator.paginate_queryset(student_object,request)
    serializer=StudentListSerializer(result_page,many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def ProfessorList(request):
    paginator=PageNumberPagination()
    paginator.page_size=2
    professor_object=Professor.objects.all()
    result_page=paginator.paginate_queryset(professor_object,request)
    serializer=ProfessorListSerializer(result_page,many=True)
    return paginator.get_paginated_response(serializer.data)



