from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def login(request):
    
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phno=request.POST['phno']
        username=request.POST['username']
        password=request.POST['password']
        data=User.objects.create(name=name,email=email,phno=phno,username=username,password=password)
        data.save()
    return render(request,'register.html')

def index(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        data=User.objects.get(username=username)
        if password==data.password:
           request.session['user']=username
           return render(request,'index.html',{'user':data})
        else:
            return redirect(login)
    else:
        return redirect(login)

def user_index(request,pk):
    if "user" in request.session:
        data=User.objects.get(pk=pk)
        data2=Post.objects.filter(uname=data)
        print(data2)
        return render(request,'user_index.html',{"user":data,"images":data2})

def add_post(request):
    if "user" in request.session:
        if request.method=="POST":
            user=User.objects.get(username=request.session['user'])
            image=request.FILES['image']
            desc=request.POST['description']
            data=Post.objects.create(uname=user,image=image,desc=desc)
            data.save() 
        return render(request,'add_post.html')