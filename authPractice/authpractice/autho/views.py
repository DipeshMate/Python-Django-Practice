from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate , login , logout, update_session_auth_hash
from .forms import SignUp_Form, Login_Form, PostForm
from django.contrib import messages
from .models import Post
from django.core.cache import cache
from autho import signals
 

# Create your views here.

def Home(request):
    fm = Post.objects.all()
    return render(request, 'Home.html',{'form':fm})

def Sign_Up(request):
   if request.method == 'POST':
       form = SignUp_Form(request.POST)
       if form.is_valid():
           messages.success(request,'Congratulations {request.user}, You have become a Premium Member of TrackMyWork !! ')
           user = form.save()
           form = SignUp_Form()
    # add user to group
           group = Group.objects.get(name='Author')
           user.groups.add(group)
   else:
       form = SignUp_Form()
   return render(request, 'signup.html',{'form':form}) 

def Log_In(request):
  if not request.user.is_authenticated:
    if request.method == 'POST':
        form = Login_Form(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username') 
            pword = form.cleaned_data.get('password') 
            email = form.cleaned_data.get('email')
            check = authenticate(username=uname,password=pword,email=email)
            if check is not None:
              login(request,check)
              messages.success(request, f'{request.user} Successfully Logged In!')  
              return redirect('/profile/')          
    else:
        form = Login_Form()   
    return render(request, 'login.html',{'form':form})
  else:
    return redirect('/profile/')
 
def Log_out(request):
    logout(request)
    msg = messages.success(request,'Logged Out Successfully !!')
    return render(request, 'Home.html', {'messages':msg})


def ResetPassword(request):
    # if request.user.is_authenticated:
    #     if request.method == 'POST':
    #       fm = PasswordChangeForm(user=request.user, data=request.POST)
    #       if fm.is_valid():
    #         fm.save()
    #         update_session_auth_hash(request,fm.user)
    #         return redirect('/profile/')
    #     else:       
    #       fm = PasswordChangeForm(user=request.user)
    #       return render(request,'resetpassword.html',{'form':fm})
    return redirect('/login/')

def Profile(request):
   if request.user.is_authenticated:
       work = Post.objects.all()
       user = request.user
       fullname = user.get_full_name() #just above user
       gps = user.groups.all() 
       ip = request.session.get('ip')
       ct = cache.get('count',version=user.pk)
       return render(request, 'profile.html', {'form':work,
            'name':request.user,'fullname':fullname, 
            'groups':gps,'ip':ip,'ct':ct})
   else:
       return redirect('/login/')
   
   
def AddPost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            signals.notification.send(sender=None, request=request,user=['Dipesh','Mate'])
            pf = PostForm(request.POST)
            if pf.is_valid():
              title = pf.cleaned_data.get('title')
              desc = pf.cleaned_data.get('desc')
              ps = Post(title=title, desc=desc)
              ps.save()
              pf = PostForm()
        else:
            pf = PostForm()
        return render(request, 'addPost.html',{'form':pf})
    else:
        return redirect('/login/')
    
    
    
def UpdatePost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pst = Post.objects.get(pk=id)
            pstfm = PostForm(request.POST, instance=pst)
            if pstfm.is_valid():
               pstfm.save()
        else:
            pst = Post.objects.get(pk=id)
            pstfm = PostForm(instance=pst)
        return render(request, 'updatePost.html',{'form':pstfm})
    else:
        return redirect('/login/')
    
def deletePost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
           fm = Post.objects.get(pk=id)
           fm.delete()
        return HttpResponseRedirect('/profile/')
    else:
        return redirect('/login/')