from rest_framework.serializers import ModelSerializer
from taxi.models import AppUser


class AppUserSerializer(ModelSerializer):
    class Meta:
        model = AppUser
        fields = ["id","username", "phone_no", "location"]