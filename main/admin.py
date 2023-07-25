from django.contrib import admin
from .models import Subscription, Post, Digest, CustomUser

admin.site.register(Subscription)
admin.site.register(Post)
admin.site.register(Digest)
admin.site.register(CustomUser)
