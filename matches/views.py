# Create your views here.
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from matches.models import Match

#leagues index
def index(request):

    matches = Match.objects.order_by('match_date')[:50]
    context = {'matches': matches}
    return render(request, 'matches/index.html', context)