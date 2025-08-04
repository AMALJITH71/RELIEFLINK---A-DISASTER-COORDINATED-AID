from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    usertype = models.CharField(max_length=20)

class camp(models.Model):
    camp_name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    Coordinator_name = models.CharField(max_length=50)
    Number_of_inmates = models.CharField(max_length=50)
    Contact_no = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    Latitude = models.CharField(max_length=10)
    Longitude = models.CharField(max_length=10)
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE)

class volunteer(models.Model):
    Name = models.CharField(max_length=200)
    Age = models.CharField(max_length=200)
    Gender = models.CharField(max_length=200)
    Place = models.CharField(max_length=200)
    pin = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    Id_proof = models.CharField(max_length=50)
    Image = models.CharField(max_length=50)
    Skill = models.CharField(max_length=50)
    Contact_no = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)
    CAMP = models.ForeignKey(camp, on_delete=models.CASCADE,default=1)



class policestation(models.Model):
    Name  = models.CharField(max_length=100)
    Place  = models.CharField(max_length=50)
    Pin  = models.CharField(max_length=50)
    Post  = models.CharField(max_length=50)
    Phone  = models.CharField(max_length=50)
    Email  = models.CharField(max_length=50)
    Latitude  = models.CharField(max_length=10)
    longitude  = models.CharField(max_length=10)

class hospital(models.Model):
    Name  = models.CharField(max_length=100)
    Place  = models.CharField(max_length=50)
    Pin  = models.CharField(max_length=50)
    Post  = models.CharField(max_length=50)
    Phone  = models.CharField(max_length=50)
    Email  = models.CharField(max_length=50)
    Latitude  = models.CharField(max_length=10)
    longitude  = models.CharField(max_length=10)


class firestation(models.Model):
    Name  = models.CharField(max_length=100)
    Place  = models.CharField(max_length=50)
    Pin  = models.CharField(max_length=50)
    Post  = models.CharField(max_length=50)
    Phone  = models.CharField(max_length=50)
    Email  = models.CharField(max_length=50)
    Latitude  = models.CharField(max_length=10)
    longitude  = models.CharField(max_length=10)

class notification(models.Model):
    DisasterCategory  = models.CharField(max_length=100)
    Date  = models.CharField(max_length=50)
    information  = models.CharField(max_length=500)
    Area  = models.CharField(max_length=50)
    Latitude  = models.CharField(max_length=10)
    longitude  = models.CharField(max_length=10)

class weather(models.Model):
    Weather  = models.CharField(max_length=100)
    Date  = models.CharField(max_length=50)
    Area  = models.CharField(max_length=50)

class deathtoll(models.Model):
    DisasterType  = models.CharField(max_length=100)
    DeathCount  = models.CharField(max_length=100)
    Date  = models.CharField(max_length=50)

class unidentifiedbodies(models.Model):
    CAMP  = models.ForeignKey(camp, on_delete=models.CASCADE)
    HOSPITAL  = models.ForeignKey(hospital, on_delete=models.CASCADE)
    Area  = models.CharField(max_length=100)
    Male  = models.CharField(max_length=50)
    Female  = models.CharField(max_length=50)
    Kids  = models.CharField(max_length=50)

class missingPerson(models.Model):
    Name  = models.CharField(max_length=100)
    Age  = models.CharField(max_length=100)
    Gender  = models.CharField(max_length=50)
    Image  = models.CharField(max_length=50)
    Description  = models.CharField(max_length=500)
    status  = models.CharField(max_length=500)
    type  = models.CharField(max_length=500)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)


class alert(models.Model):
    Disastercategory  = models.CharField(max_length=100)
    Place  = models.CharField(max_length=100)
    Area  = models.CharField(max_length=50)
    Time  = models.CharField(max_length=50)
    Description  = models.CharField(max_length=500)

class inmates(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    Gender = models.CharField(max_length=50)
    Place = models.CharField(max_length=50)
    Dateofadmission = models.CharField(max_length=500)
    Dateofvacate = models.CharField(max_length=500)
    CAMP = models.ForeignKey(camp,on_delete=models.CASCADE)


class requirment(models.Model):
    CAMP = models.ForeignKey(camp, on_delete=models.CASCADE)
    Itemrequired = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)


class user(models.Model):

    Name = models.CharField(max_length=200)
    Age = models.CharField(max_length=200)
    Gender = models.CharField(max_length=200)
    Place = models.CharField(max_length=200)
    pin = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    Contact_no = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE)

class willingusers(models.Model):
    REQUIREMENT = models.ForeignKey(requirment, on_delete=models.CASCADE)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)


class collection_duty(models.Model):
    VOLUNTEER = models.ForeignKey(volunteer, on_delete=models.CASCADE)
    WILLING_USERS = models.ForeignKey(willingusers, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)


class volunteer_support(models.Model):
    CAMP = models.ForeignKey(camp, on_delete=models.CASCADE)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    date = models.CharField(max_length=50)


class volunteerAllocation(models.Model):
    VOLUNTEER = models.ForeignKey(volunteer, on_delete=models.CASCADE)
    VOLUNTEER_SUPPORT = models.ForeignKey(volunteer_support, on_delete=models.CASCADE)
    date = models.CharField(max_length=50)

class workstatus(models.Model):
    VOLUNTEER_ALLOCATION = models.ForeignKey(volunteerAllocation, on_delete=models.CASCADE)
    date = models.CharField(max_length=50)
    status = models.CharField(max_length=500)

class reporting(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    MISSING_PERSON = models.ForeignKey(missingPerson, on_delete=models.CASCADE)
    date = models.CharField(max_length=50)
    place = models.CharField(max_length=500)

class education_content(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)






























