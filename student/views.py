from django.shortcuts import render, redirect
from django.views import View
from .models import ApplyForJob
from authenticate_user.models import *
from human_resource.models import *
from django.db.models import Q
from authenticate_user.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class UserResume(View):
    @method_decorator(login_required(login_url='/login'))
    def get(self,request,id):
        Resume.objects.get(id=id).delete()
        return redirect('profile')

    @method_decorator(login_required(login_url='/login'))
    def post(self,request):
        resume = request.FILES.get('resume')
        Resume.objects.create(
            user=request.user,
            resume=resume
        )
        return redirect('profile')



class AllJobs(View):

    template_name = "all_jobs.html"

    @method_decorator(login_required(login_url='/login'))
    def get(self,request):
        try:
            grade = request.user.user_qulification.filter(course_type='GRADUATE').first().grades
            all_jobs = Job.objects.exclude(id__in=request.user.user_jobs.values('job__id').all()).filter(requred_grades__lte=grade)
            context = {
                'jobs':all_jobs
            }
            return render(request,self.template_name,context)
        except:
            return render(request,self.template_name)

class StudentJob(View):

    template_name = 'student_job.html'

    @method_decorator(login_required(login_url='/login'))
    def get(self,request):
        return render(request,self.template_name)


class ApplyJob(View):  

    @method_decorator(login_required(login_url='/login'))
    def get(self,request,id):
        ApplyForJob.objects.create(
            user=request.user,
            job_id=id
        )
        return redirect('all_jobs')


class Chat(View):

    template_name = 'chat.html'

    @method_decorator(login_required(login_url='/login'))
    def get(self,request):
        user = User.objects.exclude(id=request.user.id)
        context = {
            'user':user
        }
        return render(request,self.template_name,context)

class ChatUser(View):

    template_name = 'chat.html'

    @method_decorator(login_required(login_url='/login'))
    def get(self,request,id):
        get_user = User.objects.get(id=id)
        user = User.objects.exclude(id=request.user.id)
        
        context = {
            'get_user':get_user,
            'user':user
        }
        return render(request,self.template_name,context)




class PlacementTraning(View):

    template_name = 'placement_traning.html'

    @method_decorator(login_required(login_url='/login'))
    def get(self,request):
        traning = Traning.objects.all()
        train = TraningApplication.objects.exclude(user=request.user).filter(traning__is_active=True)
        context = {
            'cat':train.values('traning__category__name','traning__title','traning__course').distinct(),
            'traning':train.values('traning__id','traning__title','traning__course_image','traning__course','traning__category__name','traning__description')
        }
        return render(request,self.template_name,context)

    @method_decorator(login_required(login_url='/login'))
    def post(self,request):
        id = request.POST.get('train-id')
        train = TraningApplication.objects.get(id=id)
        train.user.add(request.user)
        return redirect('placement')


class TraningInfo(View):
    template_name = 'traning_info.html'


    @method_decorator(login_required(login_url='/login'))
    def get(self,request,id):
        train = TraningApplication.objects.get(id=id)
        context = {
            'train':train
        }
        return render(request,self.template_name,context)

    


class PdfDownload(View):

    def get(self,request):
        pass