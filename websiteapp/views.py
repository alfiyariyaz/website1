from django.shortcuts import render,redirect
from . models import product
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def mainfun(request):
    data=product.objects.all()
    return render(request,'website.html',{'data':data})


def newfun(request,cardid):
    data=product.objects.get(id=cardid)
    return render(request,'demo.html',{'data':data})
   


def searching(request):
    search=request.POST['Search']
    print(search)
    data=product.objects.filter(name=search)
    return render(request,'website.html',{'data':data})
    

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        print(username)
        print(password)
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')



    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username is taken') 
            return redirect('register')
        
        elif password1!=password2:
            messages.info(request,'Password error')
            return redirect('register')
        else:
            user=User.objects.create_user(username=username,password=password1)
            user.save()
            return redirect('/')

    else:
        return render(request,'register.html')
    