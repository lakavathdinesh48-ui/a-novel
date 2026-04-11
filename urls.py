from django.contrib import admin
from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('', views.index, name='index'),  # <-- added name="index"
    
    # Admin URLs
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-home/', views.admin_home, name='admin_home'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('add-model-builders/', views.add_model_builders, name='add_model_builders'),
    # path('add-model-builder/', views.add_model_builder, name='add_model_builder'),
    path('list-model-builders/', views.list_model_builders, name='list_model_builders'),
    path('add-detector/', views.add_detector, name='add_detector'),
    path('list-detectors/', views.list_detectors, name='list_detectors'),

    # Model Builder URLs
    path('model-builder-login/', views.model_builder_login, name='model_builder_login'),
    path('model-builder-home/', views.model_builder_home, name='model_builder_home'),
    path('model-builder-logout/', views.model_builder_logout, name='model_builder_logout'),

    # Detector URLs
    path('detector-login/', views.detector_login, name='detector_login'),
    path('detector-home/', views.detector_home, name='detector_home'),
    path('detector-logout/', views.detector_logout, name='detector_logout'),
    path('enter-test-data/', views.enter_test_data, name='enter_test_data'),
    #path('upload-scan/', views.upload_scan, name='upload_scan'),

    
    path('detect-threats/', views.detect_threats, name='detect_threats'),
    path('view-reports/', views.view_reports, name='view_reports'),

    # SOC URLs
    path('soc-login/', views.soc_login, name='soc_login'),
    path('soc-home/', views.soc_home, name='soc_home'),
    path('soc-logout/', views.soc_logout, name='soc_logout'),

    


     
    path('model-builder/upload/', views.upload_dataset, name='upload_dataset'),
    path('model-builder/preprocess/', views.preprocess_dataset, name='preprocess_dataset'),
    path('model-builder/build/', views.build_model, name='build_model'),
    path('model-builder/datasets/', views.dataset_list, name='dataset_list'),


    path('datasets/', views.dataset_list, name='dataset_list'),  # for the link in template


    path('enter-test-data/', views.enter_test_data, name='enter_test_data'),

    path('export-reports/', views.export_test_reports, name='export-reports'),

    path('detector-reports/', views.detector_reports, name='detector_reports'),

    path('view-reports/', views.view_reports, name='view_reports'),




]
