from django.db import models
from human_resource.models import *
from authenticate_user.models import User
# Create your models here.

status = (
    ("PENDING","PENDING"),
    ("SELECTED","SELECTED"),
    ("REJECTED","REJECTED"),
)


class ApplyForJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name='user_jobs')
    job = models.ForeignKey(Job, on_delete=models.CASCADE,null=True,blank=True,related_query_name='job_in')
    date = models.DateField(null=True,blank=True)
    interview_start_time = models.TimeField(null=True,blank=True)
    interview_end_time = models.TimeField(null=True,blank=True)
    application_status = models.CharField(max_length = 150,choices=status,default="PENDING")
    
    
    class Meta:
        verbose_name = 'Job Application'
    


COURSE_TYPE = (
    ('10','10'),
    ('12','12'),
    ('GRADUATE','GRADUATE'),
    ('POST-GRADUATE','POST-GRADUATE'),
)
    

    
class StudentQualification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_qulification')
    course_type = models.CharField(max_length=150,choices=COURSE_TYPE,null=True,blank=True)
    course_name = models.CharField(max_length=150)
    grades = models.FloatField()
    session = models.CharField(max_length=150)
    institute = models.CharField(max_length=150)
    university_name = models.CharField(max_length=150)

    def __str__(self):
        return self.user.username

