from django.urls import path
from Rtomanage import views

urlpatterns = [
    path("",views.admin_dashboard,name="admin_dashboard"),
    path("getusers",views.get_users,name="getusers"),
    path('approveuser/<int:cr_id>/', views.approveuser, name="approveuser"),
    path('rejectuser/<int:cr_id>/', views.rejectuser, name="rejectuser"),
    path("managelearnerslicense",views.manage_learners_license,name="managelearnerslicense"),
    path('approvelearners/<int:cr_id>/', views.approveuser, name="approvelearners"),
    path('rejectlearners/<int:cr_id>/', views.rejectuser, name="rejectlearners"),
    path("managelicense",views.manage_license,name="managelicense"),
    path('approvelicense/<int:cr_id>/', views.approveuser, name="approvelicense"),
    path('rejectlicence/<int:cr_id>/', views.rejectuser, name="rejectlicence"),
    path("managerenewlicense",views.manage_renew_license,name="managerenewlicense"),
    path('approverenewlicense/<int:cr_id>/', views.approveuser, name="approverenewlicense"),
    path('rejectrenewlicence/<int:cr_id>/', views.rejectuser, name="rejectrenewlicence"),
    path("manageduplicatelicense",views.manage_duplicate_license,name="manageduplicatelicense"),
    path('approveduplicatelicense/<int:cr_id>/', views.approveuser, name="approveduplicatelicense"),
    path('rejectduplicatelicence/<int:cr_id>/', views.rejectuser, name="rejectduplicatelicence"),
    path("managehazmate",views.manage_hazmate,name="managehazmate"),
    path('approvehazmate/<int:cr_id>/', views.approvehazmate, name="approvehazmate"),
    path('rejecthazmate/<int:cr_id>/', views.rejecthazmate, name="rejecthazmate"),
    path("manageinternationallicense",views.manage_international_license,name="manageinternationallicense"),
    path("managepsvBadge",views.manage_psvBadge,name="managepsvBadge"),
    path('approvepsv/<int:cr_id>/', views.approvepsv, name="approvepsv"),
    path('rejectpsv/<int:cr_id>/', views.rejectpsv, name="rejectpsv"),
    path("managenoc",views.manage_noc,name="managenoc"),
    path('approvenoc/<int:cr_id>/', views.approvenoc, name="approvenoc"),
    path('rejectnoc/<int:cr_id>/', views.rejectnoc, name="rejectnoc"),
    path("managenoccancellation",views.manage_noc_cancellation,name="managenoccancellation"),
    path("newvehicleregister",views.new_vehicle_register,name="newvehicleregister"),
    path("vehicleownershipstatus",views.vehicle_ownership_status,name="vehicleownershipstatus"),
    path("updatelicensedata",views.update_license_data,name="updatelicensedata"),
    path("testdate",views.test_date,name="testdate"),
    path("viewpayment",views.view_payment,name="viewpayment"),
    path('approvepayment/<int:cr_id>/', views.approvepayment, name="approvepayment"),
    path('rejectpayment/<int:cr_id>/', views.rejectpayment, name="rejectpayment"),
    path("viewreport",views.view_report,name="viewreport"),
    path("viewtestdate",views.view_test_date,name="viewtestdate"),
    path("createTestDate",views.create_test_date,name="createTestDate"),
]