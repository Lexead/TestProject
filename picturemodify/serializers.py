from rest_framework import serializers
from rest_framework.response import Response
from .models import Picture
import hashlib
from PIL import Image


class PicSerializer(serializers.HyperlinkedModelSerializer, serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Picture
        fields = ('url', 'image', 'image_url', 'width', 'height')
        extra_kwargs = {
            'image': {'write_only': True},
            'width': {'write_only': True},
            'height': {'write_only': True},
            'image_url': {'read_only': True}
        }

    def get_image_url(self, obj):
        request = self.context.get("request")
        image = Image.open(obj.image.path)
        url = f"{hashlib.md5(image.filename.encode()).hexdigest()}_{image.width}x{image.height}.{image.format}"
        return request.build_absolute_uri(url)
