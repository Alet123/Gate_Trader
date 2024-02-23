from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('otp', views.otp, name='otp'),
    path('index', views.index, name='index'),
    path('news', views.news, name='news'),
    path('broker', views.broker, name='broker'),
    path('subscriptions', views.subscriptions, name='subscriptions'),
    path('profile', views.profile, name='profile'),
    path('edit', views.edit, name='edit'),
    path('order', views.order, name='order'),
    path('p&l', views.pl, name='p&l'),
    path('trade_graph', views.trade_graph, name='trade_graph'),
    path('p&l_analysis', views.planalysis, name='p&l_analysis'),
    path('market', views.market, name='market'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('contact/', views.contact, name='contact'),

]
