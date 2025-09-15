from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect

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


# def delete(request,post_id):
#     post=data.get_post(post_id)
#     if post is not None:
#         response = data.delete_post(post.id)
#         if response:
#             return HttpResponse('Deleted')
#         else:
#             return HttpResponse('204 No Content')
#     else:
#         return HttpResponse('404 Not Found')
#
@require_http_methods(["POST"])
def post_delete(request, post_id):
    post = data.get_post(post_id)
    if post is not None:
        deleted = data.delete_post(post.id)
        if deleted:
            return redirect('/')
        else:
            return HttpResponse(status=204)
    else:
        return HttpResponse("Post not found")