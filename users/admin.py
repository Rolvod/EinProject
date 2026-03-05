from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class ShedevroAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('description', 'profile_picture', 'points', 'completed_quizzes', 'nickname')}),)

admin.site.register(User, ShedevroAdmin)