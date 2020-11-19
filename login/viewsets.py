from rest_framework import viewsets
from . import models
from . import serializers

class MyUserViewset(viewsets.ModelViewSet):
    queryset = models.MyUser.objects.all()
    serializer_class = serializers.MyUserSerializer