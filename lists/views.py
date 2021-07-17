from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from lists.models import List
from lists.serializers import ListSerializer


# ═══════════════ ModelViewSet ═══════════════
class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]