from . import models, serializers
from rest_framework import viewsets, decorators, status


class PicViewSet(viewsets.ModelViewSet):
    queryset = models.Picture.objects.all()
    serializer_class = serializers.PicSerializer
