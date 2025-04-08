from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),
    path('home/', views.home, name='home'),
    path ('logout/', views.logoutUser, name = "logout"),
        #path('signup/', SignUpView.as_view(), name='signup'),
    path('details/', views.details, name='details'),
    path('receipts/', views.receipts, name='receipts'),
    path('register/', views.register, name='register'),
    path('terms/', views.terms, name='terms'),

]
