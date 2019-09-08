from django.urls import path
from . import views

# it is super important that the names in the urlpatterns
# are unique, since we are using them to route to the
# specific locations on our page

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
