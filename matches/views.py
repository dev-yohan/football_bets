import datetime
from forms import CrowdResultForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from matches.models import Match

#Matches index
def index(request):

    matches = Match.objects.filter(match_date__gte=datetime.datetime.today().date()).order_by('match_date')[:50]
    context = {'matches': matches, 'user': request.user}
    return render(request, 'matches/index.html', context)

#Match detail
def detail(request,  match_id, match_slug):

    match = get_object_or_404(Match,  pk=match_id)
    matches = Match.objects.filter(match_date__gte=datetime.datetime.today().date()).exclude(name=match.name).order_by('match_date')[:50]
    
    
    return render(request, 'matches/detail.html', {'match': match, 'matches': matches, 'user': request.user})


#CrowdResult new form
def create_crowd_result(request, match_id):
    form = CrowdResultForm()
    match = get_object_or_404(Match,  pk=match_id)
    matches = Match.objects.filter(match_date__gte=datetime.datetime.today().date()).exclude(name=match.name).order_by('match_date')[:50]
    
    if request.user.is_authenticated():
        
      return render(request, 'matches/crowd_result.html', 
                  {'match': match, 
                   'matches': matches, 
                   'form': form,
                   'user': request.user})
    
    else:
        messages.error(request, 'Debes iniciar sesi&oacute;n.')
        return redirect('matches:detail', match_id=match.id, match_slug=match.slug)  
      