
from django.shortcuts import render,HttpResponseRedirect
from services.models import Services2,Register1
from .forms import Registration

def home(request):
    a = Services2.objects.all()
    return render(request,'index.html',{'d': a })

def about(request):
    
    ss=Services2.objects.all()
    return render(request,'about.html',{'ss':ss})

def contact(request):
    if request.method == 'POST':
        s= Registration(request.POST)
        if s.is_valid():
            r = s.cleaned_data['address']
            e = s.cleaned_data['email']
            b = s.cleaned_data['birth']
            a = Register1(address=r,email=e, birth=b)
            a.save()
        s = Registration()
    else:
        s = Registration()
    data=Register1.objects.all() 
    return render(request,'contact.html',{'fm':s,'d':data})



def delete(request,id):
    s= Register1.objects.get(pk=id)
    s.delete()
    return HttpResponseRedirect('contact/')

def update(request,id):
    if request.method == 'POST':
        s= Registration(request.POST)
        if s.is_valid():
            r = s.cleaned_data['address']
            e = s.cleaned_data['email']
            b = s.cleaned_data['birth']
            a = Register1(id=id,address=r,email=e, birth=b)
            a.save()
            s = Registration()
    else:
        s = Registration()
    return render(request,'update.html',{'fm':s})





def doctor(request):
    # d={

    #     'r1':{'name':'dr.nikita'},
    #     'r2':{'name':'dr.nima'},
    # }

    # if s==1:
    #     p=d['r1']['name']
    # elif s==2:
    #     p=d['r2']['name']

    return render(request,'doctor.html')

def testimonial(request):
    return render(request,'testimonial.html')

def treatment(request):
    return render(request,'treatment.html')