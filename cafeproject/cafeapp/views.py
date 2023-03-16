from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import team
def demo(request):
   obj = place.objects.all()
   objj = team.objects.all()
   return render(request, "index.html", {'result': obj,'objj':objj})


# Create your views here.
