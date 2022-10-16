from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from admins.models import Department

class UserAccountManager(BaseUserManager):
  def create_user(self,username,email,userid=None ,phone_number =None, role=None,department=None,Created_by=None, password=None):
    if not email:
      raise ValueError('Users must have an email address')
    if not username:
      raise ValueError("User must have an username")

    email = self.normalize_email(email)
    email = email.lower()

    user = self.model(
      username     =   username,
      userid=userid,
      phone_number=phone_number,
      email=email,
      role=role,
      department=department,
      Created_by=Created_by
    )

    user.set_password(password)
    user.save(using=self._db)

    return user
  
  def create_superuser(self,username , email, password=None):
    user = self.create_user(
      username = username ,
      email =email,
      password=password,
    )

    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)

    return user


class UserAccount(AbstractBaseUser, PermissionsMixin):

   
    username =   models.CharField(max_length=50 , unique=True)
    userid = models.CharField(max_length = 500 ,null = True)
    email = models.EmailField(unique=True, max_length=255)
    phone_number =   models.CharField(max_length=50, unique=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    Created_by =  models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE ,null =True )
    created_at = models.DateTimeField(auto_now_add=True,null =True)
    updated_at = models.DateTimeField(auto_now=True,null =True)
    department = models.ForeignKey(Department,on_delete=models.PROTECT,null =True )
    role = models.CharField(max_length=255 , null =True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','phone_number']

    def __str__(self):
        return self.email




