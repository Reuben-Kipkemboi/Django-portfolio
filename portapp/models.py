from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    
    def __str__(self):
        return self.first_name
    #the str is just a basic way that helps if we want to have a view of anything that we would like to query
    
    
    
    
    
class Project(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

