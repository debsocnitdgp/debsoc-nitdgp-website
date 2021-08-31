from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from oud.models import *
import razorpay

# Create your views here.


def oud_register(request):
    if request.method == 'POST':
        if 'participant' in request.POST:
            participant = Participant()
            participant.username = request.POST.get('username', default='participant')
            participant.email = request.POST.get('email')
            participant.phone_no = request.POST.get('phone_no')
            participant.college = request.POST.get('college')
            participant.college_year = request.POST.get('college_year')
            participant.discord_id = request.POST.get('discord_id')
            participant.prior = request.POST.get('prior')
            if(request.FILES['ss'] is not None):
                participant.cv = request.FILES['cv']
                participant.is_adj = True
            participant.ss = request.FILES['ss']
            # client=razorpay.Client(auth=("rzp_test_KblRM8ffzJ6tB2","i0dm023uPO2EeoCe8Aeqfolq"))
            # order_amount = 100 * 100
            # order_currency = 'INR'
            # payment = client.order.create({'amount':order_amount, 'currency':order_currency, 'payment_capture':'1' })
            # participant.payment_id= payment['id']
            participant.save()
            # return render(request, 'oud/register.html',{'payment':payment, 'order_amount':order_amount})
            return render(request, 'oud/success.html')

    return render(request, 'oud/register.html')

# @csrf_exempt
# def success(request):
#     if(request.method=="POST"):
#         a=request.POST
#         order_id=""
#         for key , val in a.items():
#             if key=='razorpay_order_id':
#                 order_id=val
#                 break
#         participant = Participant.objects.get(payment_id=order_id)
#         participant.is_paid=True
#         participant.save()

#     return render(request, 'oud/success.html')