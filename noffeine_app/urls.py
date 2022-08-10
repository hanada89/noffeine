from django.urls import path, include
from .views import HelloAPI, CafeInfoAPI, CafeAddrAPI, CafeMenuAPI, CafeMenuDetailAPI




urlpatterns = [
    #path('cafe_get/' )
    
    path('hello/', HelloAPI),
    path('cafe/', CafeInfoAPI, name='test'),
    path('cafe-addr/', CafeAddrAPI.as_view()),
    path('cafe-menu/', CafeMenuAPI.as_view()),
    path('detail/cafe-menu/<int:cafe_no>', CafeMenuDetailAPI.as_view()),
]

