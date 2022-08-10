from django.urls import path, include
from .views import HelloAPI, CafeInfoAPI, CafeAddrAPI, CafeMenuAPI, \
        CafeInfoDetailAPI, CafeAddrDetailAPI, CafeMenuDetailAPI_update, CafeMenuDetailAPI_retrieve_destory




urlpatterns = [
    #path('cafe_get/' )
    
    path('hello/', HelloAPI),
    
    path('cafe/cafe', CafeInfoAPI, name='test'),
    path('cafe/detail/<int:cafe_no>', CafeInfoDetailAPI),
    
    path('addr/addr', CafeAddrAPI.as_view()),
    path('addr/detail/<int:cafe_no>', CafeAddrDetailAPI.as_view()),
    
    path('menu/menu', CafeMenuAPI.as_view()),
    path('menu/detail/update/<int:cafe_no>', CafeMenuDetailAPI_update.as_view()),
    path('menu/detail/select-delete/<int:cafe_no>', CafeMenuDetailAPI_retrieve_destory.as_view()),
]

