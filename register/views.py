
from django.shortcuts import render, HttpResponseRedirect
from .forms import Registrationform
from .models import User


# Create your views here.
def addata(request):
    if request.method == 'POST':
        lm = Registrationform(request.POST)
        if lm.is_valid():
            fm=lm.cleaned_data['firstname']
            sm=lm.cleaned_data['lastname']
            am=lm.cleaned_data['address']
            pm=lm.cleaned_data['phone']
            em=lm.cleaned_data['email']
            vm=lm.cleaned_data['password']
            reg=User(firstname=fm,lastname=sm,address=am,phone=pm,email=em,password=vm)
            reg.save()
            lm=Registrationform()
    
    else:
        lm=Registrationform()
    stud=User.objects.all()
    return render(request, 'register/addandshow.html',{'form':lm,'stu':stud})

def updatedata(request, id):
    if request.method == 'POST':
        op=User.objects.get(pk=id)
        lm=Registrationform(request.POST, instance=op)
        if lm.is_valid():
            lm.save()
    else:
        op = User.objects.get(pk=id)
        lm = Registrationform(instance=op)
    return render(request, 'register/updatestudent.html',{'form':lm})



def deletedata(request,id):
    if request.method=='POST':
        op=User.objects.get(pk=id)
        op.delete()
        return HttpResponseRedirect('/')    

def showdata(request):
    lm=Registrationform()
    stud=User.objects.all()
    return render(request, 'register/showall.html',{'form':lm,'stu':stud})
    #return render(request, 'register/showall.html')
    