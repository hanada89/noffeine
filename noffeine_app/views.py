# Create your views here.

## Django Package
from django.shortcuts import get_object_or_404, render, redirect
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
## 전체 카페 조회(get), 생성(post)
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
    
    
## 특정(pk) 카페 조회(get), 수정(put), 삭제(delete) 
## FBV
@api_view((['GET', 'PUT', 'DELETE']))
def CafeInfoDetailAPI(request, cafe_no):
    cafe = CafeInfo.objects.get(pk=cafe_no)
    
    if request.method == 'GET':
        queryset = CafeInfoSelect(cafe)
        return Response(queryset.data)
    
    elif request.method == 'PUT':
        queryset = CafeInfoInsert(cafe, data=request.data)
        if queryset.is_valid():
            queryset.save()
            return Response(queryset.data, status=status.HTTP_201_CREATED)
        else:
            return Response(queryset.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        cafe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
'''
class CafeInfoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = CafeMenu.objects.all()
    serializer_class = CafeInfoSelect
    lookup_field = 'cafe_no'
''' 
    
    
###############################################
# cafeAddr 카페별 주소 관리 API
###############################################

## 전체 조회, 생성
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
    
## 특정(pk) 카페 조회(get), 수정(put), 삭제(delete) 
## CBV > APIView
class CafeAddrDetailAPI(APIView):
    def get(self, request, cafe_no):
        #addr = get_object_or_404(CafeAddr, id=cafe_no)
        addr = CafeAddr.objects.get(pk=cafe_no)
        queryset = CafeAddrSelect(addr)
        return Response(queryset.data, status=status.HTTP_200_OK)


    def put(self, request, cafe_no):
        addr = CafeAddr.objects.get(pk=cafe_no)
        queryset = CafeAddrInsert(addr, data=request.data)
        if queryset.is_valid():
            queryset.save()
            return Response(queryset.data, status=status.HTTP_201_CREATED)
        else:
            return Response(queryset.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, cafe_no):
        #addr = get_object_or_404(CafeAddr, cafe_no)
        addr = CafeAddr.objects.get(pk=cafe_no)
        addr.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
'''
class CafeAddrDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = CafeMenu.objects.all()
    serializer_class = CafeAddrSelect
    lookup_field = 'cafe_no'
''' 
    
       
###############################################
# cafeMenu 카페 메뉴 URL 처리하는 API
###############################################
## 전체 조회(get), 추가(post), 수정(put), 삭제(delete)
## CBV > mixins
class CafeMenuAPI(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = CafeMenu.objects.all()
    serializer_class = CafeMenuSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


## 특정 카페 수정(update)
## CBV > mixins
class CafeMenuDetailAPI_update(mixins.UpdateModelMixin, GenericAPIView):
    queryset = CafeMenu.objects.all()
    serializer_class = CafeMenuSerializer
    lookup_field = 'cafe_no'
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    
## 특정 카페 조회(retrive), 삭제(destory)
## CBV > generics
class CafeMenuDetailAPI_retrieve_destory(generics.RetrieveDestroyAPIView): 
    ## generics.RetrieveUpdateDestroyAPIView >> 조회,수정,삭제
    queryset = CafeMenu.objects.all()
    serializer_class = CafeMenuSerializer
    lookup_field = 'cafe_no'
    
