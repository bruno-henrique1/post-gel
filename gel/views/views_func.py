from gel.models import faq, category
from django.http import JsonResponse
from django.db.models import Sum, Count
import json

def retorna_total_faq(request):
    total = faq.objects.all().aggregate(Count('id'))['id__count']
    if request.method == "GET":
        return JsonResponse({'id': total})
    

def get_category_counts(request):
    if request.method == "GET":
        categories_with_counts = category.objects.annotate(num_faqs=Count('faq'))
        results = [{'name': category.name, 'num_faqs': category.num_faqs} 
                   for category in categories_with_counts]

        labels = [category['name'] for category in results]
        data_values = [category['num_faqs'] for category in results]
        new_data = {"labels": labels, "data": data_values}

        return JsonResponse(new_data)
    




"""def get_category_counts(request):
        total = category.objects.annotate(num_faqs=Count('faq'))['category_id']
        if request.method == "GET":
            return JsonResponse(total)"""
        
        #return category.objects.annotate(num_faqs=Count('gelfaq'))