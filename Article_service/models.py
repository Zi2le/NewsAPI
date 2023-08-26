from django.db import models
from django.conf import settings

# Create your models here.

class Continent(models.Model):
    continent = models.CharField(max_length=100, null='', blank='')

    def __str__(self):
        return self.continent
    
class Category(models.Model):
    category = models.CharField(max_length=100, null='', blank='')

    def __str__(self):
        return self.category
    

class Country(models.Model):
    country= models.CharField(max_length=100, null='', blank='')

    def __str__(self):
        return self.country
class Tag(models.Model):
    tag =  models.CharField(max_length=100, null='', blank='') 

    def __str__(self):
        return self.country 

class Post(models.Model):
    Headline = models.CharField(max_length=200)
    Description= models.CharField(max_length=200)
    Reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publication_Date = models.DateTimeField()
    url = models.URLField()
    thumbnail = models.ImageField(upload_to="thumbnail")
    content = models.TextField(max_length=300)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.Headline   