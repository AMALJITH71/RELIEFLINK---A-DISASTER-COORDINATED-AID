import datetime
import random

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from Relieflink_apk.models import *


# def log(request):
#     return HttpResponse("ok")
# def register(request):
#     return render(request,'volunteer/volunteerregister.html')
#
# def register_post(request):
#     name1 = request.POST['name']
#     age1 = request.POST['Age']
#     gender1 = request.POST['Gender']
#     place1 = request.POST['place']
#     pin1 = request.POST['pin']
#     post1 = request.POST['Post']
#     image1 = request.FILES['Image']
#     id_proof1 = request.FILES['Id_proof']
#     skill1 = request.POST['Skill']
#     contact_no1 = request.POST['Contact_no']
#     email1 = request.POST['Email']
#     password1 = request.POST['password']
#     confirm_password1 = request.POST['confirm_password']
#     d=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
#     fs=FileSystemStorage()
#     fs.save(r"C:\Users\AMALJITH PRAKASH\PycharmProjects\relieflink\Relieflink_apk\static\images\\"+d+'.jpg',image1)
#     path='/static/images/'+d+'.jpg'
#     fs.save(r"C:\Users\AMALJITH PRAKASH\PycharmProjects\relieflink\Relieflink_apk\static\id_proof\\" + d + '.pdf', id_proof1)
#     path1 = '/static/id_proof/' + d + '.pdf'
#
#     if password1==confirm_password1:
#         ob = login()
#         ob.username = email1
#         ob.password = password1
#         ob.usertype="volunteer"
#         ob.save()
#
#
#         obj = volunteer()
#         obj.Name = name1
#         obj.Age = age1
#         obj.Gender = gender1
#         obj.Place= place1
#         obj.pin = pin1
#         obj.post = post1
#         obj.Image = path
#         obj.Id_proof = path1
#         obj.Skill = skill1
#         obj.Contact_no = contact_no1
#         obj.Email = email1
#         obj.LOGIN=ob
#         obj.CAMP_id=1
#         obj.save()
#         return HttpResponse("<script>alert('register successfully')window.location='/'</script>")
#
#
# #######################################################
#
# def donation_add(request):
#     return render(request,'donation/Donation.html')
#
# def donation_post(request):
#     account_no1 = request.POST['account_no']
#     amount1 = request.POST['amount']
#     date1 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
#
#     obj1 = donation()
#     obj1.Account_no = account_no1
#     obj1.Amount = amount1
#     obj1.Transaction_id = random.randint(000000,999999)
#     obj1.date = date1
#     obj1.save()
#     return HttpResponse("Payment Accepted")
#
# def home(request):
#     return render(request,'home.html')


#####################################################################

# def Login_page(request):
#     return render(request,'login/login.html')
#
# def login_post(request):
#     username1 = request.POST['Username']
#     password1 = request.POST['Password']
#     res=login.objects.filter(username=username1,password=password1)
#     if res.exists():
#         res=res[0]
#         if res.usertype=="admin":
#
#
#     return HttpResponse("login succesfull")
#


#######################################################admion#####################################################

# def log(request):
#     return render(request, 'admin/Admin_login.html')
def index(request):
    return render(request, 'index.html')
def loginpage(request):
    return render(request, 'admin/Admin_login.html')

