from django.db import models

class Person(models.Model):
  firstname=models.CharField(max_length=100)
  lastname=models.CharField(max_length=100)
  height=models.DecimalField(max_digits=10, decimal_places=5, null=True)
  weight=models.DecimalField(max_digits=10, decimal_places=5, null=True)

class Position(models.Model):
  description=models.CharField(max_length=100)

class Club(models.Model):
  name=models.CharField(max_length=100)
  coach=models.ForeignKey(Person, on_delete=models.CASCADE)
  dorm_latitude=models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
  dorm_longitude=models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)

class Play(models.Model):
  player=models.ForeignKey(Person, on_delete=models.CASCADE)
  team=models.ForeignKey(Club, on_delete=models.CASCADE)
  string_no=models.CharField(max_length=100)
  pos=models.ForeignKey(Position, on_delete=models.CASCADE)
  isActive=models.BooleanField(default=False, verbose_name="Zoning Fee")


