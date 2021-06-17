from django.db import models


# Create your models here.

class customer(models.Model):
    name=models.CharField(max_length=50)
    emailid=models.EmailField()
    balance=models.IntegerField(max_length=50)


    def __str__(self):
        return self.name

class history(models.Model):
    sender=models.CharField(max_length=50)
    receiver=models.CharField(max_length=50)
    transfer=models.IntegerField(max_length=50)
    date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.sender +" --- "+ self.receiver 