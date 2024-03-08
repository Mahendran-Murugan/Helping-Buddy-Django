from django.db import models

# Create your models here.

class Room(models.Model):
    # host = 
    # topic = 
    name = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    # participants =
    updated = models.DateTimeField(auto_now = True) #take snapshot of time when modified
    created = models.DateTimeField(auto_now_add = True) #take snapshot of time when created
    
    def __str__(self):
        return self.name