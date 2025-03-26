from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def dashboard(request):
    data = [
        {"title": "Users", "count": 150},
        {"title": "Orders", "count": 320}, 
        {"title": "Revenue", "count": "₱12,450"}
    ]
    return render(request, 'pages/dashboard.html', {'data': data})