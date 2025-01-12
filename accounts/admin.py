from django.contrib import admin
from .models import CustomUser, Profile,Post, Friendship, Message

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Friendship)
admin.site.register(Message)