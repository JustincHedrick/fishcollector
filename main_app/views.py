from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import River, Lure
from .forms import caughtForm

# Create your views here.

# Add the Cat class & list and view function below the imports


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def rivers_index(request):
  rivers = River.objects.filter(user=request.user)
  return render(request, 'rivers/index.html', { 'rivers': rivers })

@login_required
def rivers_detail(request, river_id):
  river = River.objects.get(id=river_id)
  id_list = river.lures.all().values_list('id')
  lures_river_doesnt_have = Lure.objects.exclude(id__in=id_list)
  caught_form = caughtForm()
  return render(request, 'rivers/detail.html', { 
    'river': river,'caught_form': caught_form, 
    'lures': lures_river_doesnt_have
    })


class RiverCreate(LoginRequiredMixin, CreateView):
  model = River
  fields = ['name', 'creeks', 'state', 'description', 'fish']

  def form_valid(self, form):
    # assign the logged in users id
    # for.instance is the new river instance (unsaved)
    form.instance.user = self.request.user
    # let createviews form_valid do its thing
    return super().form_valid(form)

class RiverUpdate(LoginRequiredMixin, UpdateView):
  model = River
  fields = ['description', 'fish']

class RiverDelete(LoginRequiredMixin, DeleteView):
  model = River
  success_url = '/rivers/'

@login_required
def add_caughtFish(request, river_id):
  form = caughtForm(request.POST)
  if form.is_valid():
    new_caughtFish = form.save(commit=False)
    new_caughtFish.river_id = river_id
    new_caughtFish.save()
  return redirect('detail', river_id=river_id)

@login_required
def assoc_lure(request, river_id, lure_id):
  River.objects.get(id=river_id).lures.add(lure_id)
  return redirect('detail', river_id=river_id)

@login_required
def unassoc_lure(request, river_id, lure_id):
  River.objects.get(id=river_id).lures.remove(lure_id)
  return redirect('detail', river_id=river_id)

class LureList(LoginRequiredMixin, ListView):
  model = Lure 

class LureDetail(LoginRequiredMixin, DetailView):
  model = Lure

class LureCreate(LoginRequiredMixin, CreateView):
  model = Lure
  fields = '__all__'

class LureUpdate(LoginRequiredMixin, UpdateView):
  model = Lure
  fields = ['name', 'size']

class LureDelete(LoginRequiredMixin, DeleteView):
  model = Lure
  success_url = '/lures/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # this is how to create a 'user' from object that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # this will add the user to the database
      user = form.save()
      # this is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # a bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)