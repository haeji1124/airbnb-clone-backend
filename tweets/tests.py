from rest_framework.test import APITestCase
from . import models
from users.models import User


class TestTweets(APITestCase):
    TWEET_AUTHOR = "testuser"
    TWEET_PAYLOAD = "test all tweet"
    URL = "/api/v1/tweets/"

    def setUp(self):
        self.user = User.objects.create(username=self.TWEET_AUTHOR, password="test1234")
        self.client.force_authenticate(user=self.user)
        self.tweet = models.Tweet.objects.create(
            payload=self.TWEET_PAYLOAD, user=self.user
        )

    def test_all_tweets(self):
        response = self.client.get(self.URL)
        data = response.json()
        self.assertEqual(data[0]["user"].get("username"), self.user.username)
        self.assertEqual(data[0]["payload"], self.TWEET_PAYLOAD)

    def test_create_tweet(self):
        payload = "new tweet"
        response = self.client.post(self.URL, {"payload": payload})
        data = response.json()
        self.assertEqual(data["user"].get("username"), self.user.username)
        self.assertEqual(data["payload"], payload)


class TestTweetDetail(APITestCase):
    TWEET_AUTHOR = "testuser"
    TWEET_PAYLOAD = "test one tweet"
    BASE_URL = "/api/v1/tweets/"

    def setUp(self):
        self.user = User.objects.create(username=self.TWEET_AUTHOR, password="test1234")
        self.client.force_authenticate(user=self.user)
        self.tweet = models.Tweet.objects.create(
            payload=self.TWEET_PAYLOAD, user=self.user
        )
        self.url = f"{self.BASE_URL}{self.tweet.pk}"

    def test_get_tweet(self):
        response = self.client.get(self.url)
        data = response.json()
        self.assertEqual(data["user"].get("username"), self.user.username)
        self.assertEqual(data["payload"], self.TWEET_PAYLOAD)

    def test_update_tweet(self):
        payload = "updated tweet"
        response = self.client.put(self.url, {"payload": payload})
        data = response.json()
        self.assertEqual(data["user"].get("username"), self.user.username)
        self.assertEqual(data["payload"], payload)

    def test_delete_tweet(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(models.Tweet.objects.count(), 0)
