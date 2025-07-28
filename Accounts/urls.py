from django.urls import path
from Accounts.views import create_account,user_login,custom_logout_view,user_profile
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('create/', create_account, name='account'),
    path('login/',user_login,name='login'),
    path('logout/',custom_logout_view,name='logout'),
    path('profile/', user_profile, name='profile'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)