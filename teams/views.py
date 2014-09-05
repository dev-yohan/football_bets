import cloudinary
import cloudinary.uploader
import cloudinary.api

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from teams.models import Team
from matches.models import Match


def index(request):

    team_list = Team.objects.all()
    matches = Match.objects.order_by('match_date')[:50]
    context = {'team_list': team_list, 'matches': matches}
    return render(request, 'teams/index.html', context)

def detail(request,  team_id, team_slug):

    team = get_object_or_404(Team,  pk=team_id)
    return render(request, 'teams/detail.html', {'team': team})

