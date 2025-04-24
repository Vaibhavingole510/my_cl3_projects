from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def search_result(request):
    query = request.GET.get('q', '').strip()  # Get search term & remove spaces
    products = Product.objects.none()  # Default empty queryset

    if query:  
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    return render(request, 'search.html', {'query': query, 'products': products})
