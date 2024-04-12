from django.db import models

# Create your models here.
# Creating database in django 


#### New way of database created in django using class######
class Contact(models.Model):
    name=models.CharField(max_length=122)# This are attributes of table
    email=models.CharField(max_length=122)# seperate email field is also present
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
    
    
    # This function is used to define the name of record in database using name of any attribute provided (eg. name)
    def __str__(self):
        return self.name
    
### register the model in admin file
    
## In terminal makemigration will riun to create a table and wanted to perfom changes in database


#### makemigrations - create changes and store it in file

####migrate - applypending changes made by makemigrations