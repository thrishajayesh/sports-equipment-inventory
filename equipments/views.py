from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Equipment

# Home Page
def home(request):
    return render(request, 'equipments/home.html')

# Task 8a: User Signup
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('equipment_list')
    else:
        form = UserCreationForm()
    return render(request, 'equipments/signup.html', {'form': form})

# Task 8b & 8d: User Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('equipment_list')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'equipments/login.html', {'form': form})

# Task 9a: User Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Task 5 & 9c: READ - View All Equipment (Protected)
@login_required
def equipment_list(request):
    items = Equipment.objects.all()
    return render(request, 'equipments/equipment_list.html', {'items': items})

# Task 4 & Task 2e: CREATE - Add Equipment (Protected)
@login_required
def equipment_add(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        sport = request.POST.get('sport')
        brand = request.POST.get('brand')
        price = request.POST.get('price')

        Equipment.objects.create(
            item_name=item_name,
            sport=sport,
            brand=brand,
            price=price
        )
        return redirect('equipment_list')
    return render(request, 'equipments/equipment_form.html')

# Task 6: UPDATE - Edit Equipment (Protected)
@login_required
def equipment_edit(request, pk):
    item = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        item.item_name = request.POST.get('item_name')
        item.sport = request.POST.get('sport')
        item.brand = request.POST.get('brand')
        item.price = request.POST.get('price')
        item.save()
        return redirect('equipment_list')
    return render(request, 'equipments/equipment_form.html', {'item': item})

# Task 7: DELETE - Remove Equipment (Protected)
@login_required
def equipment_delete(request, pk):
    item = get_object_or_404(Equipment, pk=pk)
    item.delete()
    return redirect('equipment_list')