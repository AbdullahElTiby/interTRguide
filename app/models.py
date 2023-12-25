from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    city = models.ForeignKey(City, related_name='items', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    googlemapslink = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="photos", blank=True, null=True)


    def __str__(self):
        return self.name
    
    
class Pagesections(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    Item = models.ForeignKey(Item, related_name='itemss', on_delete=models.CASCADE)
    titlename = models.TextField(blank=True, null=True) 
    description =  models.TextField(blank=True, null=True)
    audio = models.FileField(upload_to="audio", blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
    



class Sv(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="photos", blank=True, null=True)
    
    title1 = models.CharField(null=True, blank=True, max_length=255)
    step1 = models.TextField(null=True, blank=True)
    title2 = models.CharField(null=True, blank=True, max_length=255)
    step2 = models.TextField(null=True, blank=True)
    title3 = models.CharField(null=True, blank=True, max_length=255)
    step3 = models.TextField(null=True, blank=True)
    title4 = models.CharField(null=True, blank=True, max_length=255)
    step4 = models.TextField(null=True, blank=True)
    title5 = models.CharField(null=True, blank=True, max_length=255)
    step5 = models.TextField(null=True, blank=True)
    title6 = models.CharField(null=True, blank=True, max_length=255)
    step6 = models.TextField(null=True, blank=True)
    title7 = models.CharField(null=True, blank=True, max_length=255)
    step7 = models.TextField(null=True, blank=True)
    title8 = models.CharField(null=True, blank=True, max_length=255)
    step8 = models.TextField(null=True, blank=True)
    title9 = models.CharField(null=True, blank=True, max_length=255)
    step9 = models.TextField(null=True, blank=True)
    title10 = models.CharField(null=True, blank=True, max_length=255)
    step10 = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
