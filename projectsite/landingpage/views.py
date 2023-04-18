from django.shortcuts import render, redirect

from baseball.models import Person, Club, Play, Position

def index(request):
  persons_count=Person.objects.all().count()
  clubs_count=Club.objects.all().count()
  plays_count=Play.objects.all().count()
  positions_count=Position.objects.all().count()

  context={
    "persons_count": persons_count,
    "clubs_count": clubs_count,
    "plays_count": plays_count,
    "positions_count": positions_count
  }

  return render(request, "index.html", context )


def showPersons(request):
  persons=Person.objects.all()
  context={ "persons": persons }
  return render(request, "persons.html", context )
  

def addPerson(request):
  if request.method == 'POST':
    firstname=request.POST.get("firstname")
    lastname=request.POST.get("lastname")
    height=float(request.POST.get("height"))
    weight=float(request.POST.get("weight"))

    person=Person(firstname=firstname, lastname=lastname,height=height, weight=weight)
    person.save()

  return redirect("/persons")

def removePerson(request):
  if request.method=="POST":
    person_id=int(request.POST.get("person_id"))
    person=Person.objects.get(id=person_id)
    person.delete()

  return redirect("/persons")

def updatePerson(request):
  if request.method=="POST":
    person_id=int(request.POST.get("person_id"))
    firstname=request.POST.get("firstname")
    lastname=request.POST.get("lastname")
    height=float(request.POST.get("height"))
    weight=float(request.POST.get("weight"))

    person=Person.objects.get(id=person_id)
    person.firstname=firstname
    person.lastname=lastname
    person.height=height
    person.weight=weight

    person.save()

  return redirect("/persons")

def showPositions(request):
  positions=Position.objects.all()
  return render(request, "positions.html", {"positions": positions} )

def addPosition(request):
  if request.method == 'POST':
    description=request.POST.get("description")
    position=Position(description=description )
    position.save()

  return redirect("/positions")

def removePosition(request):
  if request.method=="POST":
    print(request.POST)
    position_id= int(request.POST.get("position_id"))
    position=Position.objects.get(id=position_id)
    position.delete()

  return redirect("/positions")

def updatePosition(request):
  if request.method=="POST":
    position_id=int(request.POST.get("position_id"))
    description=request.POST.get("description")

    position=Position.objects.get(id=position_id)
    position.description=description

    position.save()

  return redirect("/positions")


def showClubs(request):
  clubs=Club.objects.all()
  persons=Person.objects.all()

  if request.method=="GET":
    update_club=request.GET.get("update_club", False)

    if update_club:
      club_id=int(request.GET.get("club_id"))
      club=Club.objects.get(id=club_id)

      return render(request, "clubs.html", {"clubs": clubs, "persons": persons, "club": club, "updating_club":update_club} )
  
    return render(request, "clubs.html", {"clubs": clubs, "persons": persons, "club": {}, "updating_club":False} )


def addClub(request):
  if request.method == 'POST':
    club_name=request.POST.get("club_name")
    club_coach=request.POST.get("club_coach")
    latitude=float(request.POST.get("latitude"))
    longitude=float(request.POST.get("longitude"))

    coach=Person.objects.get(id=club_coach)

    club=Club(name=club_name, coach=coach, dorm_latitude=latitude, dorm_longitude=longitude)
    club.save()

  return redirect("/clubs")

def removeClub(request):
  if request.method=="POST":
    club_id= int(request.POST.get("club_id"))
    club=Club.objects.get(id=club_id)
    club.delete()

  return redirect("/clubs")

def updateClub(request):
  return redirect("/clubs")


def showPlays(request):
  return render(request, "plays.html", {} )