from django.contrib import admin
from .models import Exercise, UserExerciseLog, User
from django.contrib.auth import get_user_model

# Register your models here.
User = get_user_model()


admin.site.register(Exercise)
admin.site.register(User)
admin.site.register(UserExerciseLog)
