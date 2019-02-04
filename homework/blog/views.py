from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    message = ""
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