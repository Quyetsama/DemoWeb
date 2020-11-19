from login.viewsets import MyUserViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('myuser/qcsama', MyUserViewset)