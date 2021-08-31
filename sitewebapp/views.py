from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, JsonResponse
from .models import *
from django.db.models import Count
from .forms import CommentForm, MemberAddForm, blogcform,alumniform
from django.utils import timezone
from django.views.decorators.cache import cache_control, never_cache
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from datetime import datetime
from django.http import HttpResponseRedirect
import csv
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
                new_comment.comment_by=str(request.user)
                new_comment.active = True
                new_comment.save()
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
    live_ev = events_live.count()
    print(live_ev)
    up_ev = events_up.count()
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
            k=cform.cleaned_data['year']
            objmem=Members.objects.filter(year=k)
            c=objmem.count()                #makes easier for allocating sno 
            c=c+1
            newData = cform.save(commit=False)
            newData.sno=c
            newData.save()
            return HttpResponsePermanentRedirect(reverse(index))
        else:
            return HttpResponse("Error go back and check again plz!!!")
    else:
        cform = MemberAddForm()
    return render(request, 'sitewebapp/cmember.html', {'cform':cform})




@never_cache
def apd2(request):
    return render(request, 'sitewebapp/apd2.html')

def handler404(request, exception):
    return HttpResponse("Wrong URL")

def handler500(request):
    return HttpResponse("Wrong URL")

@user_passes_test(lambda u: u.is_staff)                                             #a form to create blogs
@never_cache
def create_blog(request):
    if request.method=='POST':

        blogcreate= blogcform(request.POST,request.FILES)
        if blogcreate.is_valid():
            bc=blogcreate.save()
            return redirect('index')
    else:
        blogcreate=blogcform()
        return render(request,'sitewebapp/blogc.html',{'blogcreateform':blogcreate})

def logusr(request):
    return render(request,'sitewebapp/logusr.html')


def alumniadd(request):
    if request.method=="POST":
        e=Alumni.objects.all()
        if e:        
            no=e.count()
        else:
            no=0
        form=alumniform(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.sno=no
           ### print(f.firstname,f.lastname,f.batch,f.facebook_url,f.instagram_url)
            f.save()
            return redirect('../Alumni/')
    else:
        form=alumniform()
        return render(request,'sitewebapp/profile.html',{'form':form})


def view_alumni(request):
    alm=Alumni.objects.all().order_by('batch')
    o=[]
    j='2000'
    m=[]
    for i in alm:
        if i.batch!=j:
            j=i.batch
            m.append(j)
            o.append(i)
        else :
            o.append(i)
        
    return render(request,'sitewebapp/alumni.html',{'alm':o,'m':m})


def edit_profile(request,key,tok):
    print('c')
    token=access_tokens.objects.filter(value=tok)
    if token:
        if request.method=='POST':
            #inst= Members.objects.get(username=key)
            inst = get_object_or_404(Members,username=key)
            

            if (1):
                
                cform = MemberAddForm(request.POST, request.FILES,instance=inst)
                if cform.is_valid():
                    cform.save()
                    return redirect("/")
            else:
                return render(request,'sitewebapp/404.html',{})
        else:
            inst= Members.objects.get(username=key)
            data = {
                'username' : inst.username,
                'firstname' : inst.firstname, 
                'lastname' : inst.lastname,
                'email' : inst.email,
                'bio' :  inst.bio,
                'year' : inst.year,
                'post' : inst.post,
                'sno' : inst.sno,
                'dp' : inst.dp,
                'facebook_url' : inst.facebook_url, 
                'instagram_url' : inst.instagram_url, 
                'linkedin_url' : inst.linkedin_url,
                    }
            cform = MemberAddForm(data)
            return render(request, 'sitewebapp/editmember.html', {'cform':cform,'key':key,'tok':tok})
    else:
        return render(request,'sitewebapp/404.html',{})

def edit_home(request,key):
    if request.method=='GET':
        print('s')
        token=access_tokens.objects.filter(value=key)
        if token:

            return render(request,'sitewebapp/edithome.html',{'token':key})
        else:
            return render(request,'sitewebapp/404.html',{})