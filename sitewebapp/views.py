from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, JsonResponse
from .models import event, Members, blog, Comments
from .forms import CommentForm
from django.utils import timezone
from django.views.decorators.cache import cache_control, never_cache
# Create your views here.


@never_cache
def about(request):
    return HttpResponse("fuckofff nothing here")


@never_cache
def index(request):
    someevents = event.objects.filter(
        active=True).order_by('-event_datetime')[:3]
    somemembers = Members.objects.filter(year=3).order_by('-post')
    someblogs = blog.objects.filter(active=True).order_by('-created_on')[:2]
    return render(request, 'sitewebapp/index.html', {'eventsI': someevents, 'membersI': somemembers, 'blogsI': someblogs})


@never_cache
def blog_home(request):
    blogs = blog.objects.filter(active=True).order_by('-created_on')
    return render(request, 'sitewebapp/blogHome.html', {'blogs': blogs})


@never_cache
def blog_view(request, blog_id):
    post = blog.objects.get(id=blog_id)
    comments = post.comments.filter(active=True)
    comment_form = CommentForm()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            try:
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.commented_on = timezone.now()
                new_comment.active = True
                new_comment = new_comment.save()
                comment_form = CommentForm()
                new_comment = None
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except:
                pass
        else:
            comment_form = CommentForm()
            new_comment = None
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        comment_form = CommentForm()
        return render(request, 'sitewebapp/blogPost.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})
    return render(request, 'sitewebapp/blogPost.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})


@never_cache
def event_home(request):
    events = event.objects.filter(active=True).order_by('-event_datetime')
    return render(request, 'sitewebapp/eventsHome.html', {'events': events})


@never_cache
def event_view(request, event_id):
    eventsingular = event.objects.get(id=event_id)
    return render(request, 'sitewebapp/Event.html', {'eventsingular': eventsingular})


@never_cache
def members(request):
    members4 = Members.objects.filter(year="3").order_by('-post')
    members3 = Members.objects.filter(year="2").order_by('-post')
    members2 = Members.objects.filter(year="1").order_by('-post')
    return render(request, 'sitewebapp/members.html', {'members4': members4, 'members3': members3, 'members2': members2})
