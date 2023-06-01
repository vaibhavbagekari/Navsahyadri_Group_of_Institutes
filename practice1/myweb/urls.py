from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.index ,name='index'),
    # path('', views.form, name='form'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name="login"),
    # path('home/<str:login>', views.url_fun),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('mechanical/', views.mechanical, name='mechanical'),
    path('Civil/', views.Civil, name='Civil'),
    path('Electrical/', views.Electrical, name='Electrical'),
    path('ENTC/', views.ENTC, name='ENTC'),
    path('CS/', views.CS, name='CS'),
    path('AIML/', views.AIML, name='AIML'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('Activity/', views.Activity, name='Activity'),
    path('admission/', views.admission, name='admission'),
    path('tpo/', views.tpo, name='tpo'),
    path('studenthome/', views.studenthome, name='studenthome'),
    path('facultyhome/', views.facultyhome, name='facultyhome'),
    path('studenthome/<classdata>/', views.classdata, name='classdata'),
    path('stud_login/', views.stud_login, name='stud_login'),
    path('notes/', views.notes, name='notes'),
    path('elibrary/', views.elibrary, name='elibrary'),
    path('nss/', views.nss, name='nss'),
    path('signup/', views.signup, name='signup'),
    path('facultyhome/<url1>/', views.url1, name='url1'),
    path('add_atten/', views.add_atten, name='add_atten'),
    path('engindex/', views.engindex, name='engindex'),
    path('polyindex/', views.polyindex, name='polyindex'),
    path('home/<url2>', views.url2, name='url2'),
    path('pharmindex/', views.pharmindex, name='pharmindex'),
    path('aicte/', views.aicte, name="aicte"),
    path('eng_lab_cs/', views.eng_lab_cs, name="eng_lab_cs"),
    path('eng_lab_mechanical/',
         views.eng_lab_mechanical,
         name="eng_lab_mechanical"),
    path('eng_lab_civil/', views.eng_lab_civil, name="eng_lab_civil"),
    path('eng_lab_electrical/',
         views.eng_lab_electrical,
         name="eng_lab_electrical"),
    path('eng_lab_aiml/', views.eng_lab_aiml, name="eng_lab_aiml"),
    path('eng_lab_entc/', views.eng_lab_entc, name="eng_lab_entc"),
    path('mbaindex/', views.mbaindex, name="mbaindex"),
    path('coc/', views.coc, name="coc"),
    path('prinsipal_desk/', views.prinsipal_desk, name='prinsipal_desk'),
    path('president_desk', views.president_desk, name="president_desk"),
    path('reaching/', views.reaching, name='reaching'),
    path('establishment/', views.establishment, name="establishment"),
    path('ogc/', views.ogc, name='ogc'),
    path('awardss/', views.awardss, name='awardss'),
    path('engadmission/', views.engadmission, name='engadmission'),
    path('polyadmission/', views.polyadmission, name='polyadmission'),
    path('pharmadmission/', views.pharmadmission, name='pharmadmission'),
    path('mbaadmission/', views.mbaadmission, name='mbaadmission'),
    path('girl_hostel/', views.girl_hostel, name='girl_hostel'),
    path('boys_hostel/', views.boys_hostel, name='boys_hostel'),
    path('tronsport/', views.tronsport, name='tronsport'),
    path('library/', views.library, name='library'),
    path('e_library/', views.e_library, name='e_library'),
    path('counselling/', views.counselling, name='counselling'),
    path('internet_facilities/',
         views.internet_facilities,
         name='internet_facilities'),
    path('mainactivity/', views.mainactivity, name='mainactivity'),
    path('gallery/', views.gallery, name='gallery'),
    path("contact/", views.contact, name="contact"),
    path("poly_mechanical/", views.poly_mechanical, name="poly_mechanical"),
    path("poly_civil/", views.poly_civil, name="poly_civil"),
    path("poly_electrical/", views.poly_electrical, name="poly_electrical"),
    path("poly_cs/", views.poly_cs, name="poly_cs"),
    path("poly_lab_mechanical/",
         views.poly_lab_mechanical,
         name="poly_lab_mechanical"),
    path("poly_lab_civil/", views.poly_lab_civil, name="poly_lab_civil"),
    path("poly_lab_electrical/",
         views.poly_lab_electrical,
         name="poly_lab_electrical"),
    path("poly_lab_cs/", views.poly_lab_cs, name="poly_lab_cs"),
    path("eng_syllabus/", views.eng_syllabus, name="eng_syllabus"),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
