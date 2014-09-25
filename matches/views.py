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
from django.db.models import F

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
    
    can_give_result = False 
    can_give_forecast = True
    
    total_forecasts = ResultForecast.objects.filter(match=match)
    home_trend = 0
    away_trend = 0
    draw_trend = 0
    total_forecasts_count = 0 

    if total_forecasts:
        total_forecasts_count = total_forecasts.count()

        for forecast in total_forecasts:
            
            if forecast.home_goals > forecast.away_goals:
                home_trend = home_trend + 1
            elif forecast.away_goals > forecast.home_goals:    
                away_trend = away_trend + 1
            elif forecast.away_goals == forecast.home_goals:
                draw_trend = draw_trend + 1
        
        home_trend = (home_trend * 100) / total_forecasts.count()
        away_trend = (away_trend * 100) / total_forecasts.count()
        draw_trend = (draw_trend * 100) / total_forecasts.count()

    
    return render(request, 'matches/detail.html', 
                  {'match': match, 
                   'matches': matches, 
                   'result_forecasts': result_forecasts,
                   'home_trend': home_trend,
                   'away_trend': away_trend,
                   'draw_trend': draw_trend,
                   'total_forecasts_count': total_forecasts_count,
                   'can_give_result': can_give_result,
                   'can_give_forecast': can_give_forecast,
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
          
          result_forecast = ResultForecast.objects.filter(user=request.user, match=match)
          print result_forecast
          
          if not result_forecast:
          
              ResultForecast.objects.create(home_goals=home_goals, 
                                        away_goals=away_goals,
                                        user=request.user,
                                        match=match,
                                        created_date=datetime.datetime.now())
              
              return redirect('matches:detail', match_id=match.id, match_slug=match.slug)
          
          else:
          
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
        return redirect('matches:detail', match_id=match.id, match_slug=match.slug, user=request.user)
    
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
      