from django.shortcuts import render, redirect, get_object_or_404, reverse, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, JsonResponse
from .models import *
from django.db.models import Count
from .forms import CommentForm, MemberAddForm, blogcform
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
                if request.user.is_authenticated :    #onlu logged in users can comment
                    new_comment.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    return redirect('')
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
@user_passes_test(lambda u: u.is_superuser)   
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
            return HttpResponse("Firse bharna parega Error hai, back Jake dekhiye Kya error hai (Go back and check again plz)")
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

#audis------------------------------------------------------------------------------

@never_cache
def audition(request):
    if request.user.is_authenticated:
        cand = request.user
        round_no = auditionRounds.objects.filter(round_status=True)
        try:
            cand = Candidates.objects.get(email=cand.email)
        except Candidates.DoesNotExist:
            user = Candidates()
            user.name = cand.first_name + " " + cand.last_name
            user.email = cand.email
            if round_no[0].roundno == 0:
                user.status = 'Selected'
                user.save() 
            else:
                user.status = 'Rejected'
                user.save() 
        cand = Candidates.objects.get(email=cand.email)
        cand_status = cand.status
        print(cand_status)
        ques = auditionQuestions.objects.filter(roundno = round_no[0].roundno)
        attempt = auditionAnswers.objects.filter(roundno = round_no[0].roundno, ansby=cand)
        print(ques)
        if not ques:
            btn_status = False
        else:
            can = Candidates.objects.filter(status="Selected", email=cand.email)
            print(attempt)
            if can:
                if not attempt: 
                    btn_status = True
                else:
                    btn_status = False
            else:
                btn_status = False   
        if not attempt: 
            attempt = False
        else:
            attempt = True  
        if round_no[0].roundno == 0:
            cands = None
        else:
            cands = Candidates.objects.filter(status='Selected').order_by('-name')
        return render(request, 'sitewebapp/auditionHome.html',{'status':cand_status, 'round_no':round_no[0].roundno,'btn_status': btn_status, 'cands': cands, 'attempt': attempt})
    else:
        return render(request, 'sitewebapp/audition.html')

@login_required
def auditionhome(request):
    return audition(request)

@login_required
def auditionform(request):
    cand = request.user
    cand = Candidates.objects.get(email=cand.email)
    round_no = auditionRounds.objects.filter(round_status=True)
    ques = auditionQuestions.objects.filter(roundno = round_no[0].roundno)
    solved = auditionAnswers.objects.filter(roundno = round_no[0].roundno, ansby=cand)
    if cand.status == "Rejected" or cand.status == "Pending":
        print(cand.status)
        return HttpResponseRedirect("/Audition/")
    if solved:
        print(solved)
        return HttpResponseRedirect("/Audition/")
    if request.method == 'POST':
        if solved:
            return HttpResponseRedirect("/Audition/")
        for q in ques:
            ans = request.POST.get(str(q.serialno))
            answer = auditionAnswers()
            answer.q = q
            answer.ans = ans
            answer.ansby = cand
            answer.roundno = round_no[0].roundno
            answer.anstime = datetime.now()
            answer.save()
            answer = auditionAnswers()
        cand.status = 'Pending'
        cand.save()
        return HttpResponseRedirect("/Audition/")
    else:
        answer = auditionAnswers()
        return render(request,'sitewebapp/auditionForm.html', {'round_no': round_no[0].roundno, 'ques': ques})
    return render(request, 'sitewebapp/auditionForm.html', {'round_no': round_no[0].roundno, 'ques': ques})

@user_passes_test(lambda u: u.is_superuser)
def showdata(request, email):
    cand = Candidates.objects.get(email=email)
    answers = auditionAnswers.objects.filter(ansby=cand)
    return render(request, 'sitewebapp/showdata.html', {'answers': answers})

@user_passes_test(lambda u: u.is_superuser)
def selectedCandidates(request):
    response = HttpResponse(content_type = 'text/csv')


    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Phone', 'Status'])

    for Candidate in Candidates.objects.filter(status='Selected').values_list('name', 'email', 'phone', 'status'):
        writer.writerow(Candidate)
    
    response['Content-Disposition'] = 'attachment; filename = "Selected.csv"'

    return response

@user_passes_test(lambda u: u.is_superuser)
def responses(request):
    response = HttpResponse(content_type = 'text/csv')


    writer = csv.writer(response)
    
    cands =Candidates.objects.all()

    for cand in cands:
        writer.writerow((cand.name, cand.email))
        for ans in auditionAnswers.objects.filter(ansby=cand):
            rnd = ans.q.roundno 
            no = ans.q.serialno
            ques = ans.q.question
            givenAns = ans.ans
            time = ans.anstime
            row1 = ('Questions:' ,rnd,no,ques)
            row2 = ('Answer:','',time, givenAns)
            writer.writerow(row1)
            writer.writerow(row2)
            writer.writerow([]) 
        writer.writerow([]) 
        writer.writerow([]) 
        writer.writerow([]) 

            
    
    response['Content-Disposition'] = 'attachment; filename = "Responses.csv"'

    return response


#@never_cache