def login_buttonclick(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    res = login.objects.filter(username=username, password=password)
    if res.exists():
         res=res[0]
         if res.usertype=="admin":
             request.session['lid']=res.id
             return redirect("/adminlanding")
         elif res.usertype == "camp":
             request.session['lid'] = res.id
             data = camp.objects.get(LOGIN=request.session['lid'])
             request.session['cid'] = data.id
             return redirect("/coordinator_home")

         elif res.usertype == "volunteer":
             request.session['lid'] = res.id
             data = volunteer.objects.get(LOGIN=request.session['lid'])
             request.session['vid'] = data.id
             return redirect("/volunteer_home")

         elif res.usertype == "user":
             request.session['lid'] = res.id
             data = volunteer.objects.get(LOGIN=request.session['lid'])
             request.session['uid'] = data.id
             return redirect("/user_home")
         else:
             return HttpResponse("<script>alert('please wait');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('not found');window.location='/'</script>")


def addcamp(request):
    return render(request, 'admin/add_camp.html')


def addcamp_registerbuttonclick(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    pin = request.POST['textfield3']
    post = request.POST['textfield4']
    coordinator = request.POST['textfield9']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']
    latitude = request.POST['textfield7']
    longitude = request.POST['textfield8']

    qry =login()
    qry.username = email
    qry.password = random.randint(0000, 9999)
    qry.usertype = 'camp'
    qry.save()

    obj = camp()
    obj.LOGIN =qry
    obj.camp_name = name
    obj.place = place
    obj.pin = pin
    obj.post = post
    obj.Coordinator_name = coordinator
    obj.Contact_no = phone
    obj.Email = email
    obj.Latitude=latitude
    obj.Longitude=longitude
    obj.save()

    return HttpResponse("<script>alert('added successfully');window.location='/viewcamp'</script>")


def updatecamp(request,id):
    view=camp.objects.get(id=id)

    return render(request, 'admin/Update_camp.html',{"data":view})


def updatecamp_updatebuttonclick(request,id):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    pin = request.POST['textfield3']
    post = request.POST['textfield4']
    coordinator = request.POST['coordinator']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']
    latitude = request.POST['textfield7']
    longitude = request.POST['textfield8']

    camp.objects.filter(id=id).update(camp_name=name,place=place,pin=pin,post=post,Coordinator_name=coordinator,Contact_no=phone,Email=email,Latitude=latitude,Longitude=longitude)
    return HttpResponse("<script>alert('updated successfully');window.location='/viewcamp'</script>")


def viewcamp(request):
    res = camp.objects.all()
    return render(request, 'admin/View_camp.html', {'data': res})

def delete_camp(request,id):
    login.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/viewcamp'</script>")


def viewvolunteer(request):
    res = volunteer.objects.all()
    return render(request, 'admin/View_volunteer.html', {'data': res})



def viewuser(request):
    return render(request, 'admin/View_user.html')


def addhospital(request):
    return render(request, 'admin/Add_hospital.html')

def viewhospital(request):
    res = hospital.objects.all()
    return render(request, 'admin/view_hospital.html',{'data': res})

def delete_hospital(request, id):
    hospital.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/viewhospital'</script>")



def addhospital_registerbuttonclick(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    pin = request.POST['textfield3']
    post = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']
    latitude = request.POST['textfield7']
    longitude = request.POST['textfield8']

    obj = hospital()
    obj.Name = name
    obj.Place = place
    obj.Pin = pin
    obj.Post = post
    obj.Phone = phone
    obj.Email = email
    obj.Latitude = latitude
    obj.longitude = longitude
    obj.save()

    return HttpResponse("<script>alert('added successfully');window.location='/viewhospital'</script>")


def updatehospital(request,id):
    view = hospital.objects.get(id=id)
    return render(request, 'admin/Update_hospital.html',{"data":view})


def updatehospital_updatebuttonclick(request,id):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    pin = request.POST['textfield3']
    post = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']
    latitude = request.POST['textfield7']
    longitude = request.POST['textfield8']

    hospital.objects.filter(id=id).update(Name=name, Place=place, Pin=pin, Post=post, Phone=phone, Email=email, Latitude=latitude, longitude=longitude)
    return HttpResponse("<script>alert('updated successfully');window.location='/viewhospital'</script>")


def addpolice(request):
    return render(request, 'admin/Add_police.html')



def addpolice_registerbuttonclick(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    pin = request.POST['textfield3']
    post = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']
    latitude = request.POST['textfield7']
    longitude = request.POST['textfield8']


    obj = policestation()
    obj.Name = name
    obj.Place = place
    obj.Pin = pin
    obj.Post = post
    obj.Phone = phone
    obj.Email = email
    obj.Latitude = latitude
    obj.longitude = longitude
    obj.save()

    return HttpResponse("<script>alert('added successfully');window.location='/viewpolice'</script>")


def updatepolice(request,id):
    view=policestation.objects.get(id=id)
    return render(request, 'admin/Update_police.html',{"data":view})


def updatepolice_updatebuttonclick(request,id):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    pin = request.POST['textfield3']
    post = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']
    latitude = request.POST['textfield7']
    longitude = request.POST['textfield8']

    policestation.objects.filter(id=id).update(Name=name, Place=place, Pin=pin, Post=post,Phone=phone, Email=email, Latitude=latitude, longitude=longitude)
    return HttpResponse("<script>alert('updated successfully');window.location='/viewpolice'</script>")


def viewpolice(request):
    res = policestation.objects.all()
    return render(request, 'admin/view_police.html', {'data': res})


def delete_police(request, id):
    policestation.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/viewpolice'</script>")


def addfire(request):
    return render(request, 'admin/Add_fire.html')


def addfire_registerbuttonclick(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    pin = request.POST['textfield3']
    post = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']
    latitude = request.POST['textfield7']
    longitude = request.POST['textfield8']

    obj = firestation()
    obj.Name = name
    obj.Place = place
    obj.Pin = pin
    obj.Post = post
    obj.Phone = phone
    obj.Email = email
    obj.Latitude = latitude
    obj.longitude = longitude
    obj.save()

    return HttpResponse("<script>alert('added successfully');window.location='/viewfire'</script>")


def updatefire(request,id):
    view=firestation.objects.get(id=id)

    return render(request, 'admin/Update_fire.html',{"data":view})


def updatefire_updatebuttonclick(request,id):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    pin = request.POST['textfield3']
    post = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']
    latitude = request.POST['textfield7']
    longitude = request.POST['textfield8']

    firestation.objects.filter(id=id).update(Name=name, Place=place, Pin=pin, Post=post, Phone=phone, Email=email,Latitude=latitude, longitude=longitude)
    return HttpResponse("<script>alert('updated successfully');window.location='/viewfire'</script>")


def viewfire(request):
    res = firestation.objects.all()
    return render(request, 'admin/View_fire.html', {'data': res})

def delete_fire(request, id):
    firestation.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/viewfire'</script>")




def viewdonation(request):
    res = willingusers.objects.all()
    return render(request, 'admin/view_donation.html', {'data': res})


def addnotification(request):
    return render(request, 'admin/Add_notification.html')


def addnotification_addbuttonclick(request):
    disastercategory = request.POST['select']
    date = request.POST['textfield']
    information = request.POST['textarea']
    area = request.POST['textfield2']
    latitude = request.POST['textfield3']
    longitude = request.POST['textfield4']

    obj = notification()
    obj.DisasterCategory = disastercategory
    obj.Date= date
    obj.information = information
    obj.Area= area
    obj.Latitude = latitude
    obj.longitude = longitude
    obj.save()

    return HttpResponse("<script>alert('added successfully');window.location='/viewnotification'</script>")




def updatenotification(request,id):

    view=notification.objects.get(id=id)
    return render(request, 'admin/Update_notification.html',{"data":view})


def updatenotification_updatebuttonclick(request,id):
    disastercategory = request.POST['cate']
    date = request.POST['textfield2']
    information = request.POST['textarea']
    area = request.POST['textfield3']
    latitude = request.POST['textfield4']
    longitude = request.POST['textfield5']

    notification.objects.filter(id=id).update(DisasterCategory=disastercategory,Date=date,information=information,Area=area,Latitude=latitude,longitude=longitude)
    return HttpResponse("<script>alert('updated successfully');window.location='/viewnotification'</script>")


def viewnotification(request):
    res = notification.objects.all()
    return render(request, 'admin/View_notification.html', {'data': res})

def delete_notification(request, id):
    notification.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/viewnotification'</script>")


def addweather(request):
    return render(request, 'admin/Add_weather.html')


def addweather_addbuttonclick(request):
    weathernow = request.POST['textfield']
    date = request.POST['textfield2']
    area = request.POST['textfield3']

    obj = weather()
    obj.Weather = weathernow
    obj.Date = date
    obj.Area = area
    obj.save()
    return HttpResponse("<script>alert('added successfully');window.location='/viewweather'</script>")


def updateweather(request,id):
    view = weather.objects.get(id=id)
    return render(request, 'admin/Update_weather.html',{"data":view})


def updateweather_updatebuttonclick(request,id):
    weather1 = request.POST['textfield']
    date = request.POST['textfield2']
    area = request.POST['textfield3']

    weather.objects.filter(id=id).update(Weather=weather1,Date=date,Area=area)
    return HttpResponse("<script>alert('updated successfully');window.location='/viewweather'</script>")

def viewweather(request):
    res = weather.objects.all()
    return render(request, 'admin/View_weather.html', {'data': res})

def delete_weather(request, id):
    weather.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/viewweather'</script>")

def adddeath(request):
    return render(request, 'admin/Add_death.html')


def adddeath_addbuttonclick(request):
    disastertype = request.POST['select']
    deathcount = request.POST['textfield']
    date = datetime.datetime.now().strftime("%d-%m-%Y")

    obj = deathtoll()
    obj.DisasterType = disastertype
    obj.DeathCount = deathcount
    obj.Date = date
    obj.save()
    return HttpResponse("<script>alert('added successfully');window.location='/viewdeath'</script>")


def updatedeath(request,id):
    view = deathtoll.objects.get(id=id)

    return render(request, 'admin/update_death.html',{"data":view})


def updatedeath_updatebuttonclick(request,id):
    disastertype = request.POST['cate']
    deathcount = request.POST['textfield']
    date = request.POST['textfield2']

    deathtoll.objects.filter(id=id).update(DisasterType=disastertype,DeathCount=deathcount,Date=date)
    return HttpResponse("<script>alert('updated successfully');window.location='/viewdeath'</script>")


def viewdeath(request):
    res = deathtoll.objects.all()
    return render(request, 'admin/View_death.html', {'data': res})

def delete_death(request, id):
    deathtoll.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/viewdeath'</script>")


def addub(request):
    data = camp.objects.all()
    data1 = hospital.objects.all()
    return render(request, 'admin/Add_ub.html',{'view':data,"data":data1})


def addub_addbuttonclick(request):
    campcoordinator= request.POST['textfield6']
    area = request.POST['textfield']
    hospital = request.POST['textfield5']
    male = request.POST['textfield2']
    female = request.POST['textfield3']
    kids = request.POST['textfield4']

    obj = unidentifiedbodies()
    obj.CAMP_id = campcoordinator
    obj.Area = area
    obj.HOSPITAL_id = hospital
    obj.Male = male
    obj.Female = female
    obj.Kids = kids
    obj.save()
    return HttpResponse("<script>alert('added successfully');window.location='/viewub'</script>")


def updateub(request,id):
    view = unidentifiedbodies.objects.get(id=id)
    data = camp.objects.all()
    data1 = hospital.objects.all()
    return render(request, 'admin/Update_ub.html',{"data":view,"cmp":data,"hos":data1})


def updateub_updatebuttonclick(request,id):
    # campcoordinator = request.POST['textfield5']
    area = request.POST['textfield']
    # hospital = request.POST['textfield6']
    male = request.POST['textfield2']
    female = request.POST['textfield3']
    kids = request.POST['textfield4']
    unidentifiedbodies.objects.filter(id=id).update( Area=area, Male=male,Female=female,Kids=kids)
    return HttpResponse("<script>alert('updated successfully');window.location='/viewub'</script>")


def viewub(request):
    res = unidentifiedbodies.objects.all()
    return render(request, 'admin/View_Ub.html', {'data': res})

def delete_ub(request, id):
    unidentifiedbodies.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/viewub'</script>")



def viewmissingperson(request):
    res = missingPerson.objects.all()
    return render(request, 'admin/View_missingperson.html', {'data': res})

def verify(request,id):
    missingPerson.objects.filter(id=id).update(status="verified")
    return HttpResponse("<script>alert('verified successfully');window.location='/viewmissingperson'</script>")


def delete_missing(request, id):
    missingPerson.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/viewmissingperson'</script>")


def viewalertandverify(request):
    res = alert.objects.all()
    return render(request, 'admin/View_alert&verify.html', {'data': res})



def logout_buttonclick(request):
    request.session['lid']=""
    return HttpResponse("<script>alert('logout successfully');window.location='/'</script>")



def adminlanding(request):
    return render(request, 'admin/index.html')


###############################################################################################################

def coordinator_home(request):
    return render(request,"camp_coordinator/coordinator_home.html")


def coordinator_view_profile(request):
    data = camp.objects.get(LOGIN=request.session['lid'])
    request.session['cid']=data.id
    return render(request,'camp_coordinator/profile.html',{"view":data})



def add_inmates(request):
    return render(request,"camp_coordinator/add inmates.html")
def add_inmates_post(request):
    name  = request.POST['textfield']
    age  = request.POST['textfield2']
    gender  = request.POST['RadioGroup1']
    place  = request.POST['textfield3']
    date_of_vacate  = request.POST['textfield5']
    date_of_admission  = request.POST['textfield4']


    obj = inmates()
    obj.Place= place
    obj.Gender=gender
    obj.Age = age
    obj.Name = name
    obj.Dateofadmission = date_of_admission
    obj.Dateofvacate=date_of_vacate
    obj.CAMP_id = request.session['cid']
    obj.save()
    return HttpResponse("<script>alert('added successfully');window.location='/coordinator_home'</script>")


def view_volunteer(request):
    data = volunteer.objects.filter(LOGIN__usertype='pending',CAMP=request.session['cid'])
    return render(request,"camp_coordinator/view volenteer and approve.html",{'view':data})

def approve_volunteer(request,id):
    login.objects.filter(id = id).update(usertype = 'volunteer')
    return HttpResponse("<script>alert('approved successfully');window.location='/view_volunteer'</script>")

def reject_volunteer(request,id):
    login.objects.filter(id = id).update(usertype = 'rejected')
    return HttpResponse("<script>alert('rejected successfully');window.location='/view_volunteer'</script>")



def add_requirement(request):
    return render(request,"camp_coordinator/add requirement.html")

def add_requirement_post(request):
    des = request.POST['textarea']
    item = request.POST['textfield']
    obj = requirment()
    obj.Description =des
    obj.Itemrequired = item
    obj.CAMP_id = request.session['cid']
    obj.save()
    return HttpResponse("<script>alert('added successfully');window.location='/add_requirement'</script>")

def view_requirement(request):
    data = requirment.objects.filter(CAMP=request.session['cid'])
    return render(request,"camp_coordinator/view requirement.html",{'view':data})

def delete_requirement(request, id):
    requirment.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/view_requirement'</script>")


def edit_requirement(request,id):
    data = requirment.objects.get(id=id)
    return render(request,"camp_coordinator/edit requirement.html",{'view':data})

def edit_requirement_post(request,id):
    des = request.POST['textarea']
    item = request.POST['textfield']
    requirment.objects.filter(id =  id).update(Itemrequired = item,Description = des)
    return HttpResponse("<script>alert('edited successfully');window.location='/view_requirement'</script>")


def view_willing_users(request,id):
    data = willingusers.objects.filter(REQUIREMENT=id)
    return render(request,"camp_coordinator/view willing users.html",{'view':data})

def allocate_collection(request,id):
    data = volunteer.objects.filter(CAMP=request.session['cid'],LOGIN__usertype='volunteer')
    return render(request,"camp_coordinator/allocate collection to volunteer.html",{'view':data,"id":id})

def allocate_collectiont_post(request,id):
    vol = request.POST['select']
    obj = collection_duty()
    obj.VOLUNTEER_id =vol
    obj.status = 'pending'
    obj.WILLING_USERS_id = id
    obj.save()
    return HttpResponse("<script>alert('collection duty added successfully');window.location='/view_requirement'</script>")


def camp_view_disaster_notification(request):
    data =notification.objects.all()
    return render(request,"camp_coordinator/view disaster notification.html",{'view':data})


def camp_view_weather(request):
    data =weather.objects.all()
    return render(request,"camp_coordinator/weather details.html",{'view':data})


def add_missing_person(request):
    return render(request,"camp_coordinator/add_missing person.html")

def add_missing_person_post(request):
    name = request.POST['textfield']
    age = request.POST['textfield2']
    gender = request.POST['RadioGroup1']
    image = request.FILES['fileField']
    des = request.POST['textarea']
    d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs=FileSystemStorage()
    fs.save(r"C:\Users\arju\Desktop\relieflink\Relieflink_apk\static\missing person\\"+d+'.jpg',image)
    path='/static/missing person/'+d+'.jpg'

    obj = missingPerson()
    obj.Name =name
    obj.Age = age
    obj.Gender = gender
    obj.Image = path
    obj.Description = des
    obj.status = 'pending'
    obj.type = "camp"
    obj.LOGIN_id = request.session['lid']
    obj.save()
    return HttpResponse("<script>alert('added successfully');window.location='/add_missing_person'</script>")


def view_missing_person(request):
    data =missingPerson.objects.filter(LOGIN=request.session['lid'],status='pending')
    return render(request,"camp_coordinator/view missing person.html",{'view':data})

def delete_missing_person(request, id):
    missingPerson.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/view_missing_person'</script>")


def edit_missing_person(request,id):
    data = missingPerson.objects.get(id = id)
    return render(request,"camp_coordinator/edit missing person.html",{"view":data})

def edit_missing_person_post(request,id):
    try:
        name = request.POST['textfield']
        age = request.POST['textfield2']
        gender = request.POST['RadioGroup1']
        image = request.FILES['fileField']
        des = request.POST['textarea']
        d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs=FileSystemStorage()
        fs.save(r"C:\Users\arju\Desktop\relieflink\Relieflink_apk\static\missing person\\"+d+'.jpg',image)
        path='/static/missing person/'+d+'.jpg'

        missingPerson.objects.filter(id = id).update(Name =name,Age = age,Gender = gender,Description = des,Image = path)


        return HttpResponse("<script>alert('edited successfully');window.location='/view_missing_person'</script>")
    except Exception as e:
        name = request.POST['textfield']
        age = request.POST['textfield2']
        gender = request.POST['RadioGroup1']
        des = request.POST['textarea']
        missingPerson.objects.filter(id=id).update(Name=name, Age=age, Gender=gender, Description=des)
        return HttpResponse("<script>alert('edited successfully');window.location='/view_missing_person'</script>")



def camp_view_volunteer_request(request):
    data =volunteer_support.objects.filter(CAMP=request.session['cid'])
    return render(request,"camp_coordinator/view volunteer request.html",{'view':data})

def allocate_request(request,id):
    data = volunteer.objects.filter(CAMP=request.session['cid'],LOGIN__usertype='volunteer')
    return render(request,"camp_coordinator/allocate to request.html",{'view':data,"id":id})

def allocate_request_post(request,id):
    vol = request.POST['select']
    obj = volunteerAllocation()
    obj.VOLUNTEER_id =vol
    obj.VOLUNTEER_SUPPORT_id = id
    obj.date =  datetime.datetime.now().strftime("%Y-%m-%d")
    obj.save()
    return HttpResponse("<script>alert('volenteer allocated successfully');window.location='/camp_view_volunteer_request'</script>")

def view_allocate_request(request,id):
    data = volunteerAllocation.objects.filter(VOLUNTEER_SUPPORT=id)
    return render(request,"camp_coordinator/view allocation request.html",{'view':data})


def view_work_status(request,id):
    data = workstatus.objects.filter(VOLUNTEER_ALLOCATION=id)
    return render(request,"camp_coordinator/view work status.html",{'view':data})

def view_reporting(request,id):
    data = reporting.objects.filter(MISSING_PERSON=id)
    return render(request,"camp_coordinator/view reporting.html",{'view':data})

##############################################################################################################

def volunteer_home(request):
    return render(request,"volunteer/home.html")

def view_profile(request):
    data = volunteer.objects.get(id = request.session['vid'])
    return render(request,"volunteer/profile.html",{'view':data})


def view_collection_duty(request):
    data = collection_duty.objects.filter(VOLUNTEER=request.session['vid'])
    return render(request,"volunteer/view collection duty.html",{"view":data})


def update_collection_request(request,id):
    collection_duty.objects.filter(id = id).update(status = 'collected')
    return HttpResponse("<script>alert('status updated ');window.location='/view_collection_duty'</script>")


def volunteer_view_allocation(request):
    data = volunteerAllocation.objects.filter(VOLUNTEER=request.session['vid'])
    return render(request,"volunteer/volunteer_view allocation.html",{"view":data})

def update_work_status(request,id):
    return render(request,"volunteer/update work  status.html",{'id':id})

def update_work_status_post(request,id):
    status = request.POST['textarea']
    obj = workstatus()
    obj.VOLUNTEER_ALLOCATION_id = id
    obj.date =  datetime.datetime.now().strftime("%Y-%m-%d")
    obj.status =  status
    obj.save()
    return HttpResponse("<script>alert('Work status added successfully');window.location='/volunteer_view_allocation'</script>")



def volunteer_view_disaster_notification(request):
    data =notification.objects.all()
    return render(request,"volunteer/volenteer view disaster notification.html",{'view':data})



def volunteer_view_weather(request):
    data =weather.objects.all()
    return render(request,"volunteer/volunteer view weather.html",{'view':data})

def volunteer_view_education_content(request):
    data =education_content.objects.all()
    return render(request,"volunteer/education content.html",{'view':data})


def volunteer_register(request):
    data =camp.objects.all()
    return render(request,"volunteer/register.html",{'view':data})

def volunteer_register_action(request):
    name = request.POST['name']
    email = request.POST['email']
    pin = request.POST['pin']
    post = request.POST['post']
    place = request.POST['place']
    phone = request.POST['phone']
    skill = request.POST['skill']
    cmp = request.POST['camp']
    age = request.POST['age']
    gender = request.POST['gender']
    image = request.FILES['image']
    idproof = request.FILES['proof']
    password = request.POST['password']
    cpassword = request.POST['cpassword']
    d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    d1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    fs=FileSystemStorage()
    fs.save(r"C:\Users\arju\Desktop\relieflink\Relieflink_apk\static\images\\"+d+'.jpg',image)
    path='/static/images/'+d+'.jpg'

    fs.save(r"C:\Users\arju\Desktop\relieflink\Relieflink_apk\static\id_proof\\" + d1 + '.pdf', idproof)
    path1 = '/static/id_proof/' + d1 + '.pdf'
    if password == cpassword:
        obj1 = login()
        obj1.usertype='pending'
        obj1.username=email
        obj1.password=cpassword
        obj1.save()

        obj = volunteer()
        obj.Name =name
        obj.Age = age
        obj.Gender = gender
        obj.Image = path
        obj.Email = email
        obj.Contact_no = phone
        obj.Id_proof = path1
        obj.Place = place
        obj.post = post
        obj.pin = pin
        obj.Skill = skill
        obj.CAMP_id = cmp
        obj.LOGIN_id = obj1.id
        obj.save()
        return HttpResponse("<script>alert('registration successfull');window.location='/'</script>")

    else:
        return HttpResponse("<script>alert('password missmatch');window.location='/'</script>")


###############################################################################################################

def public_home(request):
    return render(request,'public/home.html')
def public_view_weather(request):
    data = weather.objects.all()
    return render(request,'public/public view weather.html',{"view":data})


def public_view_disaster_notification(request):
    data = notification.objects.all()
    return render(request, "public/public view disaster notification.html", {'view': data})

def public_view_missing_person(request):
    data = missingPerson.objects.filter(status='pending')
    return render(request,'public/public view missing person.html',{"view":data})

def public_view_deathtoll(request):
    data = deathtoll.objects.all()
    return render(request,'public/view death toll.html',{"view":data})


def public_view_camp(request):
    data = camp.objects.all()
    return render(request,'public/public view camp.html',{"view":data})


# ###########################################################################################3
# def user_login(request):
#     us = request.POST['username']
#     ps = request.POST['password']
#     data = login.objects.filter(username = us,password=ps)
#     if data.exists():
#         lid = data[0].id
#         type = data[0].usertype
#         return JsonResponse({"status": 'ok', "lid": lid, "type": type})
#     else:
#         return JsonResponse({"status": None})
#
#
# def view_disaster_notification(request):
#     no = notification.objects.all()
#     ar = []
#     for i in no:
#         ar.append({"nid":i.id,"dst_type":i.DisasterCategory,"date":i.Date,"info":i.information,"area":i.Area})
#     return JsonResponse({"status":"ok","data":ar})
#
# def view_death_toll(request):
#     no = deathtoll.objects.all()
#     ar = []
#     for i in no:
#         ar.append({"dtid":i.id,"dtcount":i.DeathCount,"date":i.Date,"dis_type":i.DisasterType})
#         print(ar,"dattaaa")
#     return JsonResponse({"status":"ok","data":ar})
#
# def view_weather_user(request):
#     no = weather.objects.all()
#     ar = []
#     for i in no:
#         ar.append({"wid":i.id,"area":i.Area,"date":i.Date,"weather":i.Weather})
#     return JsonResponse({"status":"ok","data":ar})
#
# def view_capm_user(request):
#     no = camp.objects.all()
#     ar = []
#     for i in no:
#         ar.append({"cid":i.id,"cname":i.camp_name,"email":i.Email,"place":i.place,"phone":i.Contact_no})
#         print(ar,"aaaa")
#     return JsonResponse({"status":"ok","data":ar})
#
# def view_plolicestation(request):
#     no = policestation.objects.all()
#     ar = []
#     for i in no:
#         ar.append({"psid":i.id,"name":i.Name,"email":i.Email,"phone":i.Phone,"place":i.Place,"pin":i.Pin,"post":i.Post})
#     return JsonResponse({"status":"ok","data":ar})
#
##############################################user-web################################################################
def user_view_near_by_policestations(request):
    res = policestation.objects.all()
    return render(request, 'user/user view policestation.html', {'data': res})


def user_view_firestation(request):
    res = firestation.objects.all()
    return render(request, 'user/user view firestation.html', {'data': res})


def user_view_camps(request):
    res = camp.objects.all()
    return render(request, 'user/user view camps.html', {'data': res})

def user_view_requirements(request,id):
    data = requirment.objects.filter(CAMP=id)
    return render(request, "user/user view requirements.html", {'view': data})


def add_to_willing(request,id):
    obj = willingusers()
    obj.REQUIREMENT_id = id
    obj.USER_id = user.objects.get(LOGIN=request.session['lid']).id
    obj.save()
    return HttpResponse("<script>alert('Willing Request Added');window.location='/user_view_camps'</script>")

def user_send_volunteer_support_request(request,id):
    obj=volunteer_support()
    obj.USER_id = user.objects.get(LOGIN=request.session['lid']).id
    obj.CAMP_id = id
    obj.save()
    return HttpResponse("<script>alert('Volunteer Request Added');window.location='/user_view_camps'</script>")


def user_view_assigned_volunteers(request):
    data = volunteerAllocation.objects.filter(VOLUNTEER_SUPPORT__USER__LOGIN=request.session['lid'])
    return render(request,'user/view volunteer support.html',{'view':data})

def user_view_education_content(request):
    data = education_content.objects.all()
    return render(request,'user/user view education content.html',{'view':data})

def user_view_disaster_notification(request):
    data = notification.objects.all()
    return render(request,'user/user view disaster notification.html',{"view":data})


def user_view_deathtoll(request):
    data = deathtoll.objects.all()
    return render(request,'user/user view death toll.html',{"view":data})


def user_view_weather(request):
    data = weather.objects.all()
    return render(request,'user/user view weather updates.html',{"view":data})


def user_view_ub(request):
    data = unidentifiedbodies.objects.all()
    return render(request,'user/user view ub.html',{'view':data})


def user_viewmissingperson(request):
    res = missingPerson.objects.all()
    return render(request, 'user/user view missing person.html', {'data': res})


def report_missing_person_place(request,id):
    return render(request, 'user/user add reporting date.html', {'id': id})

def user_report_missing_person(request,id):
    place = request.POST['place']
    obj = reporting()
    obj.USER_id = user.objects.get(LOGIN=request.session['lid']).id
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.place = place
    obj.MISSING_PERSON_id = id
    return HttpResponse("<script>alert('Reported');window.location='/user_viewmissingperson'</script>")

def user_add_alert(request):
    return render(request,'user/user add alert.html')


def user_add_alert_post(request):
    cate = request.POST['cat']
    area = request.POST['area']
    place = request.POST['place']
    time = request.POST['time']
    dis = request.POST['dec']
    obj = alert()
    # obj.USER_id = user.objects.get(LOGIN=request.session['lid']).id
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.Disastercategory = cate
    obj.Description = dis
    obj.Time = time
    obj.Area = area
    obj.Place = place
    return HttpResponse("<script>alert('Alert added');window.location='/user_add_alert'</script>")


def user_view_alert(request):
    data = alert.objects.all()
    return render(request,'user/user view alert.html',{'view':data})

def user_delete_alert(request,id):
    alert.objects.get(id = id).delete()
    return HttpResponse("<script>alert('Alert Removed');window.location='/user_view_alert'</script>")

def user_edit_alert(request,id):
    data = alert.objects.get(id = id)
    return render(request,'user/user edit alert.html',{'data':data})


def user_edit_alert_post(request,id):
    cate = request.POST['cat']
    area = request.POST['area']
    place = request.POST['place']
    time = request.POST['time']
    dis = request.POST['dec']
    alert.objects.filter(id = id).update(Disastercategory = cate,Place = place,Time = time,Area = area,Description = dis)
    return HttpResponse("<script>alert('Alert Updated');window.location='/user_view_alert'</script>")

def user_add_missing_person(request):
    return render(request,"camp_coordinator/add_missing person.html")

def user_add_missing_person_post(request):
    name = request.POST['textfield']
    age = request.POST['textfield2']
    gender = request.POST['RadioGroup1']
    image = request.FILES['fileField']
    des = request.POST['textarea']
    d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs=FileSystemStorage()
    fs.save(r"C:\Users\arju\Desktop\relieflink\Relieflink_apk\static\missing person\\"+d+'.jpg',image)
    path='/static/missing person/'+d+'.jpg'

    obj = missingPerson()
    obj.Name =name
    obj.Age = age
    obj.Gender = gender
    obj.Image = path
    obj.Description = des
    obj.status = 'pending'
    obj.type = "camp"
    obj.LOGIN_id = request.session['lid']
    obj.save()
    return HttpResponse("<script>alert('added successfully');window.location='/user_view_missing_person'</script>")


def user_view_missing_person(request):
    data =missingPerson.objects.filter(LOGIN=request.session['lid'],status='pending')
    return render(request,"user/user view missingperson.html",{'view':data})

def user_delete_missing_person(request, id):
    missingPerson.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/user_view_missing_person'</script>")


def user_edit_missing_person(request,id):
    data = missingPerson.objects.get(id = id)
    return render(request,"user/edit missing person.html",{"view":data})

def user_edit_missing_person_post(request,id):
    try:
        name = request.POST['textfield']
        age = request.POST['textfield2']
        gender = request.POST['RadioGroup1']
        image = request.FILES['fileField']
        des = request.POST['textarea']
        d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs=FileSystemStorage()
        fs.save(r"C:\Users\arju\Desktop\relieflink\Relieflink_apk\static\missing person\\"+d+'.jpg',image)
        path='/static/missing person/'+d+'.jpg'

        missingPerson.objects.filter(id = id).update(Name =name,Age = age,Gender = gender,Description = des,Image = path)


        return HttpResponse("<script>alert('edited successfully');window.location='/user_view_missing_person'</script>")
    except Exception as e:
        name = request.POST['textfield']
        age = request.POST['textfield2']
        gender = request.POST['RadioGroup1']
        des = request.POST['textarea']
        missingPerson.objects.filter(id=id).update(Name=name, Age=age, Gender=gender, Description=des)
        return HttpResponse("<script>alert('edited successfully');window.location='/user_view_missing_person'</script>")



def user_registr(request):
    return render(request,'user/user register.html')
def user_registrations(request):
    name = request.POST['name']
    age = request.POST['age']
    gender = request.POST['gender']
    place = request.POST['place']
    pin = request.POST['pin']
    post = request.POST['place']
    phone = request.POST['place']
    email = request.POST['email']
    password = request.POST['password']
    cpass = request.POST['cpass']
    data = login.objects.filter(username=email)
    if data.exists():
        return HttpResponse(
            "<script>alert('Email already Exists');window.location='/'</script>")
    else:
        if password == cpass:
            lo = login()
            lo.usertype= 'user'
            lo.username = email
            lo.password = cpass
            lo.save()

            obj = user()
            obj.Name = name
            obj.Age = age
            obj.Gender = gender
            obj.Place = place
            obj.pin = pin
            obj.post = post
            obj.Contact_no = phone
            obj.Email = email
            obj.LOGIN_id =lo.id
            obj.save()
            return HttpResponse(
                "<script>alert('Registration successfull');window.location='/'</script>")
        else:
            return HttpResponse(
                "<script>alert('Password Mismatch');window.location='/'</script>")


def user_home(request):
    return render(request,"user/user_home.html")
















































