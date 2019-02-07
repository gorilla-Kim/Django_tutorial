from django.shortcuts import render
from .models import Album
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home(request):
    try:
        #모든 게시글을 기져오기
        albums = Album.objects.all()
        paginator = Paginator(albums, 3) # Show 25 contacts per page
        page = request.GET.get('page')
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    context = {'contacts': contacts}
    return render(request, 'album/home.html', context) 