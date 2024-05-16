from django.shortcuts import render
from .models import reservation, menu_items, FeedBack
from django.http import HttpResponse
from datetime import datetime
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def menu(request):
    menuItems = menu_items.objects.all()
    unique_categories = menu_items.objects.values_list('category', flat=True).distinct()
    categorized_data = {}

    # Iterate over each unique category
    for category in unique_categories:
        # Filter objects belonging to the current category
        category_objects = menuItems.filter(category=category)
        # Sort the objects within the category (optional, depends on your requirement)
        sorted_category_objects = category_objects.order_by('category')
        # Store the sorted objects in the dictionary
        categorized_data[category] = sorted_category_objects
    # print(categorized_data)
    starters = categorized_data['Starter']
    mains = categorized_data['Mains']
    desserts = categorized_data['Desserts']
    drinks = categorized_data['Drinks']
    print(starters, mains, desserts, drinks)
    return render(request, "menu.html", {
        # "items":menuItems
        "starters":starters,
        "mains":mains,
        "desserts":desserts,
        "drinks":drinks
    })

def reservations(request):
    return render(request, "reservations.html")

def feedback(request):
    return render(request, "feedback.html")


def redirect_reservations(request):
    data = request.POST
    name = data['rame']
    phone = data['rphone']
    date = data['rdate']
    party_size = data['rparty-size']
    info = data['radd-info']
    date_object = datetime.strptime(date, '%d/%m/%y')
    django_date = timezone.make_aware(date_object)
    # print(name, phone, date, party_size, info)
    reservation_model = reservation(name=name, contact_number=phone, date=django_date, party_size=party_size, additional_information=info)
    reservation_model.save()
    # return HttpResponse("Redirecting")
    return render(request, "reservations_redirect.html", {
        "res":"Thank you for the reservation"
    })

def redirect_feedback(request):
    data = request.POST
    name = data['rame']
    phone = data['rphone']
    date = data['rdate']
    info = data['radd-info']
    date_object = datetime.strptime(date, '%d/%m/%y')
    django_date = timezone.make_aware(date_object)
    print(name, phone, date, info)
    feedb = FeedBack(name=name, contact_number=phone, date=django_date, feedback_model=info)
    feedb.save()
    # feedback_model = feedback(u_name=name, contact_number=phone, date=django_date, feedback_info=info)
    # feedback_model.save()
    # return HttpResponse("Redirecting to feedback")
    return render(request, "feedback_redirect.html", {
        "feed":"Thank you for you valuable feedback"
    })