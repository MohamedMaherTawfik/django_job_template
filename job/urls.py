from django.urls import path
from .views import job_list,job_detail,Job_apply
from .api import joblistapi,jobdetailapi


urlpatterns = [
    path('', job_list),
    path('<slug:slug>',job_detail),
    path('<slug:slug>/apply',Job_apply.as_view()),



    path('api/list',joblistapi.as_view()),
    path('api/list/<int:pk>',jobdetailapi.as_view()),
]
