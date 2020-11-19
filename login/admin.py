from django.contrib import admin
# from .models import UserProfile
from .models import MyUser, Post, HistoryModel


admin.site.register(MyUser)
admin.site.register(Post)
admin.site.register(HistoryModel)
# admin.site.register(UserProfile)
