from django.shortcuts import render, redirect
from django.contrib import auth     # 사용자 인증 기능        # ★
from django.contrib.auth.decorators import login_required        # ★
from django.contrib.auth.hashers import check_password        # ★

from .models import UserModel

# Create your views here.
def sign_up_view(request):
    if request.method == "GET":
        user = request.user.is_authenticated        # ★
        if user:
            return redirect('/')
        else:
            return render(request, 'user/account/signup.html')
        
    elif request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')
        
        if password != password2:
            return render(request, 'user/account/signup.html', {'error':"비밀번호가 같지 않습니다."})
        else:
            if username == '' or password == '' or email == '':
                return render(request, 'user/account/signup.html', {'error':"공백은 입력불가합니다."})
            exist_email = UserModel.objects.filter(email=email)         # ★
            if exist_email:
                return render(request, 'user/account/signup.html', {'error':"존재하는 이메일입니다."})
            else:
                UserModel.objects.create_user(email=email, password=password, username=username)        # ★
                return redirect('/sign-in')
        
def sign_in_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/account/signin.html')
    elif request.method == 'POST':
        email = request.POST.get('email', '')
        username = UserModel.objects.get(email=email)         # ★
        password = request.POST.get('password', '')
        me = auth.authenticate(request, username=username, password=password)         # ★
        if me is not None:
            auth.login(request, me)         # ★
            return redirect('/')
        else:
            return render(request, 'user/account/signin.html', {'error':'입력값을 다시 확인해주세요'})

# 로그아웃
@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

# 계정 삭제
def account_delete(request):
    if request.method == "POST":        # ★
        pw_del = request.POST.get('pw_del','')
        user = request.user
        if check_password(pw_del, user.password):
            user.delete()
            return redirect('/')
    return render(request, 'user/account/account_delete.html')
