from django.shortcuts import render
from users.models import User
from django.contrib.auth.decorators import login_required

@login_required
def show_leaderboards(request):
    users = User.objects.filter(is_superuser=False).order_by('-points')[:10]
    return render(request, 'leaderboard/leaderboard.html', {'users': users})