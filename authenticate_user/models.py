from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Course(models.Model):
    image = models.ImageField(upload_to='course/',null=True,blank=True)
    course_name = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=False,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.course_name


class UserManager(BaseUserManager):

    def create_users(self,username,email,first_name,last_name,password):
        user = self.create_user(
            username=username,
            password=password
        )
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.set_password(password)
        user.is_active=False
        user.save(using=self._db)
        return user
    
    def create_user(self,username,password):
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,password):
        user = self.create_user(username=username,password=password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Addres(models.Model):
    address = models.TextField()
    city = models.CharField(max_length = 150)
    state = models.CharField(max_length = 150)
    zip = models.CharField(max_length = 150)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'User Addres'


class User(AbstractUser,PermissionsMixin):
    profile_pic = models.ImageField(upload_to='profile/',null=True,blank=True)
    username = models.CharField(_('username'),max_length=150,unique=True)
    email = models.EmailField(null=True,blank=True)
    course = models.OneToOneField(Course, on_delete=models.CASCADE,null=True,blank=True)
    
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    address = models.ForeignKey(Addres,on_delete=models.CASCADE,null=True,blank=True)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.username

    def save(self,*agrs,**kwagrs):
        super(User,self).save(*agrs,**kwagrs)
        


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='resume')
    resume = models.FileField(upload_to='resume/',null=True,blank=True)
    
    def __str__(self):
        return self.user.username
    


class Subscriber(models.Model):
    subscribe = models.EmailField(max_length=150)

    def __str__(self):
        return self.subscribe
    

class ContactDetails(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField(max_length = 150)
    subject = models.CharField(max_length = 150)
    message = models.TextField()
    contact = models.Manager()
    
    class Meta:
        verbose_name = 'Contact'    

    def __str__(self):
        return self.name
    