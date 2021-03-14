from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from home.models import Contact
from django.contrib import messages
from app1.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        if len(name)<2:
            messages.error(request,"Fill name field correctly") 
        elif len(email)<6:
            messages.error(request,"Fill email field correctly")
        elif len(phone)<10 :
            messages.error(request,"Fill phone field correctly")
        elif len(content)<4:
            messages.error(request,"please fill details correctly")
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"thank you for contacting us")
    return render(request,"contact.html")

def blogHome(request):
    return render(request,'bloghome.html')

def search(request):
    query=request.GET['query']
    if len(query)>60:
        allPosts=Post.objects.none()
    else:
        allPostsTitle=Post.objects.filter(title__icontains=query)
        allPostsContent=Post.objects.filter(content__contains=query)
        allPosts=allPostsTitle.union(allPostsContent)
    if allPosts.count()==0:
        messages.error(request,"No search results found")
    params={"allPosts":allPosts,'query':query}
    return render(request,"search.html",params)

def handlesignup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['pass']
        confirmpass=request.POST['confirmpass']
        if len(username)>15 :
            messages.error(request,"username should be under 15 characters")
            return redirect('/')
        if username.isalnum():
            messages.error(request,"username should contain only alphabets and numbers")
            return redirect('/')

        if password!=confirmpass:
             messages.danger(request,"Enter the correct password")
             return redirect('/')

        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,"your account has been created successfully")
        return redirect('/')
    else:
        return HttpResponse("not found")
    
def handlelogin(request):
    if request.method=='Post':
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        loginconfirmpass=request.POST['loginconfirmpass']
        user=authenticate(username=loginusername,password=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/')
    return HttpResponse("404")



def handlelogout(request):
    
        logout(request)
        messages.success(request,"successfully logout")
        return redirect('/')
    

