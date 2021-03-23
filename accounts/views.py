from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import profile
from django.contrib.auth.models import User
from .forms import login_form ,UpdatUserForm,UserCreationForms
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required


def app(request):
    doctors=User.objects.all()
    return render( request ,'user/app.html',{
        'doctors':doctors,
    })
    
def doctor_detail(request,slug):
    doctor_detail=profile.objects.get(slug =slug)
    return render( request ,'user/doctor_detail.html',{
        'doctor_detail': doctor_detail,
    })
def user_login(request):
    if request.method=='post':
        form = login_form()
        username = request.post['username']
        password = request.post['password']
        user = authenticate(request ,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('accounts:app')
    else:
        form=login_form()
       
    return render( request ,'user/login.html',{
       'form': form ,
    })
@login_required(login_url='accounts:login')   
def myprofile(request):
    return render(request ,'user/myprofile.html',{        
    })
    
def updat_profile(request):
    user_form=UpdatUserForm(instance=request.user)
    
    if request.method =='post':
        UpdatUserForm(request.Post ,instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('accounts:app')
    
    return render(request ,'user/updat_profile.html',{ 
        'user_form':user_form       
    })
def Sign_up(request):
    
    if request.method =='post':
        form = UserCreationForms(request.post)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForms()
        
     
    return render(request ,'user/Sign_up.html',{ 
        'form':form
              
    })

        
    
    