from django.urls import path
from users.views import home, regiser,login_user,logout_user, download_csv
urlpatterns = [
    path('',home,name="home"),
    path('register/',regiser,name="register"),
    path('login/',login_user,name="login"),
    path('logout/',logout_user,name="logout"),
    path('export/',download_csv,name="export")
]
 