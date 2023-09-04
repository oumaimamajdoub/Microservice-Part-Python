
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cars,User
from .serializers import CarsSerializer
import random


class CarsViewSet(viewsets.ViewSet):
    def list(self, request):
        cars=cars.objects.all()
        serializer = CarsSerializer(cars,many=True)
        return Response(serializer.data)

    def create(self, request):
       
        serializer = CarsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

    def retrieve(self, request, pk=None):
       
        car = car.objects.get(id=pk)
        serializer = CarsSerializer(car)
        return Response(serializer.data) 

    def update(self, request, pk=None):
    
        car = car.objects.get(id=pk)
        serializer = CarsSerializer(instance=car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED) 

    def destroy(self, request, pk=None):
         car = car.objects.get(id=pk)
         car.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
         



    class UserAPIView(APIView):
            def get(self, _):
                users = User.objects.all()
                user = random.choice(users)
                return Response({
                    'id': user.id
                }) 
            
            
