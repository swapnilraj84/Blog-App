from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import get_object_or_404 ,  redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def blog_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request , 'blog_list.html' , {'posts': posts})

def blog_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('blog_list') 
    else:
        form = PostForm()
    return render(request , 'blog_create.html' , {'form': form})

def blog_edit(request , blog_id):
    post = get_object_or_404(Post , pk = blog_id , user = request.user)
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES , instance=post)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = PostForm(instance=post)
        return render(request , 'blog_edit.html' , {'form': form})
    
def blog_delete(request , blog_id):
    post = get_object_or_404(Post , pk = blog_id , user = request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_list')
    return render(request , 'blog_delete.html' , {'post': post})

