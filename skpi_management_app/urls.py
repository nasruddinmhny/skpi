from unicodedata import name
from django.urls import path
from . import views
from . import adminHome,StaffHome,MahasiswaHome


urlpatterns = [
    path('',views.loginPage,name="login"),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('get_user_details/',views.get_user_details,name='get_user_details'),
    path('admin_home/',adminHome.admin_home,name='admin-home'),
    path('admin_profile/',adminHome.admin_profile,name='admin_profile'),
    path('manage_perguruan_tinggi/',adminHome.manage_perguruantinggi,name='manage_perguruan_tinggi'),
    path('hapus_perguruan_tinggi/<int:perguruantinggi_id>/',adminHome.hapus_perguruantinggi,name='hapus_perguruan_tinggi'),
    path('update_perguruan_tinggi/<int:perguruantinggi_id>/update',adminHome.edit_perguruantinggi,name='edit_perguruan_tinggi'),
    path('manage_fakultas/',adminHome.manage_fakultas,name='manage_fakultas'),
    path('hapus_fakultas/<int:fakultas_id>/',adminHome.hapus_fakultas,name='hapus_fakultas'),
    path('update_fakultas/<int:fakultas_id>/',adminHome.update_fakultas,name='update_fakultas'),
    path('manage_programstudi/',adminHome.manage_programstudi,name='manage_programstudi'),
    path('update_programstudi/<int:programstudi_id>',adminHome.update_programstudi,name='update_programstudi'),
    path('view_programstudi_detail/<int:programstudi_id>/',adminHome.view_programstudi_detail,name='view_programstudi_detail'),
    path('manage_staff/',adminHome.manage_staff,name='manage_staff'),
    path('add_staff/',adminHome.add_staff,name='add_staff'),
    path('add_staff_save/',adminHome.add_staff_save,name="add_staff_save"),
    path('manage_mahasiswa/',adminHome.manage_mahasiswa,name='manage_mahasiswa'),
    path('add_mahasiswa/',adminHome.add_mahasiswa,name='add_mahasiswa'),
    path('add_mahasiswa_save/', adminHome.add_mahasiswa_save,name='add_mahasiswa_save'),
    path('manage_gelar/',adminHome.manage_gelar,name='manage_gelar'),
     path('update_gelar/<int:gelar_id>/',adminHome.update_gelar,name='update_gelar'),




    path('check_email_exist/', adminHome.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', adminHome.check_username_exist, name="check_username_exist"),


]
