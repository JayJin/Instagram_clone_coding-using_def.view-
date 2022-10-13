from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PostModel, CommentModel
from .forms import PostForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:    # 사용자가 인증이 되었는지(로그인 되었는지)
        all_post = PostModel.objects.all().order_by('-created_at')
        return render(request, 'post/post/index.html', {'posts':all_post})
    else:
        return redirect('/sign-in')


def post_new(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'post/post/new_post.html')
        return render(request, 'account/user/login.html')
    
    elif request.method == 'POST':
        user = request.user     # 현재 로그인 한 사용자 불러오기
        content = request.POST.get('my-content','')
        image = request.FILES['image']              # 이미지 저장
        
        if content == '':
            return render(request, 'post/post/new_post.html', {'error':'글은 공백일 수 없습니다.'})
        else:
            my_post = PostModel.objects.create(author=user, image=image, content=content)
            my_post.save()
            return redirect('/')


@login_required
def post_delete(request, post_id):
    my_post = PostModel.objects.get(id=post_id)
    my_post.delete()
    return redirect('/')


@login_required
def post_update(request, post_id):
    my_post = PostModel.objects.get(id=post_id)
    if request.method == 'GET':
        post_form = PostForm(instance = my_post)
        return render(request, 'post/post/update_post.html', {'post':my_post, 'form':post_form})
    elif request.method == 'POST':
        my_post.content = request.POST['my-content']
        my_post.image = request.FILES['my-image']  
        my_post.save()
        return redirect('/')



@login_required
def comment_detail(request, id):
    my_post = PostModel.objects.get(id=id)
    post_comment = CommentModel.objects.filter(post_id=id).order_by('created_at')
    return render(request, 'post/post/comment_detail.html', {'post':my_post, 'comments':post_comment })       #'comment':post_comment
    
@login_required
def comment_write(request, id):
    if request.method == "POST":
        comment = request.POST.get('comment', '')
        cur_post = PostModel.objects.get(id=id)
        
        my_comment = CommentModel()
        my_comment.comment = comment
        my_comment.post = cur_post
        my_comment.author = request.user
        my_comment.save()
        return redirect('/comment/detail/'+str(id))


@login_required
def comment_delete(request, id):
    comment = CommentModel.objects.get(id=id)
    current_post = comment.post_id
    comment.delete()
    return redirect('/comment/detail/'+str(current_post))