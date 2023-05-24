from django.views import View
from api.views import process_data

from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from api.models import AnnualData


class LoadDataView(View):
    def get(self, request):
        processed_data = process_data()

        # Clear existing data from the database
        AnnualData.objects.all().delete()

        # Load processed data into the database
        for item in processed_data:
            AnnualData.objects.create(well=item['API WELL  NUMBER'], oil=item['OIL'], gas=item['GAS'], brine=item['BRINE'])

        return HttpResponse("Data loaded successfully!")

def get_annual_data(request):
    well = request.GET.get('well')
    print(well)
    annual_data = get_object_or_404(AnnualData, well=well)
    data = {
            'oil': annual_data.oil,
            'gas': annual_data.gas,
            'brine': annual_data.brine,
        }

    return JsonResponse(data)