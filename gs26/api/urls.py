#Link to test the API (http://127.0.0.1:8000/stucreate/) + we have to write username and password in Authorization section in POSTMAN for Authenticated users

from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

#Creating Router Object
router=DefaultRouter()

#Register StudentViewSet with Router
router.register('stucreate', views.StudentModelViewSet, basename='student') #(IP/stucreste/) is our path to run this API
#We can write anything in the place of //student//, //router//, //stucreate//

urlpatterns = [
    path('',include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')), #For Login button in UI
]