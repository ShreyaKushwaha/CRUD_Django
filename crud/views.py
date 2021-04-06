from django.shortcuts import render,redirect,HttpResponse
from crud.models import Detail
from django.contrib import messages



# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        pincode = request.POST.get('pincode')
        detail = Detail(name=name, email=email, phone=phone, dob=dob, pincode=pincode)
        if Detail.objects.filter(email=email):
           messages.warning(request, 'Email address already exists. Try again with other email address.')
        else:
            detail.save()
            messages.success(request, 'Details Submitted!')
        
    return render(request, 'index.html')

def read(request):
    query_results = Detail.objects.all()
    context = {'query_results':query_results}
    return render(request, 'read.html', context)


        

def update(request):
    if request.method == 'GET':
        if Detail.objects.filter(email=request.GET.get('email'))==False:
            messages.warning(request,"No such record exists in database.")
            return redirect("/update")
        
    return render(request, 'update.html')

    
    

def updateform(request):
    
    context = {'emailpara': request.GET.get('emailUpdate')}
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('emailpara')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        pincode = request.POST.get('pincode')
        detail = Detail(name=name,email=email, phone=phone, dob=dob, pincode=pincode)
        #Detail.objects.filter(email=request.GET.get('emailUpdate')).delete()
        detail.save()
        return redirect("/update", messages.success(request,"Record Updated!"))
        
    return render(request, 'updateform.html',context)

        
    
    
def delete(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if Detail.objects.filter(email=email):
            Detail.objects.filter(email=email).delete()
            messages.success(request,"Record Deleted!")
        else:
            messages.warning(request, "No such record exists in database.")
        
    return render(request, 'delete.html')
