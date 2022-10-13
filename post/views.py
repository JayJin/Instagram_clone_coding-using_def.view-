from django.shortcuts import render, redirect
from .models import PostModel


# Create your views here.
def index(request):
    if request.user.is_authenticated:    # 사용자가 인증이 되었는지(로그인 되었는지)
        return redirect('/post-all')
    else:
        return redirect('/sign-in')
    

def post_all(request):
    all_post = PostModel.objects.all().order_by('-created_at')
    return render(request, 'post/post/all_post.html', {'posts':all_post})


def post_new(request):
    if request.method == 'GET':
        return render(request, 'post/post/new_post.html')
    elif request.method == 'POST':
        user = request.user     # 현재 로그인 한 사용자 불러오기
        content = request.POST.get('my-content','')
        
        if content == '':
            return render(request, 'post/post/new_post.html', {'error':'글은 공백일 수 없습니다.'})
        else:
            my_post = PostModel.objects.create(author=user, content=content)
            my_post.save()
            return redirect('/post-all')