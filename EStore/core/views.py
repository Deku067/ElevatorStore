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


# @csrf_exempt
# def Add_to_cart(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             user_id = data.get('user_id')
#             product_id = data.get('productid')
            
#             # Check if user_id and product_id are provided
#             if not user_id or not product_id:
#                 return JsonResponse({'error': 'user_id and productid are required'}, status=400)
            
#             # Fetch user profile
#             try:
#                 user_profile = UserProfile.objects.get(user__id=user_id)
#             except UserProfile.DoesNotExist:
#                 return JsonResponse({'error': 'User not found'}, status=404)

#             # Fetch product
#             try:
#                 product = Product.objects.get(id=product_id)
#             except Product.DoesNotExist:
#                 return JsonResponse({'error': 'Product not found'}, status=404)

#             # Create a Purchase instance
#             Purchase.objects.create(user=user_profile, product=product)

#             return JsonResponse({'message': 'Add successful!'})

#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON'}, status=400)
#         except Exception as e:
#             # Log the exception for debugging
#             # You should log the exception e here using Django's logging framework
#             return JsonResponse({'error': 'Something went wrong', 'details': str(e)}, status=500)

#     return JsonResponse({'error': 'Invalid request method'}, status=405)

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

            # Check if a purchase already exists for the user
            try:
                purchase = Purchase.objects.get(user=user_profile)
                # Update existing purchase with new products
                purchase.products.set(products)
                purchase.save()
            except Purchase.DoesNotExist:
                # Create a new purchase if it doesn't exist
                purchase = Purchase.objects.create(user=user_profile)
                purchase.products.set(products)
                purchase.save()

            # Create a new Transaction instance
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