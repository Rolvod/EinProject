from django.shortcuts import render, redirect
from users.models import User

def current_profile(request):
    return redirect(f'/profiles/{request.user.username}/')

def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profiles/profile.html', {'current_user': user})