from django.shortcuts import render, get_object_or_404
from .models import Item,Sv,Category,City
from django.db.models import Q
# import speech_recognition as sr
import pyttsx3
# import openai
from django.http import JsonResponse
from gradio_client import Client
from django.shortcuts import render
import logging
from django.http import JsonResponse
from requests.exceptions import RequestException  # Import specific exceptions if needed




# Create your views here.
def index(request):
    categories = Category.objects.all()
    cities = City.objects.all()
    
    context = {
        'categories': categories,
        'cities': cities,
    }
    return render(request, 'index.html',context)

def i_am_a_tourist(request):
    item = Sv.objects.all()
    return render(request, 'i_am_a_tourist.html',{
        'item': item,
    })

def detailtor(request, pk):
    item = get_object_or_404(Sv, pk=pk)
    return render(request, 'detailtor.html',{
        'item': item,
    })

def search(request):
    query = request.GET.get('query')
    category_id = request.GET.get('category')
    city_id = request.GET.get('city')

    results = Item.objects.all()

    if query:
        results = results.filter(name__icontains=query)

    if category_id:
        results = results.filter(category_id=category_id)

    if city_id:
        results = results.filter(city_id=city_id)

    categories = Category.objects.all()
    cities = City.objects.all()

    context = {
        'results': results,
        'query': query,
        'category_selected': int(category_id) if category_id else None,
        'city_selected': int(city_id) if city_id else None,
        'categories': categories,
        'cities': cities,
    }
    return render(request, 'index.html', context)

# def usearch(request):
#     query = request.GET.get('query')
#     category_id = request.GET.get('category')
#     city_id =  request.GET.get('city')

#     results = Item.objects.all()

#     if query:
#         results = results.filter(Q(name__icontains=query))

#     if category_id:
#         results = results.filter(category_id=category_id)
        
#     if city_id:
#         results = results.filter(city_id=city_id)

#     context = {
#         'results': results,
#         'query': query
#     }
#     return render(request, 'tr_in_blocks.html', context)

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    result = None  # Initializing result with a default value

    if request.method == 'POST':
        message = request.POST.get('message')
        mode = request.POST.get('mode')
        file_url = request.POST.get('file_url')

        if not file_url:  # Check if file_url is empty or not provided
            file_url = None  # Set file_url to None if not provided

        client = Client("http://127.0.0.1:8001/")
        result = client.predict(message, mode, file_url, api_name="/chat")

    return render(request, 'detail.html', {
        'item': item,
        'result': result,
        # Include result in the context passed to the render function
    })

# def tr_in_blocks(request):
    
#     return render(request, 'tr_in_blocks.html')



# def lm(request):
#     try:
#         client = Client("http://127.0.0.1:8001/")
#         result = client.predict(
#             "Hello!!",
#             "Query Docs",
#             ["https://github.com/gradio-app/gradio/raw/main/test/test_files/sample_file.pdf"],
#             api_name="/chat"
#         )
#         # Log the result for debugging purposes
#         logging.info(result)
#     except Exception as e:
#         # Log any exceptions that might occur during the request
#         logging.error(f"An error occurred: {e}")
    
#     return render(request, 'lm.html')

def upload_file(request):
    if request.method == 'POST':
        file_url = request.POST.get('file_url')  # Assuming input field name is 'file_url'
        client = Client("http://127.0.0.1:8001/")
        result = client.predict([file_url], api_name="/_upload_file")
        return render(request, 'result.html', {'result': result})
    return render(request, 'upload_file.html')


def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        mode = request.POST.get('mode')
        file_url = request.POST.get('file_url')

        if not file_url:  # Check if file_url is empty or not provided
            file_url = None  # Set file_url to None if not provided

        try:
            client = Client("http://127.0.0.1:8001/")
            result = client.predict(message, mode, file_url, api_name="/chat")
            return render(request, 'result.html', {'result': result})

        except Exception as e:
            # Handle the exception: Log it, display an error message, or perform other actions
            error_message = f"An error occurred: {str(e)}"
            return render(request, 'error.html', {'error_message': error_message})
    
    return render(request, 'chat.html')




def heartbeat(request):
    data = request.POST  # Accessing POST data

    # Accessing the 'heartbeat' key in the POST data
    try:
        status = data['heartbeat']
        response = {'status': status}
        return JsonResponse(response)
    except KeyError as e:
        error_message = f"KeyError: {e}"
        return JsonResponse({'error': error_message}, status=400)
    







