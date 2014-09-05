from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from teams.models import League
from matches.models import Match

#leagues index
def index(request):

    leagues_list = League.objects.all()
    matches = Match.objects.order_by('match_date')[:50]
    context = {'leagues_list': leagues_list, 'matches': matches}
    return render(request, 'leagues/index.html', context)

#League detail
def detail(request, league_id, league_slug):

    league = get_object_or_404(League,  pk=league_id)
    return render(request, 'leagues/detail.html', {'league': league})