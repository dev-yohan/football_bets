from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from teams.models import Team

def index(request):

    team_list = Team.objects.all()[:5]
    context = {'team_list': team_list}
    return render(request, 'teams/index.html', context)

def detail(request, team_id):

    team = get_object_or_404(Team, pk=team_id)
    return render(request, 'teams/detail.html', {'team': team})