from django.contrib import admin
from django.urls import path,include
from tutorial import views

urlpatterns = [
    path('', views.login_redirect, name = 'login_redirect'),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls', namespace='accounts')),

]
