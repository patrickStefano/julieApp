from django.db import models

class Categories(models.Model):
  name = models.CharField(max_length=100, null=False, blank=False)

  def __str__(self):
    return self.name
  
class Photo(models.Model):
  categories = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True) # this is to set the relationship
  image = models.ImageField(null=False, blank=False)
  desciption = models.TextField()
  def __strr__(self):
    return self.desciption

