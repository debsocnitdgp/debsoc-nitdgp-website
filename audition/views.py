from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, JsonResponse
from .models import *
from django.db.models import Count
from django.utils import timezone
from django.views.decorators.cache import cache_control, never_cache
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from datetime import datetime
from django.http import HttpResponseRedirect
import csv

# Create your views here.





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
