from django.urls import path
from . import views
urlpatterns = [
    path('homepage/',views.homePage,name='homepage'),
    path('aboutpage/',views.aboutPage,name='aboutpage'),
    path('addideapage/',views.addIdeaPage,name='addideapage'),
    path('updateideapage/<int:id>/',views.updateIdeaPage,name='updateideapage'),
    path('deleteidea/<int:id>/',views.deleteIdea,name='deleteidea'),
    path('dashboardpage/',views.dashboardPage,name='dashboardpage'),
    path('signuppage/',views.signupPage,name='signuppage'),
    path('logoutpage/',views.logoutPage,name='logoutpage'),
    path('loginpage/',views.loginPage,name='loginpage')
]