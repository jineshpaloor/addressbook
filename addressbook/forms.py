from django.forms import ModelForm
from addressbook.models import Address

class AddressForm(ModelForm):
    class Meta:
        model = Address

