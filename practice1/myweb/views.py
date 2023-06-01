from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib import messages
from .models import feature, nss_photo, elibrary_url, e_Books_table, student, faculty, subject, attendance, sem, aicte_approvals
from django.contrib.auth import authenticate


# Create your views here.
# def index(request):
#     context={
#         'username':'vaibhav',
#         'age':21,
#         'nationality':'indian'
#     }
#     return render(request, 'django_project.html',context)
def url_fun(request, login):
    return HttpResponse(login)


def form(request):
    return render(request, 'form.html')


def counter(request):
    text = request.GET['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})


def form2(request):
    features = feature.objects.all()
    return render(request, 'form2.html', {'features': features})


def form_co(request):
    username = request.POST['username']
    userID = request.POST['userID']
    password = request.POST['password']
    return render(request, 'form_co.html', {
        'username': username,
        'userID': userID,
        'password': password
    })


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Alredy Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password)
                user.save()
                return render(request, 'student_home.html', {
                    'username': username,
                    'email': email,
                })
        else:
            messages.info(request, 'password not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')


def stud_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(
                username=username).exists() and User.objects.filter(
                    password=password):
            return render(request, 'student_home.html', {
                'username': username,
                'password': password
            })
        else:
            messages.info(request, 'user not found')
            return redirect('home')
    else:
        return render(request, 'home')


def pharmindex(request):
    return render(request, 'pharmindex.html')


def polyindex(request):
    return render(request, 'polyindex.html')


def president_desk(request):
    return render(request, 'president_desk.html')


def reaching(request):
    return render(request, 'reaching.html')


def establishment(request):
    return render(request, 'establishment.html')


def coc(request):
    return render(request, 'coc.html')


def prinsipal_desk(request):
    return render(request, 'prinsipal_desk.html')

def eng_lab_cs(request):
    return render(request, 'eng_lab_cs.html')

def eng_lab_mechanical(request):
    return render(request, 'eng_lab_mechanical.html')

def eng_lab_civil(request):
    return render(request, 'eng_lab_civil.html')

def eng_lab_electrical(request):
    return render(request, 'eng_lab_electrical.html')

def eng_lab_aiml(request):
    return render(request, 'eng_lab_aiml.html')

def eng_lab_entc(request):
    return render(request, 'eng_lab_entc.html')

def engindex(request):
    return render(request, 'engindex.html')

def eng_syllabus(request):
    return render(request,'eng_syllabus.html')


def mbaindex(request):
    return render(request, 'mbaindex.html')


def ogc(request):
    return render(request, 'ogc.html')

def awardss(request):
    return render(request,'awardss.html')

def engadmission(request):
    return render(request,'engadmission.html')

def polyadmission(request):
    return render(request,'polyadmission.html')

def pharmadmission(request):
    return render(request,'pharmadmission.html')

def mbaadmission(request):
    return render(request,'mbaadmission.html')

def girl_hostel(request):
    return render(request,'girl_hostel.html')

def boys_hostel(request):
    return render(request,'boys_hostel.html')

def tronsport(request):
    return render(request,'tronsport.html')

def library(request):
    return render(request,'library.html')

def e_library(request):
    return render(request,'e_library.html')

def counselling(request):
    return render(request,'counselling.html')

def internet_facilities(request):
    return render(request,'internet_facilities.html')

def mainactivity(request):
    return render(request,'mainactivity.html')

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    return render(request,'contact.html')
 
def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'index.html')


def mechanical(request):
    mechanical_faculties = faculty.objects.filter(
        department="mechanical engineering")
    return render(request, 'mechanical.html',
                  {'mechanical_faculties': mechanical_faculties})


def Civil(request):
    civil_faculties = faculty.objects.filter(department="civil engineering")
    return render(request, 'Civil_Engineering.html',
                  {'civil_faculties': civil_faculties})


def Electrical(request):
    electrical_faculties = faculty.objects.filter(
        department="electrical engineering")
    return render(request, 'Electrical.html',
                  {'electrical_faculties': electrical_faculties})


def ENTC(request):
    entc_faculties = faculty.objects.filter(department="ENTC")
    return render(request, 'ENTC.html', {'entc_faculties': entc_faculties})


def CS(request):
    CS_faculties = faculty.objects.filter(department="CS")
    return render(request, 'CS.html', {'CS_faculties': CS_faculties})


def AIML(request):
    aiml_faculties = faculty.objects.filter(department="CS")
    # b=faculty.objects.filter(department="CS engineering")
    # aiml_faculties = (a,b)
    return render(request, 'AIML.html', {'aiml_faculties': aiml_faculties})


