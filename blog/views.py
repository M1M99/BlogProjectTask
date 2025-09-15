from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from . import data

data.seed()
#domain.com/?q=Football
def post_list(request):
    posts=data.all_posts()
    q=request.GET.get('q')
    if q:
        q_low=q.lower()
        posts=[p for p in posts if q_low in p.title.lower() or q_low in p.content.lower()]

    return render(request,'blog/post_list.html',{"posts":posts})

def post_detail(request,post_id:int):
    post = data.get_post(post_id)
    if post is not None:
        return render(request,'blog/post_details.html',context={'post':post})
    else:
        return render(request,'blog/Notfound.html')