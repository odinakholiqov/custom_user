from django.urls import path
from .views import *


urlpatterns = [
    path("", ListCreateUser.as_view()),
    path("groups/", ListCreateGroup.as_view())
]