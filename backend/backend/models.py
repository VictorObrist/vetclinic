from django.db import models

class Clients(models.Model):
    ic_number = models.IntegerField()
    first_name = models.CharField()
    last_name = models.CharField()
    phone_number = models.CharField()

class Vertebrate(models.Model):
    name = models.CharField()
    description = models.CharField()

class Family(models.Model):
    name = models.CharField()
    description = models.CharField()
    id_vertebrate = models.ForeignKey(Vertebrate, on_delete=models.CASCADE)

class Breeds(models.Model):
    name = models.CharField()
    description = models.CharField()
    id_family = models.ForeignKey(Family, on_delete=models.CASCADE)

class Mascots(models.Model):
    name = models.CharField()
    owner = models.ForeignKey(Clients, on_delete=models.CASCADE)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    breed = models.ForeignKey(Breeds, on_delete=models.CASCADE)

class Services(models.Model):
    name = models.CharField()
    description = models.CharField()

class Events(models.Model):
    mascot = models.ForeignKey(Mascots)
    date = models.DateTimeField()
    service = models.ForeignKey(Services)
    observations = models.CharField()
