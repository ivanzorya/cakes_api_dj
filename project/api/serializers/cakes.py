from rest_framework import serializers

from cakes.models import Cake


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = ("id", "name", "comment", "image_url", "yum_factor")
        read_only_fields = ("id",)
