from django.shortcuts import render
from .models import Post,Comment,User
from django.shortcuts import get_object_or_404, redirect
from .forms import CommentPost, PostForm, AvatarUploadFrom
from django.http import HttpResponse, JsonResponse


def home(request):
    return render(request, 'blog/home.html')

def post_list(request):
    users = User.objects.all() 
    posts = Post.objects.all().order_by('-created_at')
    return render(request,'blog/post_list.html', {'posts':posts, 'users': users})
    

def post_detail(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    
    if request.method == 'POST':
        form = CommentPost(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentPost()
        
    return render(request,'blog/post_detail.html', {'post':post, 'comments':comments, 'form':form})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
        
    return render(request,'blog/create_post.html', {'form':form})
        

def upload_avatar(request):
    if request.method == 'POST':
        form = AvatarUploadFrom(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AvatarUploadFrom()
        
    return render(request, 'blog/upload_avatar.html', {'form': form})


def profile_view(request,user_id):
    users = get_object_or_404(User, id=user_id)
    return render(request, 'blog/profile.html')

