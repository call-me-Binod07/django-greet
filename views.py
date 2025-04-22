from django.shortcuts import render
from datetime import datetime
# Create your views here.

def greet(request):
    date=datetime.now()
    # print(date)
    msg='hello brother! whats up !!  i wish you a very Good  '
    h=int(date.strftime("%H"))

    if h<12:
        msg+= "Morning ! ❤️‍🩹"
    elif h<16:
        msg+= "AfterNoon ! 🦋"
    else:
        msg+= "Eveneing ! 🙃"

    return render(request,'greet.html',{"data":msg,"date":date})