import datetime

from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from matches.models import Match

#Matches index
def index(request):

    matches = Match.objects.filter(match_date__gte=datetime.datetime.today().date()).order_by('match_date')[:50]
    context = {'matches': matches}
    return render(request, 'matches/index.html', context)

#Match detail
def detail(request,  match_id, match_slug):

    match = get_object_or_404(Match,  pk=match_id)
    matches = Match.objects.filter(match_date__gte=datetime.datetime.today().date()).exclude(name=match.name).order_by('match_date')[:50]
    
    
    return render(request, 'matches/detail.html', {'match': match, 'matches': matches})