from rest_framework.viewsets import ModelViewSet
from .serializers import TweetSerializer
from .models import Tweet


class TweetViewSet(ModelViewSet):

    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()
