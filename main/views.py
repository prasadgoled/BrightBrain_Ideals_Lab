from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import ideaDetails
from .forms import ideaForm,signupForm,loginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def homePage(request):
    ideas=ideaDetails.objects.all()
    return render(request,'main/home.html',{'ideas':ideas})

def aboutPage(request):
    return render(request,'main/about.html')

def addIdeaPage(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=ideaForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return HttpResponseRedirect('/main/dashboardpage/')
        else:
            form=ideaForm()
        return render(request,'main/addIdea.html',{'form':form})
    else:
        return HttpResponseRedirect('/main/loginpage/')
    
def updateIdeaPage(request,id):
    if request.user.is_authenticated:
        data = ideaDetails.objects.get(id=id)
        if request.method=='POST':
            form=ideaForm(request.POST,instance=data)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/main/dashboardpage/')
        else:
            pi = ideaDetails.objects.get(id=id)
            form=ideaForm(instance=data)
        return render(request,'main/updateIdea.html',{'form':form})
    else:
        return HttpResponseRedirect('/main/loginpage/')
    
def deleteIdea(request,id):
    if request.user.is_authenticated:
        ideaDetails.objects.get(id=id).delete()
        return HttpResponseRedirect('/main/dashboardpage/')
    else:
        return HttpResponseRedirect('/main/loginpage/')
    
def dashboardPage(request):
    if request.user.is_authenticated:
        u = request.user
        if u.is_superuser:
            ideas=ideaDetails.objects.all()
        else:
            ideas=ideaDetails.objects.filter(user=u)
        return render(request,'main/dashboard.html',{'ideas':ideas})
    else:
        return HttpResponseRedirect('/main/loginpage/')
    
def signupPage(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('captcha'):
                form.save()
                messages.success(request, 'Congratulations! Your account has been successfully created')
            else:
                form.add_error('captcha', 'Invalid CAPTCHA. Please try again.')
        else:
            messages.error(request, 'Failed to create an account. Please check the form data.')
    else:
        form = signupForm()
    return render(request, 'main/signup.html', {'form': form})


def loginPage(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = loginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user:
                    login(request, user)
                    messages.success(request, 'Login successful. Welcome to the dashboard!')
                    return HttpResponseRedirect('/main/dashboardpage/')
                else:
                    messages.error(request, 'Invalid username or password. Please try again.')
        else:
            form = loginForm()
        return render(request, 'main/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/main/dashboardpage/')
    
def logoutPage(request):
    logout(request)
    return HttpResponseRedirect('/main/homepage/')