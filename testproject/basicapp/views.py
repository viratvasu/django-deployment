from django.shortcuts import render
from basicapp.models import user_data
from basicapp.models import user_data
from . import forms
# Create your views here.
def index(request):
    user_list=user_data.objects.order_by('first_name')
    my_dict={'insert_me':user_list}
    return render(request,'basicapp/index.html',context=my_dict)

def form_view(request):
    form=forms.FormName()
    if request.method=='POST':
        form=forms.FormName(request.POST)
        if form.is_valid():
            print("validation successfull...")
            user=user_data.objects.get_or_create(first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],email=form.cleaned_data['email'])[0]
    return render(request,'basicapp/form_page.html',{'form':form})
