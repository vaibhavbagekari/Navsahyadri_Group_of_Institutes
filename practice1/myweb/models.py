from django.db import models


# Create your models here.
class feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    

class faculty(models.Model):
    photo = models.ImageField(
        default=
        "https://tse4.mm.bing.net/th?id=OIP.OesLvyzDO6AvU_hYUAT4IAHaHa&pid=Api&P=0",
        null=True)
    designation= models.CharField(max_length=10 ,null=True)
    f_name = models.CharField(max_length=100, null=True)
    m_name = models.CharField(max_length=100, null=True)
    l_name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    Qualifications = models.CharField(max_length=50, null=True)
    Experience = models.CharField(max_length=50, null=True)
    contact_no = models.IntegerField(null=True)
    Email_Id = models.EmailField(max_length=100, null=True)
    program=models.CharField(max_length=50,null=True)
    department = models.CharField(max_length=50, null=True)


class nss_photo(models.Model):
    photos = models.ImageField(upload_to="images/")
    description = models.CharField(max_length=700, null=True)


# default=
#         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxvAsTIDLPrAsCWYxv9DS7xQjPlRS0SelfWkTe0TAtUA&s"
class elibrary_url(models.Model):
    name_eBooks = models.CharField(max_length=100)
    url_eBooks = models.CharField(max_length=200)


class e_Books_table(models.Model):
    e_Books = models.CharField(max_length=70)
    Link = models.CharField(max_length=70)
    Particular = models.CharField(max_length=70)


class student(models.Model):
    f_name = models.CharField(max_length=70)
    m_name = models.CharField(max_length=70)
    l_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    library_id = models.CharField(max_length=70)
    contact_no = models.IntegerField()
    department = models.CharField(max_length=70)
    year = models.CharField(max_length=70)
    sem = models.CharField(max_length=5, default="0")
    password = models.CharField(max_length=70)
    photo = models.ImageField(
        default=
        "https://tse4.mm.bing.net/th?id=OIP.OesLvyzDO6AvU_hYUAT4IAHaHa&pid=Api&P=0",
        blank=True,
        null=True)


class subject(models.Model):
    sem = models.CharField(max_length=5, default="0")
    sub_name = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=50, null=True)
    sub_notes = models.FileField(upload_to="doc/", null=True)


class attendance(models.Model):
    subject = models.CharField(max_length=50)
    date = models.DateField()
    library_id = models.CharField(max_length=50)
    att_check = models.BooleanField(default=False, blank=True, null=True)


class sem(models.Model):
    sem = models.CharField(max_length=3)
    subject1 = models.CharField(max_length=20)
    subject2 = models.CharField(max_length=20)
    subject3 = models.CharField(max_length=20)
    subject4 = models.CharField(max_length=20)
    subject5 = models.CharField(max_length=20)


class aicte_approvals(models.Model):
    title = models.CharField(max_length=30)
    aicte_file = models.FileField(upload_to="doc/", null=True)

class sppu_approvals(models.Model):
    title = models.CharField(max_length=30)
    sppu_file = models.FileField(upload_to="doc/", null=True)

class mandatory_disclosure(models.Model):
     title = models.CharField(max_length=30)
     mandatory_file = models.FileField(upload_to="doc/", null=True)

class notices(models.Model):
    notice_title = models.CharField(max_length=50)
    notice_discription=models.CharField(max_length=70)
    notice_file=models.FileField(upload_to="doc/", null=True)
    
class event(models.Model):
    event_title = models.CharField(max_length=50)
    event_discription=models.CharField(max_length=70)
    event_file=models.FileField(upload_to="doc/", null=True)

class engadmission_model(models.Model):
    name=models.CharField(max_length=100)
    Department=models.CharField(max_length=80)
    contact_no=models.IntegerField()
    email=models.EmailField(max_length=100)
    gendar=models.CharField(max_length=50)

class polyadmission_model(models.Model):
    name=models.CharField(max_length=100)
    Department=models.CharField(max_length=80)
    contact_no=models.IntegerField()
    email=models.EmailField(max_length=100)
    gendar=models.CharField(max_length=50)

class pharmadmission_model(models.Model):
    name=models.CharField(max_length=100)
    Department=models.CharField(max_length=80)
    contact_no=models.IntegerField()
    email=models.EmailField(max_length=100)
    gendar=models.CharField(max_length=50)

class mbaadmission_model(models.Model):
    name=models.CharField(max_length=100)
    Department=models.CharField(max_length=80)
    contact_no=models.IntegerField()
    email=models.EmailField(max_length=100)
    gendar=models.CharField(max_length=50)
