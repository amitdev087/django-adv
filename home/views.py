from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

from .serializer import *
@api_view(["GET"])
def getTodo(request):
    todo_objs=Todo.objects.all()
    serializer=TodoSerializer(todo_objs,many=True)

    return Response({'status':'success',
    'massage':'todo fetched',
    "data":serializer.data
    })
@api_view(["GET","POST"])
def post_Todo(request):
    try:
        data=request.data
        print(data)
        serializers=TodoSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            print(serializers.data)
            return Response({
                'status':'success',
                'message':"200",
                "data":serializers.data
                })
        return Response({
        'status':'error',
        'message':"invalid data",
        'data':serializers.errors
         }) 
    except Exception as e:
        print(e)
        return Response({
        'status':'error',
        'message':"404",
         })

@api_view(['GET','PATCH'])
def patch_todo(request):
    try:
        data=request.data
        if not (request.data.get("uid")):
          return Response({
        'status':'error',
        'message':"uid is msut",
        "data":{}
         })  

        obj=Todo.objects.get(uid=data.get('uid'))
        serializers=TodoSerializer(obj,data=data,partial=True)
        if serializers.is_valid():
            serializers.save()
            print(serializers.data)
            return Response({
                'status':'success',
                'message':"200",
                "data":serializers.data
                })

        return Response({
        'status':'error',
        'message':"invalid data",
        'data':serializers.errors
         })   
    except Exception as e:
        print(e)
        return Response({
        'status':'flase',
        'message':"invalid uid",
        'data':{}
         })  
         

@api_view(['GET',"POST",'PATCH'])
def home(request):
    if request.method=="GET":
        return Response({
            'status':'success',
            'message':"django is working",
            'methodCalled':"GET"
        })

    elif request.method=="POST":
        return Response({
            'status':'success',
            'message':"django is working",
            'methodCalled':"POST"
        })
    elif request.method=="PATCH":
        return Response({
            'status':'success',
            'message':"django is working",
            'methodCalled':"PATCH"
        })
    else:
        return Response({
            'status':'error',
            'message':"404",
            'methodCalled':"error"
        })


class Todo(APIView):
    def get(self,request):
        return Response({
            'status':'success',
            'message':"django is working",
            'methodCalled':"GET"
        })

    def post(self,requests):
         return Response({
            'status':'success',
            'message':"django is working",
            'methodCalled':"POST"
        })


