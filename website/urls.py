from django.urls import path
from .views import home,about,service,data_collection,blog,blog_details,contact,gcp,azure,aws,consolidation,activation,dashboarding,segmentation,ds_usecase

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('service', service, name='service'),
    path('data_collection', data_collection, name='data_collection'),
    path('blog', blog, name='blog'),
    path('blogdetails', blog_details, name='blog_details'),
    path('contact', contact, name='contact'),
    path('gcp', gcp, name='gcp'),
    path('azure', azure, name='azure'),
    path('aws', aws, name='aws'),

    path('consolidation', consolidation, name='consolidation'),
    path('activation', activation, name='activation'),
    path('dashboarding', dashboarding, name='dashboarding'),
    path('segmentation', segmentation, name='segmentation'),
    path('ds_usecase', ds_usecase, name='ds_usecase')
]