def aboutus(request):
    return render(request, 'aboutus.html')


def Activity(requesd):
    return render(requesd, 'Activity.html')


def admission(requesd):
    return render(requesd, 'admission.html')


def tpo(request):
    return render(request, 'tpo.html')

def poly_mechanical(request):
    return render(request, 'poly_mechanical.html') 

def poly_civil(request):
    return render(request, 'poly_civil.html') 

def poly_electrical(request):
    return render(request, 'poly_electrical.html') 

def poly_cs(request):
    return render(request, 'poly_cs.html') 

def poly_lab_mechanical(request):
    return render(request, 'poly_lab_mechanical.html') 

def poly_lab_civil(request):
    return render(request, 'poly_lab_civil.html') 

def poly_lab_electrical(request):
    return render(request, 'poly_lab_electrical.html') 

def poly_lab_cs(request):
    return render(request, 'poly_lab_cs.html') 

def studenthome(request):

    if request.method == 'POST':
        global library_id1
        library_id1 = request.POST.get('username')
        password1 = request.POST.get('password')
        if (student.objects.filter(library_id=library_id1,
                                   password=password1).exists()):
            user = student.objects.filter(library_id=library_id1).only(
                'f_name', 'm_name', 'l_name', 'email', 'library_id',
                'contact_no', 'department', 'year', 'photo')

            for i in user:
                if i.sem == "1":
                    s = "1"
                    subjects = subject.objects.filter(sem=s,
                                                      department=i.department)

                    return render(
                        request,
                        'student_home.html',
                        {
                            'user': user,
                            'subjects': subjects,
                            # 'att':att
                        })
                elif i.sem == "2":
                    s = "2"
                    subjects = subject.objects.filter(sem=s,
                                                      department=i.department)
                    return render(request, 'student_home.html', {
                        'user': user,
                        'subjects': subjects
                    })
                elif i.sem == "3":
                    s = "3"
                    subjects = subject.objects.filter(sem=s,
                                                      department=i.department)
                    return render(request, 'student_home.html', {
                        'user': user,
                        'subjects': subjects
                    })
                elif i.sem == "4":
                    s = "4"
                    sem_sub = sem.objects.filter(sem=s)
                    subjects = subject.objects.filter(sem=s,
                                                      department=i.department)
                    for v in sem_sub:
                        att_T1 = attendance.objects.filter(
                            library_id=library_id1, subject=v.subject1)
                        lt1 = len(att_T1)
                        att1 = attendance.objects.filter(
                            library_id=library_id1,
                            subject=v.subject1,
                            att_check=True)
                        l1 = len(att1)

                        att_T2 = attendance.objects.filter(
                            library_id=library_id1, subject=v.subject2)
                        lt2 = len(att_T2)
                        att2 = attendance.objects.filter(
                            library_id=library_id1,
                            subject=v.subject2,
                            att_check=True)
                        l2 = len(att2)

                        att_T3 = attendance.objects.filter(
                            library_id=library_id1, subject=v.subject3)
                        lt3 = len(att_T3)
                        att3 = attendance.objects.filter(
                            library_id=library_id1,
                            subject=v.subject3,
                            att_check=True)
                        l3 = len(att3)

                        att_T4 = attendance.objects.filter(
                            library_id=library_id1, subject=v.subject4)
                        lt4 = len(att_T4)
                        att4 = attendance.objects.filter(
                            library_id=library_id1,
                            subject=v.subject4,
                            att_check=True)
                        l4 = len(att4)

                        att_T5 = attendance.objects.filter(
                            library_id=library_id1, subject=v.subject5)
                        lt5 = len(att_T5)
                        att5 = attendance.objects.filter(
                            library_id=library_id1,
                            subject=v.subject5,
                            att_check=True)
                        l5 = len(att5)
                        lt = (lt1 + lt2 + lt3 + lt4 + lt5)
                        l = l1 + l2 + l3 + l4 + l5
                        p = (l / lt) * 100
                        tp = 100 - p
                        return render(
                            request, 'student_home.html', {
                                'user': user,
                                'subjects': subjects,
                                's1': l1,
                                's2': l2,
                                's3': l3,
                                's4': l4,
                                's5': l5,
                                'p': p,
                                'tp': tp
                            })
                elif i.sem == "5":
                    s = "5"
                    subjects = subject.objects.filter(sem=s,
                                                      department=i.department)
                    return render(request, 'student_home.html', {
                        'user': user,
                        'subjects': subjects
                    })
                elif i.sem == "6":
                    s = "6"
                    subjects = subject.objects.filter(sem=s,
                                                      department=i.department)
                    return render(request, 'student_home.html', {
                        'user': user,
                        'subjects': subjects
                    })
                elif i.sem == "7":
                    s = "7"
                    subjects = subject.objects.filter(sem=s,
                                                      department=i.department)
                    return render(request, 'student_home.html', {
                        'user': user,
                        'subjects': subjects
                    })
                else:
                    s = "8"
                    subjects = subject.objects.filter(sem=s,
                                                      department=i.department)
                    return render(request, 'student_home.html', {
                        'user': user,
                        'subjects': subjects
                    })
        else:
            messages.info(request, 'user not found')
            return redirect('home')
    else:
        return render(request, "index.html")


