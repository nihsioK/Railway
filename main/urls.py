from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name = "login"),
    path('', views.homePage, name = "home"),
    path('logout/', views.logoutUser, name = "logout"),
    path('list/<mash_id>', views.listOfMashinist, name = "list"),
    path('accept/<mash_id>', views.acceptMashinist, name = "accept_mashinist"),
    path('accept/', views.acceptPage, name = "accept"),
    path('listOfCities', views.listOfCities, name = "listOfCities"),
    path('route', views.currentRoute, name = "current_route"),
    #path('accept', views.pass_train, name = "accept"),
]