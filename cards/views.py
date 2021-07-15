from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from cards.models import Card
from cards.serializers import CardSerializer


# ═══════════════ ModelViewSet ═══════════════
class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    pernission_classes = (IsAuthenticated)