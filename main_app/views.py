from dataclasses import fields
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import River, Lure
from .forms import caughtForm

# Create your views here.

# Add the Cat class & list and view function below the imports


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def rivers_index(request):
  rivers = River.objects.all()
  return render(request, 'rivers/index.html', { 'rivers': rivers })

def rivers_detail(request, river_id):
  river = River.objects.get(id=river_id)
  id_list = river.lures.all().values_list('id')
  lures_river_doesnt_have = Lure.objects.exclude(river=id_list)
  caught_form = caughtForm()
  return render(request, 'rivers/detail.html', { 
    'river': river,'caught_form': caught_form, 
    'lures': lures_river_doesnt_have
    })

class RiverCreate(CreateView):
  model = River
  fields = '__all__'

class RiverUpdate(UpdateView):
  model = River
  fields = ['description', 'fish']

class RiverDelete(DeleteView):
  model = River
  success_url = '/rivers/'

def add_caughtFish(request, river_id):
  form = caughtForm(request.POST)
  if form.is_valid():
    new_caughtFish = form.save(commit=False)
    new_caughtFish.river_id = river_id
    new_caughtFish.save()
  return redirect('detail', river_id=river_id)

def assoc_lure(request, river_id, lure_id):
  River.objects.get(id=river_id).lures.add(lure_id)
  return redirect('detail', river_id=river_id)

def unassoc_lure(request, river_id, lure_id):
  River.objects.get(id=river_id).lures.remove(lure_id)
  return redirect('detail', river_id=river_id)

class LureList(ListView):
  model = Lure 

class LureDetail(DetailView):
  model = Lure

class LureCreate(CreateView):
  model = Lure
  fields = '__all__'

class LureUpdate(UpdateView):
  model = Lure
  fields = ['name', 'size']

class LureDelete(DeleteView):
  model = Lure
  success_url = '/lures/'