from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Purchase, Transaction, Product
from prof.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import json
from decimal import Decimal

def home(request):
    return render(request, "core/home.html", {})

def product_list(request):
    parts = Product.objects.all()
    return render(request, 'core/product_list.html', {'parts': parts})

def aboutus(request):
    return render(request, 'core/AboutUs.html')

def contact(request):
    return render(request, 'core/Contact.html')

@csrf_exempt
def checkout(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cart_items = data.get('cart_items', [])
            discount = data.get('discount', 0)
            user_id = data.get('user_id')  # Assuming user_id is passed in the request
            print(user_id)
            if not cart_items:
                return JsonResponse({'error': 'No items in the cart'}, status=400)

            # Fetch user profile
            try:
                user_profile = UserProfile.objects.get(user__id=user_id)
            except UserProfile.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)

            # Retrieve products from the cart items
            products = Product.objects.filter(id__in=cart_items)

            if not products.exists():
                return JsonResponse({'error': 'Invalid cart items'}, status=400)

            # Create a Purchase instance
            purchase = Purchase.objects.create(user=user_profile)
            purchase.products.set(products)
            purchase.save()

            # Create a Transaction instance
            transaction = Transaction.objects.create(
                user=user_profile,
                purchase=purchase,
                discount=discount
            )
            transaction.save()

            return JsonResponse({'message': 'Checkout successful!'})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        except ObjectDoesNotExist as e:
            return JsonResponse({'error': str(e)}, status=404)

        except Exception as e:
            # Log the exception for debugging
            print(e)
            return JsonResponse({'error': 'Something went wrong'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)