from django.shortcuts import render, redirect
from .forms import ArticleForm
from django.forms import formset_factory
from .mypath import searchx, searchy, time
import json
# Create your views here.

def index(request):
    if request.method == 'POST':
        people = request.POST.get('people')     
        return redirect('pages:search', people)    
    return render(request, 'pages/index.html')



def search(request, people):    
    if request.method == 'POST':        
        adlist = []        
        for i in range(people):
            adlist.append((searchx(request.POST.get(f'form-{i}-Address')), searchy(request.POST.get(f'form-{i}-Address'))))
        result, position = time(adlist)
        print(position)
        place = json.dumps(position)
        print(place)
        context = {
            'result': result,
            'place' : place,
            'place_name' : adlist,
            'counts' : people,
            # 'arrive_time': arrive_time,
        }
        return render(request, 'pages/map_result.html', context)           
    
    else:
        ArticleFormSet = formset_factory(ArticleForm, extra=people)        
        formset = ArticleFormSet()    
    context = {
        'formset': formset,
    }
    return render(request, 'pages/search.html', context)