def facultyhome(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        department = request.POST.get('department')
        s = request.POST.get('sem')
        if (faculty.objects.filter(username=username,
                                   password=password1).exists()):

            user = faculty.objects.filter(username=username).only(
                'f_name', 'm_name', 'l_name', 'Qualifications', 'Email_Id',
                'Experience', 'contact_no', 'department', 'photo')

            subjects = subject.objects.filter(sem=s, department=department)
            return render(request, 'facultyhome.html', {
                'user': user,
                'subject': subjects
            })

        else:
            messages.info(request, 'user not found')
            return redirect('home')
    else:
        return render(request, "index.html")


def notes(request):
    v = 6
    return render(request, 'notes.html', {'v': v})


def elibrary(request):
    elibrary_urls = elibrary_url.objects.all()
    e_Books_tables = e_Books_table.objects.all()
    return render(request, 'elibrary.html', {
        'elibrary_urls': elibrary_urls,
        'e_Books_tables': e_Books_tables
    })


def nss(request):
    nss_photos = nss_photo.objects.all()
    return render(request, 'nss.html', {'nss_photos': nss_photos})


def signup(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        m_name = request.POST.get('m_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        library_id = request.POST.get('library_id')
        contact_no = request.POST.get('contact_no')
        department = request.POST.get('department')
        year = request.POST.get('year')
        photo = request.FILES.get('photo')
        sem = request.POST.get('sem')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 == pass2:
            if student.objects.filter(email=email).exists():
                messages.info(request, 'email Already Exist')
                return redirect('signup')
            elif student.objects.filter(library_id=library_id).exists():
                messages.info(request, 'library_id Already Exist')
                return redirect('signup')
            elif student.objects.filter(contact_no=contact_no).exists():
                messages.info(request, 'contact_no Already exist')
                return redirect('signup')
            else:
                students = student.objects.create(f_name=f_name,
                                                  m_name=m_name,
                                                  l_name=l_name,
                                                  email=email,
                                                  library_id=library_id,
                                                  contact_no=int(contact_no),
                                                  department=department,
                                                  year=year,
                                                  sem=sem,
                                                  password=pass1,
                                                  photo=photo)
                students.save()
                return render(request, 'thank you.html')
        else:
            messages.info(request, 'password is not same')
            return redirect('signup')
    else:
        return render(request, 'signuppage.html')


def classdata(request, classdata):
    return render(request, "notes.html", {'classdata': classdata})


def url1(request, url1):
    department = request.POST.get('department')
    s = request.POST.get('sem')
    subjects = subject.objects.filter(sem=s, department=department)
    user = student.objects.filter(department=department,
                                  sem=s).order_by("l_name")
    return render(request, url1, {'user': user, 'subjects': subjects})


def url2(request, url2):

    print(url2)
    return render(request, url2)


# def form2(request):
#     features = feature.objects.all()
#     return render(request, 'form2.html', {'features': features})
def aicte(request):
    approvals = aicte_approvals.objects.all()
    return render(request, 'aicte_approvals.html', {'approvals': approvals})


def add_atten(request):
    if request.method == "POST":
        att_date = request.POST.get('date')
        subject = request.POST.get('subject')
        department = request.POST.get('department')
        s = request.POST.get('sem')
        # print(att_date,subject,department,s)
        user = student.objects.filter(department=department,
                                      sem=s).order_by("l_name")

        for i in user:

            att_id = request.POST.get('att_', i.library_id)
            att_check = request.POST.get(i.library_id) or 0

            # print(att_id,att_check)
            att_create = attendance.objects.create(subject=subject,
                                                   date=att_date,
                                                   library_id=att_id,
                                                   att_check=att_check)
            att_create.save()
        return render(request, 'thank you.html')
    else:
        return redirect('home')
