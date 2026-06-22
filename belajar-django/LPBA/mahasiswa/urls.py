from django.urls import path
from . import views

urlpatterns =[
  path('', views.beranda, name='beranda_page'),
  
  path('about/', views.about, name='about_page'),
  
  path('news/', views.news, name='news_page'),
  
  path('contact/', views.contact, name='contact_page'),
  
  path('achievement/', views.achievement, name='achievement_page'),
  
  path('education/', views.education, name='education_page'),

  path('family/', views.family, name='family_page'),
  
  path('product/', views.product, name='product_page'),
  
  path('skill/', views.skill, name='skill_page'),
  
  path('others/', views.others, name='others_page'),
]