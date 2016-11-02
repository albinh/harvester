from django.shortcuts import render
from django.http import HttpResponse


from .models import CropForm
from .models import Culture
from .models import Crop
from .models import DeliverySingle

import simplejson
from django.http import HttpResponseRedirect
# Create your views here.

def orderunits_by_crop(request, crop_id):


    # With the sector_id you know wich sector the user has selected
    # You should generate the list based in your needs
    data = []
    if crop_id:
        crop_forms = CropForm.objects.filter(crop=crop_id)

        # Then make loop over all sectors
        for crop_form in crop_forms:
            # To get the sector name you should use another dict
            # I think you already have it in USER_PROFILE_CURRENT_SECTOR_TYPES
            # Remember to import it (check above)
            # We append the id and the name to replace options in the HTML
            data.append({'id':crop_form.id, 'name':crop_form.__str__()})

        response = { 'item_list':data }  # We send back the list
        return HttpResponse(simplejson.dumps(response))

    # If we get any error, or cannot get the sector, we send an empty response
    response = {}
    return HttpResponse(simplejson.dumps(response))


def get_cultures_and_target_by_crop(request):
    response = []
    try:
        crop_id = int(request.POST['crop_id'])
    except ValueError:
        crop_id=None

    # With the sector_id you know wich sector the user has selected
    # You should generate the list based in your needs
    culture_data = []
    delivery_data    = []
    if crop_id:
        cultures = Culture.objects.filter(crop=crop_id)
        deliveries = DeliverySingle.objects.filter(deliveryitem__crop_form__crop=crop_id)
        print ("DDD")
        print (deliveries)
        print ("#")
        for delivery in deliveries:
            delivery_data.append({'id':delivery.id, 'name':delivery.__str__()})

        for culture in cultures:
            culture_data.append({'id':culture.id, 'name':culture.__str__()})

        response = { 'cultures':culture_data,'deliveries':delivery_data }  # We send back the list
        return HttpResponse(simplejson.dumps(response))

    # If we get any error, or cannot get the sector, we send an empty response
    response = {}
    return HttpResponse(simplejson.dumps(response))


def crop_forms_and_price(request, customer):
    customer=Customer.objects.get(pk=customer)

    for crop in Crop.objects.all():
        for crop_form in CropForms.objects.filter(crop=crop):
            p=customer.pricelist_item_set.get(crop_form=crop_form)
            print (p)

