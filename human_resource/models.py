from django.db import models
from authenticate_user.models import User
from django.template.defaultfilters import slugify
from django.db import transaction
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from authenticate_user.models import User
from django.dispatch import receiver
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.mail import EmailMessage

# Create your models here.



class Job(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length = 150,null=True,blank=True)
    course = models.CharField(max_length=150)
    requred_grades = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    
    class Meta:
        verbose_name = 'Available Job'
   

    def save(self,*args,**kwargs):
        user = User.objects.values("email").filter(is_staff=False).filter(is_superuser=False)
        lt = []
        for user in user:
            lt.append(user['email'])

        send_mail("New Job Available","New Job Has Been Posted \nCheck Out Now.\n[SSM College Training & Placement]\nParihaspora,Pattan",settings.EMAIL_HOST_USER,lt)
        self.slug = slugify(self.title)
        super(Job, self).save(*args,**kwargs)

        
    def __str__(self):
        return self.title



class SendMail(models.Model):
    title = models.CharField(max_length = 150)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    
    description = RichTextUploadingField(blank=True)
    

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        super(SendMail,self).save(*args,**kwargs)


@receiver(post_save, sender=SendMail)
def send_mail_to_subs(sender, instance, created, **kwargs):
    lt = []
    lt.append(instance.user.email)
    html_template = instance.description
    message = EmailMessage(instance.title, html_template, settings.EMAIL_HOST_USER, lt)

    message.content_subtype = 'html'
    message.send()
    #send_mail(instance.title,instance.description,settings.EMAIL_HOST_USER,lt)



class TraningCategory(models.Model):
    name = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Traning'

class Traning(models.Model):
    title = models.CharField(max_length = 150)
    course_image = models.ImageField(upload_to='course/image/')
    zoom_url = models.URLField(max_length = 200)
    category = models.ForeignKey(TraningCategory, on_delete=models.CASCADE)
    course = models.CharField(max_length=150)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class TraningApplication(models.Model):
    user = models.ManyToManyField(User,related_name='user_traning',null=True,blank=True)
    traning = models.ForeignKey(Traning, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.traning.title

    
    def save(self,*args,**kwargs):
        user = User.objects.values("email").filter(is_staff=False).filter(is_superuser=False)
        lt = []
        for user in user:
            lt.append(user['email'])

        send_mail("New Training Available","New Training Has Been Posted \nCheck Out Now.\n[SSM College Training & Placement]\nParihaspora,Pattan",settings.EMAIL_HOST_USER,lt)
        super(TraningApplication, self).save(*args,**kwargs)

    class Meta:
        verbose_name = 'Traning Application'
