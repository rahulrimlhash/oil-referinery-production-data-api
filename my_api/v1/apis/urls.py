from django.urls import path
from my_api.v1.apis import views

urlpatterns = [
    path('load-data/', views.LoadDataView.as_view(), name='load-data'),
    path('data/', views.get_annual_data, name='get-data'),
]