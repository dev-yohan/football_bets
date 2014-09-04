from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from teams.models import League

#leagues index
def index(request):

    leagues_list = League.objects.all()
    context = {'leagues_list': leagues_list}
    return render(request, 'leagues/index.html', context)

#League detail
def detail(request, league_id, league_slug):

    team = get_object_or_404(League,  pk=league_id)
    return render(request, 'leagues/detail.html', {'league': league})