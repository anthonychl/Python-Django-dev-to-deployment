from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete = models.DO_NOTHING) #first parameter is the model we are relating to, the second one is for what action do we want to take on deleting: this case nothing 
    title = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    zipcode = models.CharField(max_length = 20)
    description = models.TextField(blank = True) #we pass blank True, to make the field optional
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1) # it can be listed as 2 and a half bathrooms (2.5) for example, thats why its decimal and not integer
    garage = models.IntegerField(default=0) 
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1) # for example: 8.5 Acres
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/') #in django we set a folder for everything that is uploaded, this 'photos' folder will be created inside that media folder. %Y %m %d are subfolders according to the year, month and day of upload
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True) # make the other pics optional
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    is_published = models.BooleanField(default= True)
    list_date = models.DateTimeField(default= datetime.now, blank = True)

    def __str__(self):
        return self.title


