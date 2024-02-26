from rest_framework import serializers
from . models import jobCategoryModel,jobCircularModel,jobApplicationModel

# write your serializer here
class jobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = jobCategoryModel
        fields = '__all__'

class jobCircularSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobCircularModel
        fields = '__all__'

class jobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobApplicationModel
        fields = '__all__'
