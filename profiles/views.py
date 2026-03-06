from django.shortcuts import render, redirect
from .forms import ChangeProfile
from users.models import User
from django.contrib.auth.decorators import login_required

@login_required
def current_profile(request):
    return redirect(f'/profiles/{request.user.username}/')

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profiles/profile.html', {'current_user': user})

@login_required
def change_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ChangeProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(f'/profiles/{request.user.username}/')
    form = ChangeProfile(instance=request.user)
    return render(request, 'profiles/change_profile.html', {'form': form})