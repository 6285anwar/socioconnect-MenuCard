from django.shortcuts import render

# Create your views here.
def restaurant_dashboard(request):
    return render(request, 'restaurants/restaurant_dashboard.html')