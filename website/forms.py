from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

class DHForm(forms.Form):

  def addError(self, message):
    self._errors[NON_FIELD_ERRORS] = self.error_class([message])
    

class ContactForm(DHForm):
  
  name = forms.CharField(
    required = True
  )
  
  email = forms.EmailField(
    required = True
  )
  
  message = forms.CharField(widget=forms.Textarea,
                            required=True)
