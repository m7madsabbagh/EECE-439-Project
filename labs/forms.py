from django import forms
from .models import Contacts
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contacts
        fields= ('contact_id','name','address','profession','email','tel')
    def clean_tel(self):
        tel = self.cleaned_data['tel']
        if tel < 0:
            raise forms.ValidationError("Tel cannot be negative.")
        return tel   
         
    
class BalanceUpdateForm(forms.ModelForm):
     class Meta:
        model=Contacts
        fields= ('contact_id','name','address','profession','email','tel')
     def clean_tel(self):
        tel = self.cleaned_data['tel']
        if tel < 0:
            raise forms.ValidationError("Tel cannot be negative.")
        return tel  
    