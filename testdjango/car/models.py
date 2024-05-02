from django.db import models

# Create your models here.

class Owner(models.Model):

    oid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    gender = models.IntegerField(choices=[(1, "Male"),(2, "Female")])
    def __str__(self):
        return self.name
class Car(models.Model):

    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    type = models.IntegerField(choices=[(1, "Truck"),(2, "Sedan")])
    active = models.BooleanField(default=True)
    address= models.CharField(max_length=500)
    age = models.IntegerField()
    issuedate = models.DateField(auto_now=True)
    email= models.EmailField()
    url= models.URLField()
    owner= models.ForeignKey(Owner, on_delete=models.CASCADE, default=0, related_name="car_owner")
    def __str__(self):
        return self.name


