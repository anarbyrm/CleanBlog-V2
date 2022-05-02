from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from .models import Post
from .forms import PostCreateForm, ContactForm
# Create your views here.

""" Template Views """

@login_required()
def home(request):
    posts = Post.objects.all().order_by('-date_published')
    #searching posts
    if request.method == "GET":
        search = request.GET.get('q')
        if search is not None:
            posts = Post.objects.filter(title__icontains=search).order_by('-date_published')
            #pagination    
            paginator = Paginator(posts, 5)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        
    #pagination    
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'objs': posts,  'page_obj': page_obj}

    return render(request, 'index.html', context)


@login_required()
def user_posts(request, username):

    posts = Post.objects.filter(author__username=username)
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'objs': posts, 'page_obj': page_obj}

    return render(request, 'user_posts.html', context)



@login_required()
def about(request):
    return render(request, 'about.html')


@login_required()
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post' : post}

    return render(request, 'post.html', context)


@login_required()
def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been succesfully delivered!')
            return redirect('home')
            
    context = {'form':form}
    return render(request, 'contact.html', context)

#--------------------------------------------------------------
""" CRUD Views """


@login_required()
def create_view(request):
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            form.save(commit=False)
            form.instance.author = request.user
            form.save()

            return redirect('home')

    return render(request, 'post_create.html', {'form':form})


@login_required()
def update_view(request, pk):
    obj = get_object_or_404(Post, id=pk)

    if obj.author == request.user:
        form = PostCreateForm(instance = obj)

        if request.method == "POST":
            form = PostCreateForm(request.POST, instance = obj)

            if form.is_valid():
                form.save()

                return redirect('detail', pk=pk)
            #  pk=pk  ---> first pk comes from url (<int:pk>) 
            # second one comes from parameter that we given.
    else:
        return HttpResponseForbidden(request)

    context = {'form':form,'post':obj}

    return render(request, 'update.html', context)


@login_required()
def delete_view(request, pk):
    post = Post.objects.get(id=pk)
    if post.author == request.user:

        if request.method == "POST":
            post.delete()

            return redirect('home')
    else:
        return HttpResponseForbidden(request)

    return render(request, 'delete.html', {'post':post})
