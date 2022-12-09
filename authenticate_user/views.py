from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from .models import *
from django.http import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from student.models import *
from administrator.models import *

class LoginUser(View):
    template_name = 'login.html'

    def get(self,request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, self.template_name)

    def post(self,request):
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request,user)
            return redirect('home')
        else:
            context = {
                'details':'Invalid Cridential'
            }
            return render(request, self.template_name,context)




def get_course_data(request):
    course = Course.objects.get(id=request.GET.get('data'))
    return HttpResponse(course.description)


class Home(View):
    template_name = 'home.html'

    def get(self,request):
        course = Course.objects.all()[:3]
        teachers = Teacher.objects.all()[:3]
        notice = Notice.objects.all()[:5]
        event = Event.objects.all()[:5]
        context = {
            'course':course,
            'teachers':teachers,
            'notice':notice,
            'events':event,
            'gallery1':Gallery.objects.all()[0:3],
            'gallery2':Gallery.objects.all()[3:6],
            'gallery3':Gallery.objects.all()[6:9],
            'about':AboutUs.objects.first()
        }
        return render(request,self.template_name,context)


class Contact(View):
    template_name = 'contact.html'

    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = ContactDetails.contact.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        return redirect('contact')


class Register(View):

    def post(self,request):
        User.objects.create_users(
            username = request.POST.get('roll'),
            password = request.POST.get('password'),
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            email = request.POST.get('email')
        )
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('home')


class Profile(View):

    @method_decorator(login_required(login_url='/login'))
    def get(self,request):
        return render(request,'profile.html')

    @method_decorator(login_required(login_url='/login'))
    def post(self,request):
        if request.FILES.get('profile_pic'):
            request.user.profile_pic = request.FILES['profile_pic']

        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.email = request.POST.get('email')
        request.user.phone_number = request.POST.get('phone')
        address = Addres(
            address=request.POST.get('address'),
            state=request.POST.get('state'),
            city=request.POST.get('city'),
            zip=request.POST.get('zip')
        )
        address.save()
        request.user.address = address
        request.user.save()
        return redirect('profile')




class Qualification(View):

    @method_decorator(login_required(login_url='/login'))
    def get(self,request,id):
        StudentQualification.objects.get(id=id).delete()
        return redirect('profile')


    @method_decorator(login_required(login_url='/login'))
    def post(self,request):
        course_type = request.POST.get('course_type')
        course = request.POST.get('course')
        grade = request.POST.get('grade')
        session = request.POST.get('session')
        institute = request.POST.get('institute')
        university = request.POST.get('university')
        qualification = StudentQualification.objects.create(
            user=request.user,
            course_type=course_type,
            course_name=course,
            grades=grade,
            session=session,
            institute=institute,
            university_name=university
        )
        return redirect('profile')


class Dashboard(View):
    template_name = 'dashboard.html'

    @method_decorator(login_required(login_url='/login'))
    def get(self,request):
        return render(request, self.template_name)




class ProfileView(View):

    def get(self,request):
        return render(request,'profile_preview.html')



class GalleryView(View):

    def get(self,request):
        context = {
            'gallery':Gallery.objects.all()
        }
        return render(request,'gallery.html',context)




class NoticeView(View):

    def get(self,request):
        context = {
            'notice':Notice.objects.all()
        }
        return render(request,'notices.html',context)


class EventView(View):

    def get(self,request):
        context = {
            'event':Event.objects.all()
        }
        return render(request,'event.html',context)