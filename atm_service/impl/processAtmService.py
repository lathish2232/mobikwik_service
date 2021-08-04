
from atm_service.db_utils.db_connections import get_mongod_connection
from django.http import JsonResponse, request
from rest_framework import status


from resources.atm_dict import atmdata

db=get_mongod_connection()
def get_all_data(request):
    response={"code":200,"data":atmdata}
    return JsonResponse(response,status=status.HTTP_200_OK)


def get_data_by_id(request,id):
    rec=db['atmService'].find_one({'atmId':id}, {'_id': 0})
    if rec:
        data={"code":200, "message":"successful","data":rec}
        response=JsonResponse(data,status=status.HTTP_200_OK)
    else:
        data={"code":204,"message":f'id:- {id} not found', "data":"no data" }
        response=JsonResponse(data,status=status.HTTP_204_NO_CONTENT)
    return response
def update_data_by_id(request,id):
    pass

def delete_data_by_id(request,id):
    rec=db['atmService'].delete_one({'atmId':id})
    data={"code":200, "message":f"id {id} Deleted successfully"}
    response=JsonResponse(data,status=status.HTTP_202_ACCEPTED)
    return response
    

def insert_data(request):
    rec=request.data
    rec=db['atmService'].insert_one({rec})
    data={"code":202,"message":"one record inserted Successfully"}
    response=JsonResponse(data,status=status.HTTP_201_CREATED)

