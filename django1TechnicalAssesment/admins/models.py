from django.db import models
# from authentication.models import UserAccount
from django.conf import settings

# from django1TechnicalAssesment.authentication.models import UserAccount

# Create your models here.


class Department(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    Created_by =  models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null =True, related_name='+' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


