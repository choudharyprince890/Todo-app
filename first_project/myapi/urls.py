from django.urls import include, path
from rest_framework import routers
from . import views

from myapi.views import *

# router = routers.DefaultRouter()
# router.register(r'task', TaskViewSet)

urlpatterns = [
    # path('api/', include(router.urls)),
    path('create/',views.createTask),
    path('task/',views.taskDetail),
    path('del/<str:pk>',views.deleteTask)
    # path('task/<str:pk>/',views.taskDetail)
]