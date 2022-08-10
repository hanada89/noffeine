from dataclasses import field
from email.policy import default
from rest_framework import serializers
from .models import CafeInfo, CafeAddr, CafeMenu


###############################
# Cafe Info >> serializer
###############################
class CafeInfoSelect(serializers.Serializer):
    cafe_no = serializers.IntegerField(help_text='PK') ## primary_key=True error ??????????? 오타인듯
    cafe_name = serializers.JSONField(default=dict)
    cafe_tel = serializers.CharField(max_length=15)
    opening_time = serializers.JSONField(default=dict)
    is_operating = serializers.BooleanField(default=True)
    cafe_sns = serializers.JSONField(default=dict)
    reg_dtime = serializers.DateTimeField()
    mod_dtime = serializers.DateTimeField()
    
    def create(self, validated_data):
        return CafeInfo.objects.create(**validated_data)
    
    def update(self, instance, validated_Data): ## 전부 다 넣어줘야함 >> 자동으로 들어가는건 제거 
        instance.cafe_no = validated_Data.get('cafe_no', instance.cafe_no)
        instance.cafe_name = validated_Data.get('cafe_name', instance.cafe_name)
        instance.cafe_tel = validated_Data.get('cafe_tel', instance.cafe_tel)
        instance.opening_time = validated_Data.get('opening_time', instance.opening_time)
        instance.is_operating = validated_Data.get('is_operating', instance.is_operating)
        instance.cafe_sns = validated_Data.get('cafe_sns', instance.cafe_sns)
        instance.reg_dtime = validated_Data.get('reg_dtime', instance.reg_dtime)
        instance.mod_dtime = validated_Data.get('mod_dtime', instance.mod_dtime)    
   
'''  
class CafeInfoSelect(serializers.ModelSerializer):
    class Meta:
        model = CafeInfo
        fields = ['cafe_no', 'cafe_name', 'cafe_tel', 'opening_time', 'is_operating', 'cafe_sns', 'reg_dtime', 'mod_dtime']     
'''

class CafeInfoInsert(serializers.ModelSerializer):
    class Meta:
        model = CafeInfo
        fields = ['cafe_name', 'cafe_tel', 'opening_time', 'is_operating', 'cafe_sns']     

## 인서트시에는 자동채워지는건 제외하고 해야하는건지 > 심화버전하면 해결되는건지 ?????????

    

###############################
# Cafe Addr >> Model Serializer
###############################        
class CafeAddrSelect(serializers.ModelSerializer):
    class Meta:
        model = CafeAddr
        fields = ['cafe_no', 'addr_depth_1', 'addr_depth_2', 'addr_depth_3', 'addr_depth_4', 'latitude', 'longitude', 'reg_dtime', 'mod_dtime']

class CafeAddrInsert(serializers.ModelSerializer):
    class Meta:
        model = CafeAddr
        fields = ['addr_depth_1', 'addr_depth_2', 'addr_depth_3', 'addr_depth_4', 'latitude', 'longitude']
        
               
        
###############################
# Cafe Menu >> Model Serializer
###############################
class CafeMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CafeMenu
        fields = ['cafe_no', 'menu_url', 'reg_dtime', 'mod_dtime']
        
        
    