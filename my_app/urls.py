 from django.urls import path
 from . import views
 urlpatterns = [
        path('',views.home ,name = 'home'),
        path('new_search',views.new_search ,namespace = 'new_search'),




 ]
