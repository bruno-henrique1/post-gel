from gel.models import faq, category, location
from django.http import JsonResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required

@login_required(login_url='gel:register')
def retorna_total_faq(request):
    total = faq.objects.all().aggregate(Count('id'))['id__count']
    if request.method == "GET":
        return JsonResponse({'id': total})
    
@login_required(login_url='gel:login')
def get_category_counts(request):
    if request.method == "GET":
        categories_with_counts = category.objects.annotate(num_faqs=Count('faq'))
        results = [{'name': category.name, 'num_faqs': category.num_faqs} 
                   for category in categories_with_counts]

        labels = [category['name'] for category in results]
        data_values = [category['num_faqs'] for category in results]
        new_data = {"labels": labels, "data": data_values}

        return JsonResponse(new_data)

@login_required(login_url='gel:login')
def get_location_counts(request):
    if request.method == "GET":
        locations_with_counts = location.objects.annotate(num_faqs=Count('faq'))
        results = [{'name': location.bairro, 'num_faqs': location.num_faqs} 
                   for location in locations_with_counts]
        labels = [location['name'] for location in results]
        data_values = [location['num_faqs'] for location in results]
        new_data = {"labels": labels, "data": data_values}
        return JsonResponse(new_data)
