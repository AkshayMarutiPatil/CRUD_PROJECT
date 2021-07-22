from django.shortcuts import render


from rest_framework.decorators import api_view
from .serializer import TestModelSerializer,GetLimitedDataSerializer
from .models import CrudModel
from django.http import JsonResponse


@api_view(['POST'])
def create_test_record(request):
    re=request.data
    print(re)
    test_model_serializer = TestModelSerializer(data=re)
    if test_model_serializer.is_valid():
        test_model_serializer.save()
        return JsonResponse({"message": "success", "status": 200, "responce": test_model_serializer.data})
    else:
        return JsonResponse({"message": "failed", "status": 500, "responce": test_model_serializer.errors})

@api_view(['POST'])
def get_one_record(request):
    re=request.data
    check_type_1=CrudModel.objects.filter(id=re['id']).exists()
    if check_type_1:
        record=CrudModel.objects.get(id=re['id'])
        serializer=GetLimitedDataSerializer(record)
        return JsonResponse({"message":"success","status":200,"responce":serializer.data})
    else:
        return JsonResponse({"message": "Record Does Not Exist", "status": 200, "responce": []})


@api_view(['PATCH'])
def update_test_record(request):
    re = request.data
    record=CrudModel.objects.get(id=re["id"])
    test_model_serializer=TestModelSerializer(record,data=re,partial=True)
    if test_model_serializer.is_valid():
        test_model_serializer.save()
        return JsonResponse({"message":"Success","Status":200,"responce":test_model_serializer.data})
    else:
        return JsonResponse({"message":"failed","Status":500,"responce":test_model_serializer.errors})









@api_view(['POST'])
def delete_one_record(request):
    re=request.data


    check_type_1 = CrudModel.objects.filter(id=re['id']).exists()
    if check_type_1:
        record = CrudModel.objects.get(id=re['id'])
        record.delete()
        return JsonResponse({"message": "Record Deleted"})
    else:
        return JsonResponse({"message": "Record Does Not Exist", "status": 200, "responce": []})







