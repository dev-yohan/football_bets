import datetime
from django.template.context import RequestContext
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

# Create your views here.
from django.http import HttpResponse
from teams.models import Team, TeamPhoto
from matches.models import Match



def index(request):

    team_list = Team.objects.all()
    matches_list = Match.objects.filter(match_date__gte=datetime.datetime.today().date()).order_by('match_date')[:50]
    context = {'team_list': team_list, 'matches_list': matches_list, 'user': request.user}
    
    return render(request, 'teams/index.html', context)

def detail(request,  team_id, team_slug):

    team = get_object_or_404(Team,  pk=team_id)
    team_photos = TeamPhoto.objects.filter(team=team)[:20]
    matches = Match.objects.filter(Q(home=team) | Q(away=team), match_date__gte=datetime.datetime.today().date()).order_by('match_date')[:50]
    last_matches = Match.objects.filter(Q(home=team) | Q(away=team), match_date__lt=datetime.datetime.today().date()).order_by('match_date')[:5]
    return render(request, 'teams/detail.html', 
                  {'team': team,
                   'matches': matches, 
                   'photos': team_photos,
                   'last_matches': last_matches})

