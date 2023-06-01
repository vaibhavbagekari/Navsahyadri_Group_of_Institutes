from django.contrib import admin

# Register your models here.,
from .models import feature, nss_photo, elibrary_url, e_Books_table, student, faculty, subject, attendance, sem, aicte_approvals

admin.site.register(feature)


class facultyAdmin(admin.ModelAdmin):
    fac_display = ('username', 'password', 'photo', 'Qualifications',
                   'Experience', 'contact_no', 'Email_Id', 'department')


admin.site.register(faculty, facultyAdmin)


class nss_photosAdmin(admin.ModelAdmin):
    nss_display = ('photos', 'description')


admin.site.register(nss_photo, nss_photosAdmin)


class elibrary_urlAdmin(admin.ModelAdmin):
    url_display = ('name_eBooks', 'url_eBooks')


admin.site.register(elibrary_url, elibrary_urlAdmin)


class e_Books_tableAdmin(admin.ModelAdmin):
    e_Books_display = ('S.NO', 'E-resource', 'Link', 'Particular')


admin.site.register(e_Books_table, e_Books_tableAdmin)


class studentAdmin(admin.ModelAdmin):
    student_display = ('f_name', 'm_name', 'l_name', 'email', 'library_id',
                       'contact_no', 'department', 'year', 'password', 'photo')


admin.site.register(student, studentAdmin)


class subjectAdmin(admin.ModelAdmin):
    subject_display = ('sem', 'sub_name', 'sub_notes', 'department')


admin.site.register(subject, subjectAdmin)


class attendanceAdmin(admin.ModelAdmin):
    attendance_display = ('subject', 'date', 'library_id', 'att_check')


admin.site.register(attendance, attendanceAdmin)


class semAdmin(admin.ModelAdmin):
    sem4_display = ('sem', 'subject1', 'subject2', 'subject3', 'subject4',
                    'subject5')


admin.site.register(sem, semAdmin)

class aicteAdmin(admin.ModelAdmin):
    aict_display = ('title','file')


admin.site.register(aicte_approvals, aicteAdmin)
