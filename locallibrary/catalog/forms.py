from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime
from .models import BookInstance
from django.forms import ModelForm

class RenewBookModelForm(ModelForm):
    def clean_due_back(self):
       data = self.cleaned_data['due_back']

       if data < datetime.date.today():
           raise ValidationError(_('Invalid date - renewal in past'))

       if data > datetime.date.today() + datetime.timedelta(weeks=4):
           raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

       return data

    class Meta:
        model = BookInstance
        fields = ['due_back',]
        labels = { 'due_back': _('Renewal date'), }
        help_texts = { 'due_back': _('Enter a date between now and 4 weeks (default 3).'), }



class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")