from django import forms

from django.forms import ModelChoiceField
from .models import Crop
from .models import CropForm
from .models import Culture
from .models import DeliverySingle
from .models import HarvestItem
from .models import DeliveryItem
import floppyforms


from django.forms import ModelForm
from clever_selects.form_fields import ChainedModelChoiceField
from clever_selects.form_fields import ChainedChoiceField
from clever_selects.forms import ChainedChoicesForm
from clever_selects.forms import ChainedChoicesModelForm
from django.forms.models import inlineformset_factory
from django.urls import reverse_lazy


class HarvestItemForm(ModelForm):
    qs=Crop.objects.all()

    crops = [(cc.id,cc.crop) for cc in qs]
    crops = crops+crops
    print (crops)


    crop = forms.ChoiceField(choices=crops, widget=forms.Select(attrs={'onchange': 'get_cultures();'}))
    culture_is_done = forms.BooleanField(required=False)

    class Meta:
        model = HarvestItem
        fields = ['culture', 'time', 'harvested_length', 'comment', 'destination']

        widgets = {
            'comment': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }


class HarvestItemFormUpdate(ModelForm):
    # fields = ['culture', 'weight','count','comment','time']
    error_css_class = "uk-form-danger"
    class Meta:
        model = HarvestItem
        fields = ['culture', 'time', 'harvested_length', 'comment', 'destination']

        widgets = {
            'comment': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }

class DeliverySingleForm(ModelForm):
    error_css_class = "uk-form-danger"
    class Meta:
        model = DeliverySingle
        fields = ['customer','target_date']

class DeliveryItemForm(ModelForm):
    crop = forms.ModelChoiceField(queryset=Crop.objects.all())
    print ("QQQ")

    class Meta:
        exclude = []
        model = DeliverySingle

class CropFormForm(ModelForm):
    class Meta:
        model=Crop
        exclude=[]


DeliveryItemFormSet    = inlineformset_factory(DeliverySingle, DeliveryItem,  form=DeliveryItemForm, exclude=[], extra=20)
CropFormFormSet = inlineformset_factory(Crop,CropForm,exclude=[],extra=5,can_delete=True)