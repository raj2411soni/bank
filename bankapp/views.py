from django.shortcuts import render,redirect
from django.http import HttpResponse
from bankapp.models import customer, history
# Create your views here.

def f(request):
    return render(request,"home.html")

def cus(request):
    cs = customer.objects.all()
    d={
        "one":cs
    }
    return render(request,'customers.html',d)

def tran(request,t_id):
    error = False
    abc=customer.objects.get(id=t_id)
    abcd=customer.objects.all()
    if request.method=="POST":
        data=request.POST
        f=abc.name
        print(f)
        #sname=data["sName"]
        tid=data['rname']
        rname=customer.objects.get(id=tid)
        print(rname)

        #rname=data["rname"]
        sbal=data["Balance"]
        bal=abc.balance

        if bal < (int(sbal)): 
            error = True
        else:
            abc.balance -= (int(sbal))
            abc.save()
            rname.balance = rname.balance +(int(sbal))
            rname.save()
            history.objects.create(sender=f,receiver=rname,transfer=sbal)
            return redirect("home")
    d={
        "t":abc,
        "r":abcd, 
        "error":error
    }
    return render(request,"transfer.html",d)

def make(request):
    al=customer.objects.all()

    d={
        "ones":al
    }
    return render(request,"maketransaction.html",d)

def hist(request):
    a=history.objects.all()
    d={
        "a":a
    }
    return render(request,"history.html",d)