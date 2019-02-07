from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    message = ""
    if request.session.get('message', False):
        message = request.session['message']
        del request.session['message']
    print("*********")
    print(message)
    try:
        #모든 게시글을 기져오기
        posts = Post.objects.all()
        paginator = Paginator(posts, 5) # Show 25 contacts per page
        page = request.GET.get('page')
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
        message = "더이상 게시글이 존재하지 않습니다."
    except:
        message = "게시글이 존재하지 않습니다."
    context = {'contacts': contacts, 'message':message}
    return render(request, 'blog/home.html', context)

def post_view(request, pk):
    try:
        post = Post.objects.get(pk = pk)
        message = ""
    except:
        message = "error"
    context = {'post':post, 'message':message}
    return render(request, 'blog/post_view.html', context)

def post_update(request, pk):
    post = Post.objects.get(pk = pk)
    try:
        if request.method == 'POST':
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.password = request.POST.get('password')
            post.save()
            return redirect(reverse('home_blog'))
    except:
        request.session['message'] = "Server Error"
        return redirect(reverse('home_blog'))
    context = {'post':post}
    return render(request, 'blog/post_form.html', context)

def pw_check(request):
    password = request.POST.get('password')
    pk = request.POST.get('pk')
    try:
        post = Post.objects.get(pk = pk) 
        # 패스워드 불일치 
        if not (post.password == str(password)):
            request.session['message'] = "패스워드가 일치하지 않습니다."
        # 패스워드 일치
        else:
            if request.POST.get('site') == "update":
                print("*******update******")
                return redirect('post_update', pk)
            elif request.POST.get('site') == "delete":
                print("*******delete******")
                return redirect('post_delete', pk)
    except:
        request.session['message'] = "Server Error1"
        return redirect(reverse('home_blog'))
    return redirect(reverse('home_blog'))

def post_create(request):
    if request.method == "POST":
        post = Post(
            password = request.POST.get('password'),
            title = request.POST.get('title'),
            content = request.POST.get('content')
        )
        post.save()
        return redirect(reverse('home_blog'))
    context = {}
    return render(request, 'blog/post_form.html', context)

def post_delete(request, pk):
    post = Post.objects.get(pk = pk)
    post.delete()
    return redirect('home_blog')