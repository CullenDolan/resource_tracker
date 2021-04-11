from django.forms import ModelForm
from .models import Provider

class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = ['epic_id','prov_fname','prov_midinital','prov_lname','prov_division',
                'prov_department', 'prov_department','prov_email', 'prov_hospital']