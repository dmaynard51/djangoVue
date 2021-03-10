from django.urls import path
from students import views
from rest_framework import routers
from students.views import *
from django.conf.urls import include


router = routers.DefaultRouter()
router.register('students', StudentsViewSet)

urlpatterns = [
    path('', include(router.urls))
    ]