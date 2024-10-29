from rest_framework import serializers
from .models import *


class TeamMemberSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = TeamMember
        fields = '__all__'
        #fields = ['name', 'designation', 'address','image']

        def get_image_url(self,obj):
            request = self.context.get('request')
            image_url = obj.fingerprint.url
            return request.build_absolute_uri(image_url)
        
class IndustrySerializers(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(read_only =True)
    updated_at = serializers.DateTimeField(read_only =True)

    class Meta:
        model = Industry
        fields = ['id', 'name',  'icon', 'short_description', 'created_at', 'updated_at']

    def get_image_url(self,obj):
        request = self.context.get('request')
        image_url = obj.fingerprint.url
        return request.build_absolute_uri(image_url)
        #return request.build_absolute_url(obj.url)

class ProjectSerializers(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(read_only =True)
    updated_at = serializers.DateTimeField(read_only =True)

    class Meta:
        model = Projects
        fields = ['id','title','short_description','long_description','client_name','client_statement','client_picture','created_at','updated_at']
        #fields = '__all__'
        
    def get_client_picture_url(self,obj):
        request = self.context.get('request')
        image_url = obj.fingerprint.url
        return request.build_absolute_uri(image_url)

