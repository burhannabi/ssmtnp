from django.shortcuts import render
from django.views import View
from .models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


class CollegeNotice(View):

    template_name = 'notice.html'

    @method_decorator(login_required(login_url='/login'))
    def get(self,request):
        context = {
            'notice':Notice.objects.all()
        }
        return render(request,self.template_name,context)



class CollegeAbout(View):
    
    template_name = 'about.html'

    @method_decorator(login_required(login_url='/login'))
    def get(self,request):
        context = {
            'staff':TechnicalStaff.objects.all(),
            'about':AboutUs.objects.first()
        }
        return render(request,self.template_name,context)
