from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader


def Trading_strategy(request):
    #ConAH = Vimo.published.all()
    context ={}
    return render(request, 'chienluocgiaodich.html',context)
    

"""
def index(request):
    context = {}
    template = loader.get_template('chienluocgiaodich.html')
    return HttpResponse(template.render(context, request))
    
"""