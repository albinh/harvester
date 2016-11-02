from django.conf.urls import url

from . import views
from . import ajax_views
urlpatterns = [

	url(r'^harvests/new$',                          views.HarvestNew.as_view(),                     name='harvest-new',),
	url(r'^harvests/(?P<pk>\d+)/$',                 views.HarvestEdit.as_view(),                    name='harvest-update',),
    url(r'^harvests/$',                             views.HarvestList.as_view(),                    name='harvest-list'),

	url(r'^deliveries/$',                           views.DeliveryList.as_view(),                   name='delivery-list'),
    url(r'^deliveries/new$',                        views.DeliveryNew.as_view(),                    name='delivery-new'),
    url(r'^deliveries/(?P<pk>\d+)/$',               views.DeliveryEdit.as_view(),                   name='delivery-edit', ),



    url(r'^customer_categories/',                   views.CustomerCategoryList.as_view(),           name='cusstomer-categories-list'),
	url(r'^customer_categories/(?P<pk>\d+)/$',      views.CustomerCategoryEdit.as_view(),           name='customer-category-edit'),



	url(r'^crops/$',                                views.CropList.as_view(),                       name='crop-list'),
	url(r'^crops/(?P<pk>\d+)/$',                    views.CropEdit.as_view(),                       name='crop-edit'),

	url(r'^ajax/crop/cultures$', 					 ajax_views.get_cultures_and_target_by_crop, 				name='get_cultures_and_target_by_crop'),
	url(r'^ajax/crop/(?P<crop_id>\d+)/orderunits/$', ajax_views.orderunits_by_crop, 				name='ajax_orderunits_by_crop'),
	url(r'^ajax/crop/(\d+)/crop_forms_and_price$',	 ajax_views.crop_forms_and_price, 				 name='data_crop_forms_and_price'),



]