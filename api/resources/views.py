from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from resources.models import Category, Expense
from resources.serializers import CategorySerializer, ExpenseSerializer

@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data)
    
    elif request.method == 'DELETE':
        category.delete()
        return HttpResponse(status=204)
    
    else:
        return HttpResponse(status=400)

@csrf_exempt
def expense_list(request):
    if request.method == 'GET':
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExpenseSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def expense_detail(request, pk):
    try:
        expense = Expense.objects.get(pk=pk)
    except Expense.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ExpenseSerializer(expense)
        return JsonResponse(serializer.data)
    
    elif request.method == 'DELETE':
        expense.delete()
        return HttpResponse(status=204)
    
    else:
        return HttpResponse(status=400)

@csrf_exempt
def category_expenses(request, pk):
    if request.method == 'GET':
        expenses = Expense.objects.filter(category_id=pk)
        serializer = ExpenseSerializer(expenses, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    else:
        return HttpResponse(status=400)
