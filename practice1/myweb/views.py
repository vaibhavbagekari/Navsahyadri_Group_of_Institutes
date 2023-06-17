from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
# feature, nss_photo, elibrary_url, e_Books_table, student, faculty, sppu_approvals, subject, attendance, sem, aicte_approvals, event, notices,mandatory_disclosure
from django.contrib.auth import authenticate
from django.core.mail import send_mail


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
    approvals = aicte_approvals.objects.all()
    return render(request, 'pharmindex.html', {'approvals': approvals})


def d_pharm(request):
    return render(request, 'd-pharm.html')


def b_pharm(request):
    return render(request, 'b-pharm.html')


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


def about_nesgi(request):
    return render(request, 'about_nesgi.html')


def vision_mission(request):
    return render(request, "vision-mission.html")


def director_Desk(request):
    return render(request, 'director_desk.html')


def eng_fe(request):
    return render(request, 'eng_fe.html')


def eng_lab_cs(request):
    return render(request, 'eng_lab_cs.html')


def eng_lab_mechanical(request):
    return render(request, 'eng_lab_mechanical.html')


def eng_lab_civil(request):
    return render(request, 'eng_lab_civil.html')


def aicteindex(request):
    return render(request, 'aicteindex.html')


def eng_lab_electrical(request):
    return render(request, 'eng_lab_electrical.html')


def committees(reques):
    return render(reques, 'committees.html')


def eng_lab_aiml(request):
    return render(request, 'eng_lab_aiml.html')


def eng_lab_entc(request):
    return render(request, 'eng_lab_entc.html')


def engindex(request):
    return render(request, 'engindex.html')


def eng_electrical_syllabus(request):
    return render(request, 'eng_electrical_syllabus.html')


def eng_civil_syllabus(request):
    return render(request, 'eng_civil_syllabus.html')


def eng_mech_syllabus(request):
    return render(request, 'eng_mech_syllabus.html')


def eng_entc_syllabus(request):
    return render(request, 'eng_entc_syllabus.html')


def eng_aiml_syllabus(request):
    return render(request, 'eng_aiml_syllabus.html')


def eng_cs_syllabus(request):
    return render(request, 'eng_cs_syllabus.html')


def mbaindex(request):
    return render(request, 'mbaindex.html')


def ogc(request):
    return render(request, 'ogc.html')


def awardss(request):
    return render(request, 'awardss.html')


def engadmission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Contact = request.POST.get('Contact')
        Department = request.POST.get('Department')
        gendar = request.POST.get('gendar')

        engadmissions = engadmission_model.objects.create(
            name=name,
            email=email,
            contact_no=int(Contact),
            Department=Department,
            gendar=gendar)
        engadmissions.save()
        return render(request, 'engadmission.html')
    else:
        return render(request, 'engadmission.html')


def mba_contact(request):
    return render(request, 'mba_contact.html')


def mba_Infrastucture(request):
    return render(request, 'mba_Infrastucture.html')


def mba_placement(request):
    return render(request, 'mba_placement.html')


def mba_training(request):
    return render(request, 'mba_training.html')


def mba_about_ngi(request):
    return render(request, 'mba_about_ngi.html')

def mba_awardss(request):
    return render(request,'mba_awardss.html')

def eng_mech_ev(request):
    return render(request, 'eng_mech_ev.html')


def eng_placements(request):
    return render(request, 'eng_placements.html')


def m_pharm_faculty(request):
    m_pharm_f = m_pharm_facultys.objects.all()
    return render(request, 'm_pharm_faculty.html', {'facultys': m_pharm_f})


def b_pharm_faculty(request):
    b_pharm_f = b_pharm_facultys.objects.all()
    return render(request, 'b_pharm_faculty.html', {'facultys': b_pharm_f})


def d_pharm_faculty(request):
    d_pharm_f = d_pharm_facultys.objects.all()
    return render(request, 'd_pharm_faculty.html', {'facultys': d_pharm_f})


def mca(request):
    mca_f = mca_facultys.objects.all()
    return render(request, 'mca.html', {'faculties': mca_f})


def eng_contact(request):
    return render(request, 'eng_contact.html')


def poly_contact(request):
    return render(request, 'poly_contact.html')


def pharm_contact(request):
    return render(request, 'pharm_contact.html')


def eng_civil_ev(request):
    return render(request, 'eng_civil_ev.html')


def eng_aiml_ev(request):
    return render(request, 'eng_aiml_ev.html')


def mba_mba(request):
    mba_f = mba_facultys.objects.all()
    return render(request, 'mba_mba.html', {'faculties': mba_f})


def mbapp(request):
    mbapp_f = mbapp_facultys.objects.all()
    return render(request, 'mbapp.html', {'faculties': mbapp_f})


