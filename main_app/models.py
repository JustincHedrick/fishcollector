from django.db import models
from django.urls import reverse

FISH = (
  ('BC', 'Black Crappie'),
  ('BG', 'Bluegill'),
  ('BH', 'Bullhead'),
  ('BT', 'Bull Trout'),
  ('BR', 'Brown Trout'),
  ('CC', 'Channel Catfish'),
  ('CT', 'Cutthroat Trout'),
  ('DV', 'Dolly Varden'),
  ('EB', 'Eastern Brook Trout'),
  ('GC', 'Grass Carp'),
  ('GR', 'Green Sunfish'),
  ('GS', 'Green Sturgeon'),
  ('KK', 'Kokanee'),
  ('LB', 'Largemouth Bass'),
  ('RB', 'Rock Bass'),
  ('RT', 'Rainbow Trout'),
  ('SB', 'Smallmouth Bass'),
  ('SH', 'Steelhead'),
  ('TM', 'Tiger Muskie'),
  ('WE', 'Walleye'),
  ('WS', 'White Sturgeon'),
  ('YP', 'Yellow Perch'),
)

class Lure(models.Model):
  name = models.CharField(max_length=50)
  size = models.PositiveIntegerField(default=0)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('lures_detail', kwargs={'pk': self.id})




# Create your models here.
class River(models.Model):
  name = models.CharField(max_length=100)
  creeks = models.CharField(max_length=200)
  state = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  fish = models.TextField(max_length=100)
  lures = models.ManyToManyField(Lure)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'river_id': self.id})

class caughtFish(models.Model):
  date = models.DateField('caught date')
  fish = models.CharField(
    max_length=2,
    choices=FISH,
    default=FISH[0][0]
    )

  river = models.ForeignKey(River, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.get_fish_display()} on {self.date}'