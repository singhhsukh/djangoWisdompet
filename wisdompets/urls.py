from django.contrib import admin
from django.urls import path

from adoptions import views,api_views

urlpatterns = [
    path('api/v1/pets/', api_views.PetList.as_view()),
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('adoptions/<int:pet_id>/',views.pet_detail,name='pet_detail'),
    path('form/',views.hash_form,name='hash_form'),
    path('hash/<str:hash>/',views.hash_display,name='hash_display'),
    path('quickhash/',views.quickHash,name='quickhash'),
]
