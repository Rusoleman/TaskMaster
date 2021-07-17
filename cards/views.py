from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from cards.models import Card
from cards.serializers import CardSerializer

from cards.tasks import deadline_mail
from datetime import timedelta, datetime


# ═══════════════ ModelViewSet ═══════════════
class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    # ═══════════════ Asynchronous Actions ═══════════════
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serialized = serializer(data=request.data)
        if not serialized.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)
        deadline_mail.apply_async(
                args=[request.user.email],
                eta=datetime.now() + timedelta(days=3)
        )
        serialized.save()
        return Response(status=status.HTTP_200_OK, data=serialized.data)