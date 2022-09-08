from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

# Create your views here


#Here we are using //IsAuthenticatedOrReadOnly// permission i.e no 4!!
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle, UserRateThrottle]



#Ways to generate TOKEN--

#1)Using Admin Application
#2)Using Django manage.py command
# -->(python manage.py drf_create_token <username>)
#3)By exposing an API endpoint
#4)Using Signals


#Types of permissions Classes--

#1)AllowAny (Always available BYDEFAULT)
#2)IsAuthenticated
#3)IsAdminUser
#4)IsAuthenticatedOrReadOnly
#5)DjangoModelPermissions
#6)DjangoModelPermissionsOrAnonReadOnly
#7)DjangoObjectPermissions
#8)CustomPermissions


#Types of Authentication--

#1)BasicAuthentication
#2)SessionAuthentication
#3)TokenAuthentication
#4)RemoteUserAuthentication
#5)CustomAuthentication