import datetime

from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

# Create your views here.
from django.http import HttpResponse
from teams.models import Team
from matches.models import Match


def index(request):

    team_list = Team.objects.all()
    matches_list = Match.objects.filter(match_date__gte=datetime.datetime.today().date()).order_by('match_date')[:50]
    context = {'team_list': team_list, 'matches_list': matches_list}
    return render(request, 'teams/index.html', context)

def detail(request,  team_id, team_slug):

    team = get_object_or_404(Team,  pk=team_id)
    matches = Match.objects.filter(Q(home=team) | Q(away=team), match_date__gte=datetime.datetime.today().date()).order_by('match_date')[:50]
    return render(request, 'teams/detail.html', {'team': team,'matches': matches})

