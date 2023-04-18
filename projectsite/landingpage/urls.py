from django.urls import path
from . import views

urlpatterns=[
  path("", views.index, name="index"),
  path("persons", views.showPersons, name="persons"),
  path("persons/add", views.addPerson, name="add_person"),
  path("persons/remove", views.removePerson, name="remove_person"),
  path("persons/update", views.updatePerson, name="update_person"),
  path("positions", views.showPositions, name="positions"),
  path("positions/add", views.addPosition, name="add_positions"),
  path("positions/update", views.updatePosition, name="update_positions"),
  path("positions/remove", views.removePosition, name="remove_positions"),
  path("clubs", views.showClubs, name="clubs"),
  path("clubs/add", views.addClub, name="add_clubs"),
  path("clubs/update", views.updateClub, name="update_clubs"),
  path("clubs/remove", views.removeClub, name="remove_clubs"),
  path("plays", views.showPlays, name="plays"),
]