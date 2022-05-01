from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib import messages
# Create your views here.
def index(req):
    return render(req, 'acc/index.html')

def login_user(req):
    if req.method == "POST":
        un = req.POST.get("uname")
        up = req.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(req, u)
            return redirect("acc:index")
        else:
            messages.error(req, "로그인 실패")
    return render(req, 'acc/login.html')

def logout_user(req):
    logout(req)
    return redirect("acc:index")

def signup(req):
    if req.method == "POST":
        un = req.POST.get("uname")
        up = req.POST.get("upass")
        ua = req.POST.get("uage")
        pi = req.FILES.get("upic")
        uc = req.POST.get("ucom")
        try:
            User.objects.create_user(username=un, password=up, age=ua, pic=pi, comment=uc)
            return redirect('acc:login')
        except:
            messages.error(req, "사용자 이름이 중복됩니다")     
    return render(req, 'acc/signup.html')

def profile(req):
    return render(req, 'acc/profile.html')

def update(req):
    if req.method == "POST":
        u = req.user
        up = req.POST.get("upass")
        ue = req.POST.get("email")
        ua = req.POST.get("uage")
        pi = req.FILES.get("upic")
        uc = req.POST.get("ucom")
        if up:
            u.set_password(up)
        if pi:
            u.pic.delete()
            u.pic = pi
        u.email = ue
        u.age = ua
        u.comment = uc
        u.save()
        login(req, u)
        return redirect('acc:profile')
    return render(req, 'acc/update.html')

def delete(req):
    if req.method == "POST":
        up = req.POST.get("upass")
        if check_password(up, req.user.password):
            req.user.delete()
            return redirect('acc:index')
        else:
            messages.error(req, "비밀번호가 일치하지 않습니다.")
            return redirect('acc:profile')
    return render(req, 'acc/delete.html')

def delete2(req):
    pwck = req.POST.get("pwck")
    print(pwck)
    if check_password(pwck, req.user.password):
        req.user.pic.delete()
        req.user.delete()
        return redirect('acc:index')
    else:
        messages.error(req, "비밀번호가 일치하지 않습니다.")
        return redirect('acc:profile')