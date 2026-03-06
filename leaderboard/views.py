from django.shortcuts import render
from users.models import User

def show_leaderboards(request):
    users = User.objects.order_by('-points')[:10]
    return render(request, 'leaderboard/leaderboard.html', {'users': users})