def eng_cs_ev(request):
    return render(request, 'eng_cs_ev.html')


def eng_fe_ev(request):
    return render(request, 'eng_fe_ev.html')


def eng_electrical_ev(request):
    return render(request, 'eng_electrical_ev.html')


def eng_entc_ev(request):
    return render(request, 'eng_entc_ev.html')


def polyadmission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Contact = request.POST.get('Contact')
        Department = request.POST.get('Department')
        gendar = request.POST.get('gendar')
        print(name, email, Contact, Department, gendar)
        polyadmissions = polyadmission_model.objects.create(
            name=name,
            email=email,
            contact_no=int(Contact),
            Department=Department,
            gendar=gendar)
        polyadmissions.save()
        return render(request, 'polyadmission.html')
    else:
        return render(request, 'polyadmission.html')


def pharmadmission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Contact = request.POST.get('Contact')
        Department = request.POST.get('Department')
        gendar = request.POST.get('gendar')
        pharmadmissions = pharmadmission_model.objects.create(
            name=name,
            email=email,
            contact_no=int(Contact),
            Department=Department,
            gendar=gendar)
        pharmadmissions.save()
        return render(request, 'pharmadmission.html')
    else:
        return render(request, 'pharmadmission.html')


def mbaadmission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Contact = request.POST.get('Contact')
        Department = request.POST.get('Department')
        gendar = request.POST.get('gendar')
        mbaadmissions = mbaadmission_model.objects.create(
            name=name,
            email=email,
            contact_no=int(Contact),
            Department=Department,
            gendar=gendar)
        mbaadmissions.save()
        return render(request, 'mbaadmission.html')
    else:
        return render(request, 'mbaadmission.html')


def hostel(request):
    return render(request, 'hostel.html')


def tronsport(request):
    return render(request, 'tronsport.html')


def library(request):
    return render(request, 'library.html')


def e_library(request):
    return render(request, 'e_library.html')


def counselling(request):
    return render(request, 'counselling.html')


def internet_facilities(request):
    return render(request, 'internet_facilities.html')


def mainactivity(request):
    return render(request, 'mainactivity.html')


def gallery(request):
    return render(request, 'gallery.html')


def main_placement(request):
    return render(request, 'main_placement.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'login.html')


def eng_fe_syllabus(request):
    return render(request, "eng_fe_syllabus.html")


def home(request):
    notice = notices.objects.all()
    events = event.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        Department = request.POST.get('Department')
        send_mail(
            "Testing mail",
            "hii " + name + " your department is " + Department,
            "webtestbyvaibhav.com",
            [email],
            fail_silently=False,
        )

        return render(request, 'index.html', {
            'notice': notice,
            'events': events
        })
    else:

        return render(request, 'index.html', {
            'notice': notice,
            'events': events
        })


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


def b_pharmaceutics_cem(request):
    return render(request, 'b-pharmaceutics-cem.html')


def poly_lab_civil(request):
    return render(request, 'poly_lab_civil.html')


def poly_lab_electrical(request):
    return render(request, 'poly_lab_electrical.html')


def poly_lab_cs(request):
    return render(request, 'poly_lab_cs.html')


def m_pharm(request):
    return render(request, 'm-pharm.html')


def b_pharmaceuitcs(request):
    return render(request, "b-pharmaceuitcs.html")


def pharm_student_welfare(request):
    return render(request, "pharm_student_welfare.html")


def pharm_computer_center(request):
    return render(request, "pharm_computer_center.html")


def pharm_library(request):
    return render(request, "pharm_library.html")


def transpotation(request):
    return render(request, "transportation.html")


def b_pharmacolory(request):
    return render(request, "b-pharmacology.html")


def pharm_health_care(request):
    return render(request, "pharm_health_care.html")


def pharm_coc(request):
    return render(request, "pharm_coc.html")


def b_pharmacognosy(request):
    return render(request, "b_pharmacognosy.html")


def manual_slider(request):
    return render(request, "manual_slider.html")


def pharm_plyaground(request):
    return render(request, "pharm_plyaground.html")


def pharm_gallery(request):
    return render(request, "pharm_gallery.html")


def pharm_hostel(request):
    return render(request, "pharm_hostel.html")


def slider(request):
    return render(request, "slider.html")


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


def sppu_approval(request):
    sppu_approval = sppu_approvals.objects.all()
    return render(request, 'SPPU_affiliation.html',
                  {'sppu_approvals': sppu_approval})


def mandatory_disclosures(request):
    mandatory_disclosures = mandatory_disclosure.objects.all()
    return render(request, "mandatory_disclosure.html",
                  {'mandatory_disclosure': mandatory_disclosures})


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
