from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('rivers/', views.rivers_index, name='index'),
  path('rivers/<int:river_id>/', views.rivers_detail, name='detail'),
  path('rivers/create/', views.RiverCreate.as_view(), name='rivers_create'),
  path('rivers/<int:pk>/update/', views.RiverUpdate.as_view(), name='rivers_update'),
  path('rivers/<int:pk>/delete/', views.RiverDelete.as_view(), name='rivers_delete'),
  path('rivers/<int:river_id>/add_caughtFish', views.add_caughtFish, name='add_caughtFish'),
  path('rivers/<int:river_id>/assoc_lure/<int:lure_id>/', views.assoc_lure, name="assoc_lure"),
  path('rivers/<int:river_id>/unassoc_lure/<int:lure_id>/', views.unassoc_lure, name='unassoc_lure'),
  path('lures/', views.LureList.as_view(), name='lures_index'),
  path('lures/<int:pk>/', views.LureDetail.as_view(), name='lures_detail'),
  path('lures/create/', views.LureCreate.as_view(), name='lures_create'),
  path('lures/<int:pk>/update/', views.LureUpdate.as_view(), name='lures_update'),
  path('lures/<int:pk>/delete/', views.LureDelete.as_view(), name='lures_delete'),
]