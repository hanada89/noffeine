"""noffeine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include

## swagger
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

## permission
#from rest_framework.permissions import AllowAny
from rest_framework import permissions

from django.conf import settings
## from django.conf.urls import url # <- error?????????????????
from django.urls import re_path



## swagger DOC
schema_cafe_info = get_schema_view(
    openapi.Info(
        title = '노페인 API 목록',
        default_version = 'v1',
        description = '디카페인 카페를 제공하는 노페인 앱에서 사용하는 API 목록',
    ),
    public = True,
    #permission_classes = (permissions.AllowAny,),
)



## urls
urlpatterns = [
    ## urls
    path('admin/', admin.site.urls),
    path('noffeine_app/', include('noffeine_app.urls')),
    
    ## swagger 
    ## url은 위의 conf에서 에러, path하면 출력이 안됨
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_cafe_info.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_cafe_info.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_cafe_info.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

'''
## Debug 일때, 문서가 보이도록 설정
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_cafe_info.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_cafe_info.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_cafe_info.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    ]
'''
