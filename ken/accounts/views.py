from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login,logout,authenticate
from .forms import UserCreateForm
from django.contrib import messages

#  from django.contrib.auth.decorators import login_required

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('home')
    template_name = "accounts/registration.html"
    def form_valid(self, form):
        valid = super().form_valid(form)
        email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
        user = authenticate(email=email, password=password)

        login(self.request, user)
        return valid

# function based view
# def signUp(request):
#     if request.method == 'POST':
#         form = UserCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Account has been created!')
#             return redirect('/')
#     else:
#         form = UserCreateForm()
#     return render(request,'accounts/registration.html',{'form':form})
