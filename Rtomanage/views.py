from django.shortcuts import render,redirect
from Rtomanagement.models import rtouser,Learners,licence,Vehi_Reg,NOC,Hazmate,Ownership_transfer,Payment,International_dl,Test_date,PSV_Badge
from django.contrib import messages

# Create your views here.


def get_users(request):
    data=rtouser.objects.all()
    return render(request,'table-data-users.html',{'data':data})

def approveuser(request, cr_id):     
        cr = rtouser.objects.get(id=cr_id)
        cr.user_status =  1  
        cr.save()
        return redirect('getusers')

def rejectuser(request,cr_id):
     item =rtouser.objects.get(id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('getusers')   

def admin_dashboard(request):
    return render(request,'dashboard.html')


def manage_learners_license(request):
    data=Learners.objects.all()
    return render (request,'table-data-learners.html',{'data':data})


def approvelearners(request, cr_id):     
        cr = Learners.objects.get(user_id=cr_id)
        cr.learners_status =  1  
        cr.save()
        return redirect('managelearnerslicense')

def rejectlearners(request,cr_id):
     item =Learners.objects.get(user_id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('managelearnerslicense')   

def manage_license(request):
    data=licence.objects.all()
    return render (request,'table-data-licence.html',{'data':data})


def approvelicense(request, cr_id):     
        cr = licence.objects.get(user_id=cr_id)
        cr.licence_status =  1  
        cr.save()
        return redirect('managelicense')

def rejectlicence(request,cr_id):
     item =licence.objects.get(user_id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('managelicense')   


def manage_renew_license(request):
    data=licence.objects.all()
    return render (request,'table-data-renewlicence.html',{'data':data})

def approverenewlicense(request, cr_id):     
        cr = licence.objects.get(user_id=cr_id)
        cr.licence_status =  1  
        cr.save()
        return redirect('managerenewlicense')

def rejectrenewlicence(request,cr_id):
     item =licence.objects.get(user_id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('managerenewlicense')   


def manage_duplicate_license(request):
    data=licence.objects.all()
    return render (request,'table-data-duplicate.html',{'data':data})


def approveduplicatelicense(request, cr_id):     
        cr = licence.objects.get(user_id=cr_id)
        cr.licence_status =  1  
        cr.save()
        return redirect('manageduplicatelicense')

def rejectduplicatelicence(request,cr_id):
     item =licence.objects.get(user_id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('manageduplicatelicense')   



def manage_hazmate(request):
    data=Hazmate.objects.all()
    return render (request,'table-data-hazmate.html',{'data':data})


def approvehazmate(request, cr_id):     
        cr = Hazmate.objects.get(user_id=cr_id)
        cr.hazmate_status =  1  
        cr.save()
        return redirect('managehazmate')

def rejecthazmate(request,cr_id):
     item =Hazmate.objects.get(user_id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('managehazmate') 


def manage_international_license(request):
    data=International_dl.objects.all()
    return render (request,'table-data-international_licence.html',{'data':data})


def approveinternationalLicence(request, cr_id):     
        cr = International_dl.objects.get(user_id=cr_id)
        cr.inter_dl_status =  1  
        cr.save()
        return redirect('manageinternationallicense')

def rejectinternationalLicence(request,cr_id):
     item =International_dl.objects.get(user_id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('manageinternationallicense') 

def manage_psvBadge(request):
    data=PSV_Badge.objects.all()
    return render (request,'table-data-psv.html',{'data':data})

def approvepsv(request, cr_id):     
        cr = PSV_Badge.objects.get(user_id=cr_id)
        cr.psv_status =  1  
        cr.save()
        return redirect('managepsvBadge')

def rejectpsv(request,cr_id):
     item =PSV_Badge.objects.get(user_id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('managepsvBadge') 


def manage_noc(request):
    data=NOC.objects.all()
    return render (request,'table-data-noc.html',{'data':data})

def approvenoc(request, cr_id):     
        cr = NOC.objects.get(user_id=cr_id)
        cr.noc_status =  1  
        cr.save()
        return redirect('managenoc')

def rejectnoc(request,cr_id):
     item =NOC.objects.get(user_id=cr_id) 
     item.noc_status =  2  
     item.save()
     messages.info(request,'Rejected')
     return redirect('managenoc')   


def manage_noc_cancellation(request):
    data=NOC.objects.all()
    return render (request,'table-data-cancelnoc.html',{'data':data})

def new_vehicle_register(request):
    data=Vehi_Reg.objects.all()
    return render (request,'table-data-vehicle_reg.html',{'data':data})

def vehicle_ownership_status(request):
    data=Ownership_transfer.objects.all()
    return render (request,'table-data-ownership_transfer.html',{'data':data})


def approveownership(request, cr_id):     
        cr = Ownership_transfer.objects.get(user_id=cr_id)
        cr.vehi_newreg_status =  1  
        cr.save()
        return redirect('vehicleownershipstatus')

def rejectownership(request,cr_id):
     item =Ownership_transfer.objects.get(user_id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('vehicleownershipstatus')   

def update_license_data(request):
    return render (request,'table-data-update_dl.html')
def test_date(request):
    return render (request,'table-data-add_testdate.html')

def view_payment(request):
    data = Payment.objects.all()
    return render (request,'table-data-payment.html',{'data':data})


def approvepayment(request, cr_id):     
        cr = Payment.objects.get(userreg_id=cr_id)
        cr.payment_status =  1  
        cr.save()
        return redirect('viewpayment')

def rejectpayment(request,cr_id):
     item =Payment.objects.get(userreg_id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('viewpayment')

def view_report(request):
    return render (request,'table-data-report.html')

def view_test_date(request):
     data=Test_date.objects.all()
     return render (request,'table-data-view-testdate.html',{'data':data})

def create_test_date(request):
     if request.method == 'POST':
        fullname= request.POST.get('fullname') 
        Licence_type= request.POST.get('licence_type') 
        date= request.POST.get('date')

        data = Test_date(Test_date=date,name=fullname,Licence_type=Licence_type,test_status=0)
        data.save()
        return redirect('viewtestdate')