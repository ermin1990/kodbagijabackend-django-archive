from django.db import models

class Alergen(models.Model):
    id = models.AutoField(primary_key=True)
    nameBa = models.CharField(max_length=255)
    nameEng = models.CharField(max_length=255, null=True, blank=True)
    icon = models.ImageField(upload_to='icons/', null=True)

    def __str__(self):
        return self.nameBa

class Pancake(models.Model):
    id = models.AutoField(primary_key=True)
    nameBa = models.CharField(max_length=255)
    nameEng = models.CharField(max_length=255)
    dscBa = models.TextField()
    dscEng = models.TextField()
    image = models.ImageField(upload_to='pancakes/', null=True, blank=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    price = models.FloatField()
    alergens = models.ManyToManyField('Alergen', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}0 KM".format(self.nameBa, self.price)

class CreateYourOwn(models.Model):
    id = models.AutoField(primary_key=True)
    nameBa = models.CharField(max_length=255)
    nameEng = models.CharField(max_length=255)
    price = models.FloatField()
    alergens = models.ManyToManyField('Alergen', blank=True)
    active = models.BooleanField(default=True)

class Drink(models.Model):
    id = models.AutoField(primary_key=True)
    nameBa = models.CharField(max_length=255)
    nameEng = models.CharField(max_length=255)
    price = models.FloatField()
    active = models.BooleanField(default=True)

class FeaturedGame(models.Model):
    id = models.AutoField(primary_key=True)
    pancake = models.ForeignKey('Pancake', on_delete=models.CASCADE)
