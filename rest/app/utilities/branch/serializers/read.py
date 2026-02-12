from rest_framework import serializers
from app.models.models import Branches, BranchPhone

class BranchPhoneReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchPhone
        fields = ["id", "phone"]


class BranchesReadSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    phones = serializers.SerializerMethodField()
    
    class Meta:
        model = Branches
        fields = [
            "id", "name", "location", "image", "image_url", "area", "city", 
            "district", "open", "time", "latitude", "longitude", "phones"
        ]
    
    def get_image_url(self, obj):
        if obj.image:
            file_path = obj.image.replace('media/', '').replace('branches/', '')
            return f'/media/branches/{file_path}'
        return None
    
    def get_phones(self, obj):
        phones = []
        for phone in obj.branchphone_set.all():
            phones.append({
                "id": phone.id,
                "phone": phone.phone
            })
        return phones