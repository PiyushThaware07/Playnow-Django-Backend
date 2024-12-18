from django.urls import path,include
from rest_framework import routers
from . views import *

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"genres",viewset=GenreViewSet)
router.register(r"movies",viewset=MovieViewSet)

urlpatterns = [
    path("",include(router.urls)),
]

