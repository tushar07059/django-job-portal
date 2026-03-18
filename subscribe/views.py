from django.shortcuts import render
from subscribe.models import Subscribe
from subscribe.forms import SubscribeForm
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
def subscribe(request):
    subscribe_form= SubscribeForm
    if request.POST:
        subscribe_form=SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            # print("Valid form ")
            # print(subscribe_form.cleaned_data)
            # email=subscribe_form.cleaned_data['email']
            # name=subscribe_form.cleaned_data['name']
            # subscribe=Subscribe(name=name,email=email)
            # subscribe.save()
            return redirect(reverse('thank_you')) 
            
    context={"form":subscribe_form}
    return render(request,'subscribe/home.html',context)

def thank_you(request):
    context={}
    return render(request,'subscribe/thank_you.html',context)