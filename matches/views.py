import datetime
from forms import CrowdResultForm, ResultForecastForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from matches.models import Match, CrowdResult, ResultForecast
from django.db.models import Count
from django import forms

#Matches index
def index(request):

    matches = Match.objects.filter(match_date__gte=datetime.datetime.today().date()).order_by('match_date')[:50]
    context = {'matches': matches, 'user': request.user}
    return render(request, 'matches/index.html', context)

#Match detail
def detail(request,  match_id, match_slug):

    match = get_object_or_404(Match,  pk=match_id)
    matches = Match.objects.filter(match_date__gte=datetime.datetime.today().date()).exclude(name=match.name).order_by('match_date')[:50]
    result_forecasts = ResultForecast.objects.filter(match=match).order_by('-created_date')[:20]
    
    home_trend = ResultForecast.objects.filter(home_goals__gt=F('away_goals')).count()
    away_trend = ResultForecast.objects.filter(away_goals__gt=F('home_goals')).count()
    draw_trend = ResultForecast.objects.filter(away_goals=F('home_goals')).count()
    
    return render(request, 'matches/detail.html', 
                  {'match': match, 
                   'matches': matches, 
                   'result_forecasts': result_forecasts,
                   'home_trend'=home_trend,
                   'away_trend'=away_trend,
                   'draw_trend'=draw_trend,
                   'user': request.user})

#Match forecast new form
def create_match_forecast(request, match_id, match_slug):
    match = get_object_or_404(Match,  pk=match_id)
    matches = Match.objects.filter(match_date__gte=datetime.datetime.today().date()).exclude(name=match.name).order_by('match_date')[:50]
    
    if request.user.is_authenticated():
       
       form = ResultForecastForm(request.POST) 
       print form.errors
       if request.method == 'POST'  and form.is_valid():
       
          home_goals = form.cleaned_data['home_goals']
          away_goals = form.cleaned_data['away_goals']
          
          ResultForecast.objects.create(home_goals=home_goals, 
                                        away_goals=away_goals,
                                        user=request.user,
                                        match=match,
                                        created_date=datetime.datetime.now())
          return render(request, 'matches/create_match_forecast.html', 
                     {'match': match, 
                      'matches': matches,
                      'form': form, 
                      'user': request.user})
          
       else:
           
         form = ResultForecastForm()
            
         return render(request, 'matches/create_match_forecast.html', 
                     {'match': match, 
                      'matches': matches,
                      'form': form, 
                      'user': request.user})
    
    else:
        #messages.add_message(request, messages.INFO, 'Hello world.')
        return redirect('matches:detail', match_id=match.id, match_slug=match.slug)
    
#CrowdResult list
def crowd_result_list(request, match_id):
    match = get_object_or_404(Match,  pk=match_id)
    matches = Match.objects.filter(match_date__gte=datetime.datetime.today().date()).exclude(name=match.name).order_by('match_date')[:50]
    crowd_results = CrowdResult.objects.filter(match=match)
    
    return render(request, 'matches/crowd_result_list.html', 
                      {'match': match, 
                       'matches': matches,
                       'user': request.user,
                       'crowd_results': crowd_results})

#CrowdResult new form
def create_crowd_result(request, match_id):

    match = get_object_or_404(Match,  pk=match_id)
    matches = Match.objects.filter(match_date__gte=datetime.datetime.today().date()).exclude(name=match.name).order_by('match_date')[:50]
    
    if request.user.is_authenticated():
    
        if request.method == 'POST': # If the form has been submitted...
            # ContactForm was defined in the previous section
            form = CrowdResultForm(request.POST) # A form bound to the POST data
            #if form.is_valid(): # All validation rules pass
                # Process the data in form.cleaned_data
                # ...
            return redirect('matches:crowd_result_list', match_id=match.id) # Redirect after POST
        else:    
            
          form = CrowdResultForm()
            
          return render(request, 'matches/crowd_result.html', 
                      {'match': match, 
                       'matches': matches, 
                       'form': form,
                       'user': request.user})
    
    else:
        #messages.add_message(request, messages.INFO, 'Hello world.')
        return redirect('matches:detail', match_id=match.id, match_slug=match.slug)  
      