from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app_api.sender import rabbitmq_api, kafka_api
from app_api.cheking.authen_checking import authen_pass
from app_api.cheking.url_checking import url_pass
from app_api.date import getdate


@api_view(['POST'])
def Rest_Api_Test(request):

    header_origin_get=request.headers.get('origin')
    header_authen_get=request.headers.get('Authorization')

    if (authen_pass(header_authen_get) and url_pass(header_origin_get))==True:
        # rabbitmq_api.Rabbitmq_Send_Message(request.data)
        request.data["time_stamp"]=getdate.get_date_zone()
        kafka_api.Kafka_Send_Message(request.data)
        print(request.data)
        # return Response(data=request.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_201_CREATED)
            
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST) 
