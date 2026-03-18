from django import forms
from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        error_messages={
            'name':{
                'required':("You can't move forward without first name.")
        
            }
        }

    
# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError("Invalid name!")
#     return value


    
# class SubsribeForm(forms.Form):
#     name=forms.CharField(max_length=100 ,validators=[validate_comma])
#     email=forms.EmailField(max_length=100 )

    # def clean_name(self):
    #    data=self.cleaned_data['name']
    #    if "," in data:
    #             raise forms.ValidationError("Invalid name!")
    #    return data 