from django.urls import path
from . import views
from .views import Trangchu, SiteRegisterView, SiteRegisterOkView, Sitechange_password_OkView, AddPost,PutAPI,History
    # , GetAllAPIView
# from .views import register
# , changepass
from django.contrib.auth import views as auth_views

from django.conf.urls import url




urlpatterns = [
    path('', Trangchu.as_view(), name='trangchu'),
    # function base view
    # path('register/', views.register, name='login'),
    # class base view
    # path('register/', register.as_view(), name='register'),

    # Đăng nhập
    path('login/', auth_views.LoginView.as_view(template_name="login/login.html"), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),

    # Đổi mật khẩu
    # path('changepassword/', changepass.as_view(), name='changepassword'),
    url('changepass/', views.change_password, name='change_password'),
    path('changepass/ok', Sitechange_password_OkView.as_view(template_name="login/change_password_ok.html"), name='change_password_ok'),

    # Đăng kí
    path('demoregister/', SiteRegisterView.as_view(template_name="login/demoregister.html"), name='demoregister'),
    path('demoregister/ok', SiteRegisterOkView.as_view(template_name="login/demoregister_ok.html"), name='demoregister_ok'),

    # Quên mật khẩu
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='login/reset_password.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='login/reset_password_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='login/reset_password_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='login/reset_password_complete.html'), name='password_reset_complete'),


    path('post/', AddPost.as_view(), name='post'),
    # path('api/', GetAllAPIView.as_view()),


    path('sellclone/', PutAPI.as_view(), name='sellclone'),

    path('history/', History.as_view(), name='history'),
]


