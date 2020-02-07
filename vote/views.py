from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage,Paginator
from .models import Item,Voted
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        messages.error(request,'You need to logout First')
        return redirect('Vote')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are Logged in')
            return redirect('Vote')
        else:
            messages.error(request,'Invalid Crediantials')
            return redirect('Login')
        return
    else:
        return render(request,'login.html')
def vote(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            items=Item.objects.all()
            paginator=Paginator(items,3)
            page=request.GET.get('page')
            pagged_items=paginator.get_page(page)

            context={
                'items':pagged_items
            }
            return render(request,'items1.html',context)
        else:
            items=Item.objects.all()
            paginator=Paginator(items,3)
            page=request.GET.get('page')
            pagged_items=paginator.get_page(page)

            context={
                'items':pagged_items
            }
            return render(request,'items.html',context)
        
    else:
        messages.error(request,'You need to login to access the page')
        return render(request,'login.html')

def voting(request,title):
    if request.user.is_authenticated:
        if request.user.is_staff:
            items=Item.objects.all()
            paginator=Paginator(items,3)
            page=request.GET.get('page')
            pagged_items=paginator.get_page(page)

            context={
                'items':pagged_items
            }
            messages.error(request,'Admin Cannot Vote')
            return redirect('Vote')
        else:
            voted_item=get_object_or_404(Item,title=title)
            username=request.user.username
            users = [user.username for user in Voted.objects.all()]
            if username in users:
                messages.error(request, 'You Have Already Voted')
                return redirect('Vote') 
            else:
                voted_item.count+=1
                voted_item.save()
                voted=Voted(username=username)
                voted.save()
                messages.success(request, 'Voted successfully')
                return redirect('Vote')
    else:
        messages.error(request,'You need to login to vote')
        return render(request,'login.html')

def AddItem(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method=='POST':
                title=request.POST['title']
                count=request.POST.get('count',0) 
                item=Item(title=title,count=count)
                item.save()
                messages.success(request,'New Item ADDED')
                return redirect('Vote')
            else:
                return render(request,'additem.html')
        else:
            messages.error(request,'Not Authorized')
            return redirect('Vote')
    else:
        messages.error(request,'You need to login as ADMIN')
        return render(request,'login.html')

def register(request):
    if request.user.is_authenticated:
        messages.error(request,'You need to logout First')
        return redirect('Vote')
    if request.method=='POST':
        
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'This Username is Not Available')
                return redirect('Register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'This Email is being Used')
                    return redirect('Register')
                else:
                    user=User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                    )
                    auth.login(request,user)
                    messages.success(request,'You are logged in')
                    return redirect('Vote')
        else:
            messages.error(request,'Passwords do not match')
            return redirect('Register')
    else:
        return render(request,'register.html')

def logout(request):
    if request.method=='POST':
       auth.logout(request)
       messages.success(request,'You are now logged out') 
       return redirect('Login')
    else:
        messages.error(request,'Not Logged In')
        return redirect('Login')