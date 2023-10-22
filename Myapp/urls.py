# urls.py
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('commande/',views.commande, name='commande'),  # Use 'commande' instead of 'index'
    path('index/', views.index, name='index'),
    path('download_links/', views.download_links, name='download_links'),
    path('clients/',views.clients_table, name='clients_table'),
    path('bondedecommandes/', views.bondedecommandes, name='bondedecommandes'),
    path('ajouter_client/', views.ajouter_client, name='ajouter_client'),
    path('ajouter_bondedecommande/', views.ajouter_bondedecommande, name='ajouter_bondedecommande'),
    path('edit_client/<int:client_id>/', views.edit_client, name='edit_client'),
    path('delete_client/<int:client_id>/', views.delete_client, name='delete_client'),
    path('edit_bondedecommande/<int:bondedecommande_id>/', views.edit_bondedecommande, name='edit_bondedecommande'),
    path('delete_bondedecommande/<int:bondedecommande_id>/', views.delete_bondedecommande, name='delete_bondedecommande'),
    path('bondedecommande/', views.bondedecommandes, name='bondedecommande'),
    path('convert/', views.convert_pdf_to_excel_express, name='convert_pdf_to_excel_express'),
    path('indexx/', views.indexx, name='indexx'),
    path('indexxx/', views.indexxx, name='indexxx'),
    path('indexxxx/', views.index4, name='index4'),
    path('convert_pdf_to_excel_MAXILV/', views.convert_pdf_to_excel_MAXILV, name='convert_pdf_to_excel_MAXILV'),

    # ... Your existing URL patterns ...
    #path('generate_report/', views.generate_report, name='generate_report'),
    path('report_table/', views.report_table, name='report_table'),
    path('report_list/', views.report_list, name='report_list'),
    path('comparaisonExcel/', views.comparaison_excel, name='comparaison_excel'),
    path('download_report/<int:report_id>/', views.download_report, name='download_report'),
    path('generate_error_excel/', views.generate_error_excel, name='generate_error_excel'),
    path('', views.login_view, name='login_view'),
    path('text/', views.convert_excel_to_txt, name='convert_excel_to_txt'),
    path('logout/', views.logout_view, name='logout_view'),
    path('acceuil/', views.ma_vue, name='ma_vue'),
]


    #path('rechercher/', views.rechercher, name='rechercher'),
    #path('generate-excel/', views.generate_excel, name='generate_excel'),
    #path('bondedecommande-list/', views.bondedecommande_list, name='bondedecommande_list'),
    #path('get_table_data/', views.get_table_data, name='get_table_data'),
    #path('generate-excel/', views.generate_excel, name='generate_excel'),
    #path('view_pdf_content/', views.view_pdf_content, name='view_pdf_content'),
    #path('download_excel/', views.download_excel, name='download_excel'),
    #path('download_console_output/', views.download_console_output, name='download_console_output'),



