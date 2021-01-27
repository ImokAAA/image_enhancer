from django.db import models

class Image(models.Model):
    """ This model keeps all images of users before enhancing """  
    
    name      = models.CharField(max_length=50) 
    image     = models.ImageField(upload_to='images/')

 
