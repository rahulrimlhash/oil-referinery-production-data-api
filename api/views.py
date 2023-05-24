from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import AnnualData
# from api.views import process_data

# Create your views here.
import pandas as pd

def process_data():
    data = pd.read_excel('data.xls')
    print(data.columns)
    # Group by API WELL NUMBER and calculate the annual data
    annual_data = data.groupby('API WELL  NUMBER').sum()

    # Convert the DataFrame to a list of dictionaries
    annual_data_list = annual_data.reset_index().to_dict('records')

    return annual_data_list

# class LoadDataView(View):
#     def get(self, request):
#         processed_data = process_data()
#
#         # Clear existing data from the database
#         AnnualData.objects.all().delete()
#
#         # Load processed data into the database
#         for item in processed_data:
#             AnnualData.objects.create(well=item['API WELL NUMBER'], oil=item['OIL'], gas=item['GAS'], brine=item['BRINE'])
#
#         return HttpResponse("Data loaded successfully!")
