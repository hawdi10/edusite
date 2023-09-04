from django.shortcuts import render
from django.views import View
# Create your views here.
class register(View):
    def get(self, request):
        register_data = forms.register_form
        return render(request, "signup.html", {"register_form": register_data})

    def post(self, request):
        register_data1 = forms.register_form(request.POST)
        if register_data1.is_valid():
            username_data = register_data1.cleaned_data.get("username")
            password_data = register_data1.cleaned_data.get("password")
            confirm_data = register_data1.cleaned_data.get("confirm")
            user_final = user(username=username_data,
                              last_name=confirm_data,
                              )
            user_final.set_password(password_data)
            user_final.save()
            return redirect("/")