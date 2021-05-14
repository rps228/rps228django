from django.urls import path
from .import views 

urlpatterns =[
		path('',views.index,name='index'),
		path('submit',views.submit,name='submit'),
		path('main',views.main,name='main'),
		path('logout_user',views.logout_user,name='logout_user'),

]