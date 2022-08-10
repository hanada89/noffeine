from django.db import models
from datetime import datetime
# Create your models here.


class CafeInfo(models.Model):
    cafe_no = models.AutoField(primary_key=True)
    cafe_name = models.JSONField(default=dict) ## 검색시 json보다는 / key 검색?
    #cafe_name_kor = models.CharField(max_length=100)
    #cafe_name_eng = models.CharField(max_length=100)
    cafe_tel = models.CharField(max_length=15)
    opening_time = models.JSONField(default=dict)
    is_operating = models.BooleanField(default=True)
    cafe_sns = models.JSONField(default=dict)
    reg_dtime = models.DateTimeField(auto_now_add=True)
    mod_dtime = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cafe_info'

    

class CafeAddr(models.Model):
    cafe_no = models.AutoField(primary_key=True)
    addr_depth_1 = models.CharField(max_length=5) ## 서울특별시, 대구광역시, 경기도
    addr_depth_2 = models.CharField(max_length=5) ## 광진구, 의왕시
    addr_depth_3 = models.CharField(max_length=10) ## 학의로, 내손순환로
    addr_depth_4 = models.CharField(max_length=20) ## 상세주소
    latitude =  models.DecimalField(max_digits=10, decimal_places=7) ## 위도
    longitude = models.DecimalField(max_digits=11, decimal_places=7) ## 경도 
    reg_dtime = models.DateTimeField(auto_now_add=True)
    mod_dtime = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cafe_addr'

    
class CafeMenu(models.Model):
    cafe_no = models.AutoField(primary_key=True)
    menu_url =  models.TextField(blank=True, null=True)
    reg_dtime = models.DateTimeField(auto_now_add=True)
    mod_dtime = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cafe_menu'
