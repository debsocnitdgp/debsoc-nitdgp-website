from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, JsonResponse
from .models import event, Members, blog, Comments
from django.db.models import Count
from .forms import CommentForm, MemberAddForm
from django.utils import timezone
from django.views.decorators.cache import cache_control, never_cache
# Create your views here.


@never_cache
def about(request):
    return render(request, 'sitewebapp/about.html')


@never_cache
def index(request):
    someevents = event.objects.filter(
        active=True).order_by('-event_datetime')[:3]
    somemembers = Members.objects.filter(year="Fourth").order_by('sno')
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
    events_up = event.objects.filter(active=True).filter(event_status='Upcoming').order_by('-event_datetime')
    events_past = event.objects.filter(active=True).filter(event_status='Past').order_by('-event_datetime')
    events_live = event.objects.filter(active=True).filter(event_status='Live').order_by('-event_datetime') 
    live_ev = int(len(events_live))
    print(live_ev)
    up_ev = int(len(events_up))
    return render(request, 'sitewebapp/eventsHome.html', {'events_up': events_up, 'events_past': events_past, 'events_live': events_live, 'live_ev': live_ev, 'up_ev': up_ev})


@never_cache
def event_view(request, event_id):
    eventsingular = event.objects.get(id=event_id)
    return render(request, 'sitewebapp/Event.html', {'eventsingular': eventsingular})


@never_cache
def members(request):
    members4 = Members.objects.filter(year="Fourth").order_by('sno')
    members3 = Members.objects.filter(year="Third").order_by('sno')
    members2 = Members.objects.filter(year="Second").order_by('post')
    return render(request, 'sitewebapp/members.html', {'members4': members4, 'members3': members3, 'members2': members2})

@never_cache
def cmember(request):
    if request.method == 'POST':
        cform = MemberAddForm(request.POST, request.FILES)
        newData = None
        if cform.is_valid():
            newData = cform.save(commit=False)
            newData = newData.save()
            cform = MemberAddForm()
            newData = None
            return HttpResponsePermanentRedirect(reverse(index))
        else:
            return HttpResponse("Firse bharna parega Error hai, back Jake dekhiye Kya error hai (Go back and check again plz)")
    else:
        cform = MemberAddForm()
    return render(request, 'sitewebapp/cmember.html', {'cform':cform})

def handler404(request, exception):
    return HttpResponse("Wrong URL")

def handler500(request):
    return HttpResponse("Wrong URL")

