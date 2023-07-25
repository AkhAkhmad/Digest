from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from .models import CustomUser, Digest
from .serializers import UserSerializer, DigestSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class DigestViewSet(viewsets.ModelViewSet):
    queryset = Digest.objects.all()
    serializer_class = DigestSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_id = request.user.id
        else:
            return HttpResponse("Пользователь не залогинен")

        try:
            user = CustomUser.objects.get(pk=user_id)
        except Exception as e:
            print(e)

        subscriptions = user.subscription_set.all()
        posts = []

        for subscription in subscriptions:
            posts.extend(subscription.post_set.all())

        popular_posts = [post for post in posts if post.top > 10]
        title = request.data.get('title')
        digest = Digest.objects.create(user=user)
        digest.posts.set(popular_posts)
        digest.title = title
        digest.save()
        serializer = DigestSerializer(digest)
        return Response(serializer.data)
