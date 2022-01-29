from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate,login,logout,get_user_model
from users.models import CustomUser
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def about(request):
    return render(request,'about.html')

def index(request):
    return render(request,'index.html')
    
def contact(request):
    return render(request,'contact.html')

def user_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username = u, password = p)
        try:
            if user:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,'login.html', d)

def signup(request):
    error=""
    if request.method=="POST":
        f = request.POST['first_name']
        l = request.POST['last_name']
        r = request.POST['regno']
        e = request.POST['email']
        b = request.POST['branch']
        u = request.POST['username']
        p = request.POST['password']
        try:
            user = CustomUser.objects.create_user(username=u,password=p,first_name=f, last_name=l, regno=r, email=e, branch=b)
            error="no"
        except:
            error="yes"
    d={"error":error}
    return render(request,'signup.html',d)

def admin_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username = u, password = p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,'admin_login.html', d)

def admin_home(request):
    if not request.user.is_staff:
        return redirect('admin_login')

    notes = Note.objects.all()

    a,b,c,d=0,0,0,0
    for note in notes:
        if note.status == 'pending':
            a+=1
        elif note.status == 'verified':
            b+=1
        else:
            c+=1
        d+=1
        
    dic = {'a':a,'b':b,'c':c,'d':d}

    return render(request,'admin_home.html',dic)


def Logout(request):
    logout(request)
    return redirect('index')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = CustomUser.objects.get(id=request.user.id)
    return render(request,'profile.html',{'user':user})

def password_change(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    if request.method=="POST":
        o = request.POST['old']
        n = request.POST['new']
        c = request.POST['confirm']
        if n==c:
            user = CustomUser.objects.get(username__exact=request.user.username)
            user.set_password(n)
            user.save()
            error="no"
        else:
            error="yes"
    d={'error':error}
    return render(request,'password_change.html',d)

def profie_edit(request):
    if not request.user.is_authenticated:
        redirect('user_login')
    
    user=CustomUser.objects.get(id=request.user.id)
    error=True
    if request.method=="POST":
        f = request.POST['first_name']
        l = request.POST['last_name']
        r = request.POST['regno']
        b = request.POST['branch']

        user.first_name = f
        user.last_name = l
        user.regno = r
        user.branch = b
        user.save()
        error=False

    return render(request,'profile_edit.html',{'user':user,'error':error})

def notes_upload(request):
    if not request.user.is_authenticated:
        redirect('user_login')
    error=""
    if request.method=="POST":
        a = CustomUser.objects.filter(username=request.user.username).first()
        b = request.POST['branch']
        s = request.POST['subject']
        f = request.FILES['notesfile']
        ft = request.POST['filetype']
        d = request.POST['description']
        try:
            Note.objects.create(author=a,branch=b,uploaddata=date.today(),subject=s,notesfile=f,filetype=ft,description=d,status='pending')
            error="no"
        except:
            error="yes"
        

    return render(request,'notes_upload.html',{'error':error})

def view_my_notes(request):

    if not request.user.is_authenticated:
        redirect('user_login')
    else:
        user = CustomUser.objects.get(id=request.user.id)
        notes = Note.objects.filter(author=user)
        
        d={'notes':notes,}

        return render(request,'view_my_notes.html',d)

def delete_my_notes(request,pid):
    if request.user.is_authenticated:
        redirect('user_login')
    else:
        note = Note.objects.get(id=pid)
        note.delete()

    return redirect('view_my_notes')

def view_users(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        redirect('admin_login')
    
    users = CustomUser.objects.all()

    return render(request,'view_users.html',{'users':users})

def delete_user(request,pid):
    if not request.user.is_authenticated or not request.user.is_staff:
        redirect('admin_login')
    else:
        user = CustomUser.objects.get(id=pid)
        user.delete()

    return redirect('view_users')

def pending_notes(request):

    if not request.user.is_authenticated or not request.user.is_staff:
        redirect('admin_login')
    else:
        notes = Note.objects.filter(status='pending')
        d={'notes':notes}

    return render(request,'pending_notes.html',d)

def assign_status(request,pid):
    error=""
    if not request.user.is_authenticated or not request.user.is_staff:
        redirect('admin_login')
    else:
        note = Note.objects.get(id=pid)
        if request.method=="POST":
            s = request.POST['status']
            try:
                note.status = s
                note.save()
                error="no"
            except:
                error="yes"
    return render(request,'assign_status.html',{'error':error})

def verified_notes(request):

    if not request.user.is_authenticated or not request.user.is_staff:
        redirect('admin_login')
    else:
        notes = Note.objects.filter(status="verified")
        d={'notes':notes}

    return render(request,'verified_notes.html',d)

def rejected_notes(request):

    if not request.user.is_authenticated or not request.user.is_staff:
        redirect('admin_login')
    else:
        notes = Note.objects.filter(status="rejected")
        d={'notes':notes}

    return render(request,'rejected_notes.html',d)

def all_notes(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        redirect('admin_login')
    else:
        notes = Note.objects.all()

    return render(request,'all_notes.html',{'notes':notes})

def delete_note(request,pid):
    if not request.user.is_authenticated or not request.user.is_staff:
        redirect('admin_login')
    else:
        note = Note.objects.get(id=pid)
        note.delete()

    return redirect('all_notes')
def all_notes_user(request):
    if not request.user.is_authenticated:
        redirect('user_login')
    notes = Note.objects.filter(status="verified")

    return render(request,'all_notes_user.html',{'notes':notes})