from rest_framework import serializers
from app.models.models import HeroSlider
from django.conf import settings

class HeroSliderSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = HeroSlider
        fields = "__all__" 
        

    def get_file_url(self, obj):
        if obj.file:
            return self.context['request'].build_absolute_uri('/' + obj.file)
        return None
