import pywhatkit
from django.db import models
from authenticate_user.models import Course,User
# Create your models here.



class Notice(models.Model):
    title = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    date = models.DateField(auto_now_add=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    file = models.FileField(upload_to='notice/',null=True,blank=True)
    def __str__(self):
        return self.title



class Event(models.Model):
    title = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    date = models.DateField(auto_now_add=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    file = models.FileField(upload_to='notice/',null=True,blank=True)
    def __str__(self):
        return self.title

class Teacher(models.Model):
    image = models.ImageField(upload_to='teacher/')
    designation = models.CharField(max_length=150,null=True,blank=True)
    name = models.CharField(max_length=150)
    facebook = models.URLField(max_length=250)
    gmail = models.URLField(max_length=250)
    twitter = models.URLField(max_length=250)
    linkedin = models.URLField(max_length=250)
    description = models.TextField(null=True,blank=True)
    is_show = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class AboutUs(models.Model):
    about  = models.TextField()
    
    class Meta:
        verbose_name = 'About U'

    def __str__(self):
        return self.about

class TechnicalStaff(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='user/staff/')
    description = models.TextField()
    facebook = models.URLField()
    linkedin = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()

    def __str__(self):
        return self.name

class Gallery(models.Model):
    image = models.ImageField(upload_to='media/gallery')
    

class WhatsappGroup(models.Model):
    User = models.ManyToManyField(User,null=True,blank=True)
    group_name = models.CharField(max_length=150)

    def __str__(self):
        return self.group_name

class WhatsappMessage(models.Model):
    group = models.ForeignKey(WhatsappGroup, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        for number in self.group.User.all():
            pywhatkit.sendwhatmsg_instantly(number.phone_number,self.message,5,tab_close=False)
        super(WhatsappMessage,self).save(*args,**kwargs)

    