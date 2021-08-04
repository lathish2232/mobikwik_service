from django.shortcuts import render


from django.http import JsonResponse, request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from atm_service.impl.processAtmService import get_all_data, get_data_by_id,insert_data,delete_data_by_id
# Create your views here.


@csrf_exempt
@api_view(['GET'])
def atm_data(request):
    return get_all_data(request)

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def process_atm_service(request,id):
    print(request.method)
    if request.method=='GET':
        return get_data_by_id(request,id)
    elif request.method=='DELETE':
        print('i am in ---------------------------')
        return delete_data_by_id(request,id)
    elif request.method=='PUT':
        pass

def del_item(request,id):
    return delete_data_by_id(request,id)


@csrf_exempt
@api_view(['POST'])
def add_item(request):
    return insert_data(request)
