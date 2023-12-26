from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import usersForm
from members.models import AdmissionForm,User,Admin,LandOwner,LandPlot,LandTransaction,LandValuation,LandTenure,Infrastructure
from django.template import loader
from members.models import TransactionType,TenureType,InfrastructureType
from datetime import date, timedelta
from django.db.models import Q


def enterform(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        dob = request.POST.get('DOB')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        save=AdmissionForm(first_name=firstname,last_name=lastname,birth_date=dob,city=city,phone_number=phone,email=email)
        save.save()
    return render(request, 'enterform.html')  

def enteradmin(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        save=Admin(first_name=firstname,last_name=lastname)
        save.save()
        return redirect('getadmin')
    return render(request, 'enteradmin.html') 

def enterinfra(request):
    if request.method == 'POST':
        infrastructure_type_str = request.POST.get('infrastructure_type')
        plot_id = request.POST.get('plot')
        infrastructure_name = request.POST.get('infrastructure_name')

        plot_instance = LandPlot.objects.get(plot_id=plot_id)

        Infrastructure.objects.create(infrastructure_type=infrastructure_type_str,plot=plot_instance,infrastructure_name=infrastructure_name)
        return redirect('getinfra') 
    plots = LandPlot.objects.all()
    return render(request, 'enterinfra.html', {'plots': plots,'infraTypes': [[infraType.name, infraType.value] for infraType in InfrastructureType]})

def entervalue(request):
    if request.method == 'POST':
        plot_id = request.POST.get('plot')
        valuation_amount = request.POST.get('valuation_amount')
        valuation_date = request.POST.get('valuation_date')
        market_value = request.POST.get('market_value')

        plot_instance = LandPlot.objects.get(plot_id=plot_id)

        LandValuation.objects.create(
            plot=plot_instance,valuation_amount=valuation_amount,valuation_date=valuation_date,market_value=market_value)
        return redirect('getvalue')  

    plots = LandPlot.objects.all()
    return render(request, 'entervalue.html', {'plots': plots})

def entertenure(request):
    if request.method == 'POST':
        plot_id = request.POST.get('plot')
        tenure_type_str = request.POST.get('tenure_type')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        plot_instance = LandPlot.objects.get(plot_id=plot_id)

        LandTenure.objects.create(
            plot=plot_instance,
            tenure_type=tenure_type_str,
            start_date=start_date,
            end_date=end_date
        )
        return redirect('gettenure') 
    plots = LandPlot.objects.all()
    return render(request, 'entertenure.html', {'plots': plots,'tenureTypes': [[tenureType.name, tenureType.value] for tenureType in TenureType]})

def enterowner(request):
    if request.method == 'POST':
        owner_name = request.POST.get('owner_name')
        phone_number = request.POST.get('phone_number')
        date_of_birth = request.POST.get('date_of_birth')
        save=LandOwner(owner_name=owner_name,phone_number=phone_number,date_of_birth=date_of_birth)
        save.save()
        return redirect('getowner')
    return render(request, 'enterowner.html') 

def enteruser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        location = request.POST.get('location')
        admin_id = request.POST.get('admin_id')
        owner_id = request.POST.get('owner_id')
        province = request.POST.get('province')
        city = request.POST.get('city')
    
        user_instance = User(username=username, password=password, location=f'{province}, {city}, {location}')
        
        if admin_id:
            try:
                admin_instance = Admin.objects.get(pk=admin_id)
                user_instance.admin = admin_instance
            except Admin.DoesNotExist:
                pass
        if owner_id:
            try:
                owner_instance = LandOwner.objects.get(pk=owner_id)
                user_instance.owner = owner_instance
            except LandOwner.DoesNotExist:
                pass
        
        user_instance.save()

        return redirect('getuser') 

    return render(request, 'enteruser.html')

def entertrans(request):
    if request.method == 'POST':
        transaction_type_str = request.POST.get('transaction_type')
        plot_id = request.POST.get('plot')
        transaction_date = request.POST.get('transaction_date')
        plot_instance = LandPlot.objects.get(plot_id=plot_id)

        LandTransaction.objects.create(
            transaction_type=transaction_type_str,  
            plot=plot_instance,
            transaction_date=transaction_date
        )
        return redirect('gettrans') 

    plots = LandPlot.objects.all()
    return render(request, 'entertrans.html', {'plots': plots, 'transTypes': [[transactionType.name, transactionType.value] for transactionType in TransactionType]})


def enterplot(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        area = request.POST.get('area')
        owner_id = request.POST.get('ownerid')
        owner = LandOwner.objects.get(owner_id=owner_id)
        province = request.POST.get('province')
        city = request.POST.get('city')

        LandPlot.objects.create(
            location=f'{province}, {city}, {location}',
            area=area,
            ownerid=owner
        )

        return redirect('getplot')  

    owners = LandOwner.objects.all()
    return render(request, 'enterplot.html', {'owners': owners})

def getplot(request):
    plot_list = LandPlot.objects.all()
    return render(request, 'getplot.html', {'plot_list': plot_list})

def getuser(request):
    user_list = User.objects.all()
    return render(request, 'getuser.html', {'user_list': user_list})

def gettrans(request):
    trans_list = LandTransaction.objects.all()
    return render(request, 'gettrans.html', {'trans_list': trans_list})

def gettenure(request):
    tenure_list = LandTenure.objects.all()
    return render(request, 'gettenure.html', {'tenure_list': tenure_list})

def getadmin(request):
    admin_instance = Admin.objects.all().order_by('admin_id').select_related('user')
    template = loader.get_template('getadmin.html')
    context = {'admin':admin_instance}
    return HttpResponse(template.render(context, request))

def getowner(request):
    owner_instance = LandOwner.objects.all().order_by('owner_id').select_related('user')
    template = loader.get_template('getowner.html')
    context = {'owner':owner_instance}
    return HttpResponse(template.render(context, request))

def getvalue(request):
    value_list = LandValuation.objects.all()
    return render(request, 'getvalue.html', {'value_list': value_list})

def getform(request):
    allforms = AdmissionForm.objects.all().order_by('first_name').values()
    template = loader.get_template('getform.html')
    context = {'myform':allforms,}
    return HttpResponse(template.render(context, request))

def getinfra(request):
    infrastructure_list = Infrastructure.objects.all()
    return render(request, 'getinfra.html', {'infrastructure_list': infrastructure_list})

def updateuser(request, user_id):
    user = User.objects.get(user_id=user_id)
    return render(request,'updateuser.html',{'user':user})

def updateinfra(request, infrastructure_id):
    infra = Infrastructure.objects.get(infrastructure_id=infrastructure_id)
    return render(request,'updatedinfra.html',{'infra':infra})

def updatetenure(request, tenure_id):
    tenure = LandTenure.objects.get(tenure_id=tenure_id)
    return render(request,'updatetenure.html',{'tenure':tenure})

def updateadmin(request, admin_id):
    admin = Admin.objects.get(admin_id=admin_id)
    return render(request,'updateadmin.html',{'admin':admin})

def updateowner(request, owner_id):
    owner = LandOwner.objects.get(owner_id=owner_id)
    return render(request,'updatedowner.html',{'owner':owner})

def updatetrans(request, transaction_id):
    trans = LandTransaction.objects.get(transaction_id=transaction_id)
    return render(request,'updatetrans.html',{'trans':trans})

def updateplot(request, plot_id):
    plot = LandPlot.objects.get(plot_id=plot_id)
    return render(request,'updateplot.html',{'plot':plot})

def updatevalue(request, valuation_id):
    value = LandValuation.objects.get(valuation_id=valuation_id)
    return render(request,'updatevalue.html',{'value':value})

def updated(request, user_id):
    x=request.POST['username']
    z=request.POST['password']
    w = request.POST['location']
    p = request.POST.get('province')
    c = request.POST.get('city')
    user = User.objects.get(user_id=user_id)
    y = f'{p}, {c}, {w}'
    user.location = y
    user.username=x
    user.password=z
    user.save()
    return redirect("getuser")


def updatedplot(request, plot_id):
    x = request.POST['location']
    p = request.POST.get('province')
    c = request.POST.get('city')
    y = request.POST['area']
    plot = LandPlot.objects.get(plot_id=plot_id)
    x = f'{p}, {c}, {x}'
    plot.location = x
    plot.area = y
    plot.save()
    return redirect("getplot")


def updatedadmin(request, admin_id):
    a=request.POST['first_name']
    b=request.POST['last_name']
    admin = Admin.objects.get(admin_id=admin_id)
    admin.first_name=a
    admin.last_name=b
    admin.save()
    return redirect("getadmin")

def updatedowner(request, owner_id):
    a=request.POST['owner_name']
    b=request.POST['phone_number']
    c=request.POST['date_of_birth']
    owner = LandOwner.objects.get(owner_id=owner_id)
    owner.owner_name=a
    owner.phone_number=b
    owner.date_of_birth=c
    owner.save()
    return redirect("getowner")

def updatedinfra(request, infrastructure_id):
    y=request.POST['infrastructure_name']
    x=request.POST['infrastructure_type']
    infra = Infrastructure.objects.get(infrastructure_id=infrastructure_id)
    infra.infrastructure_name=y
    infra.infrastructure_type=x
    infra.save()
    return redirect("getinfra")

def updatedtenure(request, tenure_id):
    x=request.POST['tenure_type']
    y=request.POST['start_date']
    z=request.POST['end_date']
    tenure = LandTenure.objects.get(tenure_id=tenure_id)
    tenure.tenure_type=x
    tenure.start_date=y
    tenure.end_date=z
    tenure.save()
    return redirect("gettenure")

def updatedtrans(request, transaction_id):
    x=request.POST['transaction_type']
    y=request.POST['transaction_date']
    trans = LandTransaction.objects.get(transaction_id=transaction_id)
    trans.transaction_type=x
    trans.transaction_date=y
    trans.save()
    return redirect("gettrans")

def updatedvalue(request, valuation_id):
    x=request.POST['valuation_amount']
    y=request.POST['valuation_date']
    z=request.POST['market_value']
    value = LandValuation.objects.get(valuation_id=valuation_id)
    value.valuation_amount=x
    value.valuation_date=y
    value.market_value=z
    value.save()
    return redirect("getvalue")

def deluser(request, user_id):
    user = User.objects.get(user_id=user_id)
    user.delete() 
    return redirect('getuser') 

def deladmin(request, admin_id):
    admin = Admin.objects.get(admin_id=admin_id)
    admin.delete() 
    return redirect('getadmin') 

def delowner(request, owner_id):
    owner = LandOwner.objects.get(owner_id=owner_id)
    owner.delete() 
    return redirect('getowner') 

def delinfra(request,infrastructure_id):
    infra = Infrastructure.objects.get(infrastructure_id=infrastructure_id)
    infra.delete() 
    return redirect('getinfra') 

def deltenure(request,tenure_id):
    tenure = LandTenure.objects.get(tenure_id=tenure_id)
    tenure.delete() 
    return redirect('gettenure') 

def deltrans(request,transaction_id):
    trans = LandTransaction.objects.get(transaction_id=transaction_id)
    trans.delete() 
    return redirect('gettrans') 

def delplot(request,plot_id):
    plot = LandPlot.objects.get(plot_id=plot_id)
    plot.delete() 
    return redirect('getplot')

def delvalue(request,valuation_id):
    value = LandValuation.objects.get(valuation_id=valuation_id)
    value.delete() 
    return redirect('getvalue')

def ownerid(request, owner_id):
    owner = get_object_or_404(LandOwner, owner_id=owner_id)
    return render(request, 'getowner.html', {'owner': [owner]})

def adminid(request, admin_id):
    admin = get_object_or_404(Admin, admin_id=admin_id)
    return render(request, 'getadmin.html', {'admin': [admin]})

def userid(request, user_id):
    user = get_object_or_404(User, user_id=user_id)
    return render(request, 'getuser.html', {'user_list': [user]})

def tenureid(request, tenure_id):
    tenure = get_object_or_404(LandTenure, tenure_id=tenure_id)
    return render(request, 'gettenure.html', {'tenure_list': [tenure]})

def plotid(request, plot_id):
    plot = get_object_or_404(LandPlot, plot_id=plot_id)
    return render(request, 'getplot.html', {'plot_list': [plot]})

def transid(request, transaction_id):
    trans = get_object_or_404(LandTransaction, transaction_id=transaction_id)
    return render(request, 'gettrans.html', {'trans_list': [trans]})

def valueid(request, valuation_id):
    value = get_object_or_404(LandValuation, valuation_id=valuation_id)
    return render(request, 'getvalue.html', {'value_list': [value]})

def infraid(request, infrastructure_id):
    infra = get_object_or_404(Infrastructure, infrastructure_id=infrastructure_id)
    return render(request, 'getinfra.html', {'infrastructure_list': [infra]})

def ownerdob(request, age):
    birthdate_limit = date.today() - timedelta(days=365 * age)
    owners_above_age = LandOwner.objects.filter(date_of_birth__lte=birthdate_limit)
    owner_names = [owner.owner_name for owner in owners_above_age]
    return render(request, 'dob.html', {'owner_names': owner_names, 'age': age})

def filterplot(request):
    keyword = request.GET.get('keyword', '')
    if keyword:
        plots = LandPlot.objects.filter(
            Q(location__icontains=keyword) |
            Q(area__icontains=keyword)
        ).select_related('ownerid')
    else:
        plots = LandPlot.objects.all().select_related('ownerid')
    return render(request, 'filterplots.html', {'plots': plots, 'keyword': keyword})

def filtervalue(request):
    min_valuation = request.GET.get('min_valuation', 0)
    max_valuation = request.GET.get('max_valuation', 200000)
    valuations = LandValuation.objects.filter(
        valuation_amount__gte=min_valuation,
        valuation_amount__lte=max_valuation
    )
    return render(request, 'filtervalue.html', {'valuations': valuations, 'min_valuation': min_valuation, 'max_valuation': max_valuation})

def filtertrans(request):
    keyword = request.GET.get('keyword', '')
    if keyword:
        transactions = LandTransaction.objects.filter(
            Q(transaction_type__icontains=keyword) 
        ).select_related('plot')
    else:
        transactions = LandTransaction.objects.all().select_related('plot')
    return render(request, 'filtertrans.html', {'transactions': transactions, 'keyword': keyword})

def filtertenure(request):
    keyword = request.GET.get('keyword', '')
    if keyword:
        tenures = LandTenure.objects.filter(
            Q(tenure_type__icontains=keyword) |
            Q(plot__location__icontains=keyword)
        ).select_related('plot')
    else:
        tenures = LandTenure.objects.all().select_related('plot')
    return render(request, 'filtertenure.html', {'tenures': tenures, 'keyword': keyword})

def filterinfra(request):
    keyword = request.GET.get('keyword', '')
    if keyword:
        infrastructures = Infrastructure.objects.filter(
            Q(infrastructure_type__icontains=keyword) |
            Q(infrastructure_name__icontains=keyword) |
            Q(plot__location__icontains=keyword)
        ).select_related('plot')
    else:
        infrastructures = Infrastructure.objects.all().select_related('plot')
    return render(request, 'filterinfra.html', {'infrastructures': infrastructures, 'keyword': keyword})

def index(request):
    return render(request, 'index.html')