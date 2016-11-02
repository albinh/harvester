from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, ListView
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from .models import *
from .forms import *



class DeliveryEdit(UpdateView):
    model = DeliverySingle
    form_class = DeliverySingleForm
    template_name = 'harvester/delivery-edit.html'



    def get_obj(self):
        return self.get_object()

    def get(self, request, *args, **kwargs):
        self.object = self.get_obj()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        delivery_item_form = DeliveryItemFormSet(instance=self.object, )

        for form2 in delivery_item_form.forms:
            print (form2.instance.pk)
            if form2.instance.pk:
                form2.initial['crop'] = form2.instance.crop_form.crop

        return self.render_to_response(
            self.get_context_data(form=form,
                                  delivery_item_form=delivery_item_form,
                                  ))


    def post(self, request, *args, **kwargs):
        self.object = self.get_obj()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        delivery_item_form = DeliveryItemFormSet(self.request.POST,instance=self.object)


        if (form.is_valid() and delivery_item_form.is_valid()):
            return self.form_valid(form, delivery_item_form)
        else:
            return self.form_invalid(form, delivery_item_form)


    def form_valid(self, form, delivery_item_form):
        self.object = form.save()
        delivery_item_form.instance = self.object
        delivery_item_form.save()
        return HttpResponseRedirect(self.get_success_url())


    def form_invalid(self, form, delivery_item_form):
        print ("invalid")
        print (form.is_valid())
        print (delivery_item_form.is_valid())
        print (form.errors)
        print ("A")

        print (delivery_item_form.errors)
        print ("B")
        return self.render_to_response(
            self.get_context_data(form=form,
                                  delivery_item_form=delivery_item_form
                                  ))


    def get_success_url(self):
        return reverse('harvest-list')


    def get_initial(self):
        return {'time': timezone.now()}



class DeliveryNew(CreateView):
    model = DeliverySingle
    form_class = DeliverySingleForm
    template_name = 'harvester/delivery-edit.html'



    def get_obj(self):
        return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_obj()
        form_class = self.get_form_class()
        form = self.get_form(form_class)


        delivery_item_form = DeliveryItemFormSet(instance=self.object)

        return self.render_to_response(
            self.get_context_data(form=form,
                                  delivery_item_form=delivery_item_form,
                                  ))


    def post(self, request, *args, **kwargs):
        self.object = self.get_obj()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        delivery_item_form = DeliveryItemFormSet(self.request.POST)

        if (form.is_valid() and delivery_item_form.is_valid()):
            return self.form_valid(form, delivery_item_form)
        else:
            return self.form_invalid(form, delivery_item_form)


    def form_valid(self, form, delivery_item_form):
        self.object = form.save()
        delivery_item_form.instance = self.object
        delivery_item_form.save()
        return HttpResponseRedirect(self.get_success_url())


    def form_invalid(self, form, delivery_item_form):
        print ("invalid")
        print (form.is_valid())
        print (delivery_item_form.is_valid())
        print (form.errors)
        return self.render_to_response(
            self.get_context_data(form=form,
                                  delivery_item_form=delivery_item_form
                                  ))


    def get_success_url(self):
        return reverse('harvest-list')


    def get_initial(self):
        return {'time': timezone.now()}


class HarvestNew(CreateView):
    model = HarvestItem
    form_class = HarvestItemForm
    template_name = 'harvester/harvest-edit.html'
    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        print ("asdf")
        print ("asdf")
        print (request.GET)
        if 'delivery_item' in request.GET:
            print (request.GET.get('delivery_item'))
            delivery=get_object_or_404(DeliveryItem,pk=request.GET.get('delivery_item'))

            print (delivery.crop_form.crop)
            form.initial['crop'] = delivery.crop_form.crop.id
            form.initial['cropform'] = delivery.crop_form.id
            form.initial['destination'] = delivery.delivery.id
            print (delivery.delivery.id)
            print ("---")

        return self.render_to_response(
            self.get_context_data(form=form,

                                  ))

    def success_url(self):
        return reverse(harvest-list)







class HarvestEdit(UpdateView):
    model = HarvestItem
    form_class = HarvestItemFormUpdate
    template_name = 'harvester/harvest-edit.html'

class CustomerCategoryList(ListView):
    model=CustomerCategory

class CustomerCategoryEdit(UpdateView):
    model=CustomerCategory

class CropList(ListView):
    model=Crop

    template_name='harvester/crop-list.html'

class CropEdit(UpdateView):
    model=Crop
    form_class = CropFormForm
    template_name= 'harvester/crop-edit.html'
    def get_obj(self):
        return self.get_object()
    def get(self, request, *args, **kwargs):
        self.object = self.get_obj()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        cropform_form = CropFormFormSet(instance=self.object)

        return self.render_to_response(
            self.get_context_data(form=form,
                                  cropform_form=cropform_form,
                                  ))


    def post(self, request, *args, **kwargs):
        self.object = self.get_obj()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        cropform_form = CropFormFormSet(self.request.POST)
        print (cropform_form)
        if (form.is_valid() and cropform_form.is_valid()):
            return self.form_valid(form, cropform_form)
        else:
            return self.form_invalid(form, cropform_form)


    def form_valid(self, form, cropform_form):
        self.object = form.save()
        cropform_form.instance = self.object
        cropform_form.save()
        return HttpResponseRedirect(self.get_success_url())


    def form_invalid(self, form, cropform_form):

        return self.render_to_response(
            self.get_context_data(form=form,
                                  cropform_form=cropform_form
                                  ))


    def get_success_url(self):
        return reverse('harvest-new')


    def get_initial(self):
        return {'time': timezone.now()}


class HarvestList(ListView):
    template_name = 'harvester/harvest-list.html'
    model = HarvestItem

    def get_context_data(self, **kwargs):
        context = super(HarvestList, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class DeliveryList(ListView):
    template_name = 'harvester/delivery-list.html'
    model = DeliverySingle

