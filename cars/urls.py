from django.urls import path

from .views import  CarsViewSet
from .views import UserAPIView


urlpatterns = [
    path('cars', CarsViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('cars/<str:pk>', CarsViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user', UserAPIView.as_view()),
    

   path('', UserAPIView.as_view({'get': 'say_hello'}), name='say_hello'),

]