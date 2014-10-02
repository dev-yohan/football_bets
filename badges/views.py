from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from activities.models import Activity, ActivityByUser
from badges.models import Badge, BadgeByActivity, BadgeByUser

#Badges index
def index(request):

     if request.user.is_authenticated():

        user_badges = BadgeByUser.objects.filter(user=request.user).order_by('linking_date')

        context = {'badges':user_badges}
        return render(request, 'badges/index.html', context)

     else:
      
        return redirect('/')  
