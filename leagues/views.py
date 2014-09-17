import datetime

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from leagues.models import League
from leagues.models import Season
from leagues.models import SeasonStatus
from matches.models import Match

#leagues index
def index(request):

    leagues_list = League.objects.all()
    matches = Match.objects.filter(match_date__gte=datetime.datetime.today().date()).order_by('match_date')[:50]
    context = {'leagues_list': leagues_list, 'matches': matches}
    return render(request, 'leagues/index.html', context)

#League detail
def detail(request, league_id, league_slug):

    league = get_object_or_404(League,  pk=league_id)
    matches = Match.objects.filter(match_date__gte=datetime.datetime.today().date(), league = league).order_by('match_date')[:50]
    
    if Season.objects.filter(league=league):
      current_season = Season.objects.filter(league=league).order_by('-initial_date')[0]
      season_status = SeasonStatus.objects.filter(current_season=current_season).order_by('-points','-goals_difference','-goals_for')
    else:
      current_season = None
      season_status = None  
    
    return render(request, 'leagues/detail.html', 
                  {'league': league, 
                   'matches': matches, 
                   'current_season': current_season, 
                   'season_status': season_status})