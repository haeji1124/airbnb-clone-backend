from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TweetSerializer
from .models import Tweet


@api_view(["GET"])
def tweets_by_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise NotFound
    tweets = Tweet.objects.filter(user=user)
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)
