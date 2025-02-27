from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Comment, Like, BlogPost,Post
from .forms import BlogPostForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import PostForm
from django.contrib import messages
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse

def home(request):
    posts = BlogPost.objects.filter(published=True).order_by('-created_at')
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            post_id = request.POST.get('post_id')
            post = BlogPost.objects.get(id=post_id)
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

    return render(request, 'home.html', {
        'posts': posts,
        'comment_form': comment_form,
    })


def about(request):
    return render(request, 'about.html')

def blog_view(request):
    return render(request, 'blog.html')

def blog_list(request):
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    for post in blog_posts:
        post.comments = post.comment_set.all()  
        post.likes_count = post.likes.count() 

    return render(request, 'blog_list.html', {'blog_posts': blog_posts})

def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user  
            new_post.save()  
            
            return redirect(reverse('blog:home'))  
    else:
        form = BlogPostForm()
    
    return render(request, 'blog/create_blog.html', {'form': form})

def post_comment(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, id=blog_post_id)  
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.blog_post = blog_post  
            comment.save()
            return redirect('blog_detail', blog_id=blog_post.id)  
    else:
        form = CommentForm()

    return render(request, 'post_comment.html', {'form': form, 'blog_post': blog_post})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comment_set.all()  
    form = CommentForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        Comment.objects.create(blog_post=post, user=request.user, content=form.cleaned_data['content'])
        return redirect('blog_detail', post_id=post.id) 

    return render(request, 'blog_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })

@login_required
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', blog_post_id=comment.blog_post.id)

    return render(request, 'delete_comment.html', {'comment': comment})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if post.author == request.user:  
        post.delete()  
        return redirect('homepage') 
    return redirect('post_detail', blog_post_id=post.id)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    
    if request.method == 'POST':
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            print(f"User {request.user.username} unliked post {post.title}. New like count: {post.likes.count()}")
        else:
            post.likes.add(request.user)
            print(f"User {request.user.username} liked post {post.title}. New like count: {post.likes.count()}")

    return redirect('blog:home')  

@login_required
def add_comment(request, blog_post_id):
    post = get_object_or_404(BlogPost, id=blog_post_id)  
    if request.method == "POST":
        content = request.POST.get('content')
        comment = Comment(content=content, post=post, author=request.user)
        comment.save()
        return HttpResponseRedirect(reverse('blog_detail', args=[post.id]))  
    return render(request, 'add_comment.html', {'post': post})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('blog:home') 
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

def profile(request):
    return render(request, 'profile.html') 

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home') 
            
        else:
            error_message = "Invalid credentials"
            return render(request, 'registration/login.html', {'error_message': error_message})
    
    return render(request, 'registration/login.html')





