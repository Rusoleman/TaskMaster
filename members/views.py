from members.models import Member
from members.serializers import MembersSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.

class MeberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MembersSerializer
    permission_classes = (AllowAny, )
