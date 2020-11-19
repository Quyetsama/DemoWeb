from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
# from .forms import RegistrationForm
# , SetPasswordForm1
from django.contrib.auth import authenticate, login

# Create your views here.

class Trangchu(View):
    def get(self, request):
        return render(request, 'login/base.html')


# function base view
# def register(request):
#     form = RegistrationForm()

    #   kiểm tra người đùng đã nhấn nút đăng kí
#     if request.method == 'POST':

    #   đưa dữ liệu người dùng nhập vào trong form
#         form = RegistrationForm(request.POST)

    # nếu kiểm tra các trowngf trong form hợp lệ thì save user
#         if form.is_valid():
#             form.save()
    #   quay lại trang chủ
#             return HttpResponseRedirect('/')
#     return render(request, 'login/register.html', {'form': form})


# class base view
# class register(View):
#     def get(self, request):
#         form = RegistrationForm()
#         return render(request, 'login/register.html', {'form': form})
#
#     def post(self,request):
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#         return render(request, 'login/register.html', {'form': form})



from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Mật khẩu của bạn đã được cập nhật thành công!')
            return redirect('change_password')
        else:
            pass
            # messages.error(request, 'Vui lòng sửa lỗi bên dưới.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'login/change_password.html', {'form': form})




from django.views.generic import TemplateView

class Sitechange_password_OkView(TemplateView):
    template_name = 'change_password_ok.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('username')
        return context




from django.views.generic import TemplateView, FormView
# from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse
from .forms import RegisterForm

from django.contrib.auth import get_user_model

# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     class Meta:
#         model = User
#         fields = ('username', 'email')
#         field_classes = {'username': UsernameField}

class SiteRegisterView(FormView):
    template_name = 'demoregister.html'
    form_class = RegisterForm

    def form_valid(self, form):
        User = get_user_model()
        data = form.cleaned_data
        new_user = User.objects.create_user(username=data['username'],
                                            password=data['password1'],
                                            email=data['email']
                                            )
        # from pprint import pprint; pprint(data)
        url = f"{reverse('demoregister_ok')}?username={new_user.username}"
        return redirect(url)


class SiteRegisterOkView(TemplateView):
    template_name = 'demoregister_ok.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('username')
        return context



from .forms import PostForm
class AddPost(View):
    def get(self, request):
        f = PostForm()
        return render(request, 'login/post.html', {'form': f})
    def post(self, request):
        f = PostForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse('Ok')



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import MyUser
# from .serializers import GetAllSerializer, APISerializer, Post
# from django.contrib.auth.models import AbstractUser
#
# class GetAllAPIView(APIView):
#
#     def get(self, request):
#         list_course = MyUser.objects.all()
#         mydata = GetAllSerializer(list_course, many=True)
#         return Response(data= mydata.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         mydata = APISerializer(data=request.data)
#         if not mydata.is_valid():
#             return Response('Sai dữ liệu rồi!', status=status.HTTP_400_BAD_REQUEST)
#         username_get = mydata.data['username_post']
#         sodu_get = mydata.data['sodu_post']
#         kc=MyUser.objects.create(username=username_get, sodu=sodu_get)
#         return Response(data=kc.id, status=status.HTTP_200_OK)

from .tests import Put

class PutAPI(View):
    def get(self, request):
        return render(request, 'login/sellclone.html')

    def post(self, request):
        soduht = request.POST["sodu"]
        username = request.POST["username"]
        id_user = request.POST["id"]
        sl = request.POST["sl"]
        loai = request.POST['loai']
        f = Put(soduht ,username ,id_user, sl, loai)
        s = "\n"
        s = s.join(f)
        soduht = int(soduht)
        sl = int(sl)
        kc = -1
        if loai == "1":
            kc = soduht - (5000 * sl)
        if loai == "2":
            kc = soduht - (10000 * sl)
        if loai == "3":
            kc = soduht - (12000 * sl)
        if loai == "4":
            kc = soduht - (15000 * sl)
        if loai == "5":
            kc = soduht - (20000 * sl)
        if loai == "6":
            kc = soduht - (25000 * sl)

        if kc>=0:
            user = request.user
            clone_id = request.POST["loai"]
            so_luong = request.POST["sl"]
            history = HistoryModel(user=user, clone_id=clone_id, so_luong=so_luong, title_history = user, list_clone = s)
            history.save()
        return HttpResponse(s)



from .models import HistoryModel
class History(View):
    def get(self, request):
        history = 'Bạn cần đăng nhập để xem lịch sử mua hàng! '
        try:
            history = HistoryModel.objects.filter(user=request.user)
        except:
            pass
        return render(request, 'login/history.html', {'history':history})

