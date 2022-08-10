# Create your views here.

## Django Package
from django.shortcuts import render, redirect
from .models import CafeInfo, CafeAddr, CafeMenu

## DRF Package
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

## Serializer
from .serializers import CafeInfoSelect, CafeInfoInsert, CafeAddrSelect, CafeAddrInsert, CafeMenuSerializer

## DRF Serializer 심화
from rest_framework.generics import GenericAPIView
from rest_framework import mixins

from rest_framework import generics

import traceback 

## Django API
#def cafe_get(request):
#    cafe_list = CafeInfo.objects.
#    return render(request, )


## DRF API
@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")


###############################################
# cafeInfo
###############################################
## FBV 
@api_view((['GET','POST']))
def CafeInfoAPI(request):
    try:
        if request.method == 'GET':
            cafes = CafeInfo.objects.all()
            queryset = CafeInfoSelect(cafes, many=True)
            return Response(queryset.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            queryset = CafeInfoInsert(data=request.data)
            if queryset.is_valid():
                queryset.save()
                return Response(queryset.data, status=status.HTTP_201_CREATED)
            else:
                return Response(queryset.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        traceback.print_exc()
    


###############################################
# cafeAddr
###############################################
## 시리얼라이저 get, set 시 동일하게 처리가 가능한가? 에러가 나서 분리함 (자동증가, 자동추가 등)
## CBV > APIView 
class CafeAddrAPI(APIView):
    def get(self, request):
        addrs = CafeAddr.objects.all()
        queryset = CafeAddrSelect(addrs, many=True)
        return Response(queryset.data, status=status.HTTP_200_OK)

    def post(self, request):
        queryset = CafeAddrInsert(data=request.data)
        if queryset.is_valid():
            queryset.save()
            return Response(queryset.data, status=status.HTTP_201_CREATED)
        else:
            return Response(queryset.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
###############################################
# cafeMenu
###############################################
## CBV > mixins
class CafeMenuAPI(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = CafeMenu.objects.all()
    serializer_class = CafeMenuSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



## CBV > generics
class CafeMenuDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = CafeMenu.objects.all()
    serializer_class = CafeMenuSerializer
    lookup_field = 'cafe_no'
    
