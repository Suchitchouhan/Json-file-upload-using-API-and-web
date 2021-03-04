from django.shortcuts import render
import json
from .models import *
import json
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from rest_framework.response import Response

# Create your views here.
# It will upload the json into database by web
def index(request):
	context={}
	if request.method == "POST":
		file=request.FILES['file']
		print(file)
		data = json.load(file)
		for x in data:
			print(x)
			accountO,__=account.objects.get_or_create(Ido=x['_id']['$oid'])
			accountO.user_idO=x['user_id']
			accountO.amount=x['amount']
			accountO.coins_balance=x['coins_balance']
			accountO.txn_type=x['txn_type']
			accountO.txn_info=x['txn_info']
			accountO.action=x['action']
			accountO.time=x['time']
			accountO.save()
		context['status']="Data is successfully uploaded"
		acc=account.objects.all()
		context['account']=acc	
		return render(request,'account/index.html',context)
	else:
		acc=account.objects.all()
		context['account']=acc	
		return render(request,'account/index.html',context)



# It will upload the json into database by api
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def upload_data(request):
	context={}
	file=request.FILES['file']
	data = json.load(file)
	for x in data:
		print(x)
		accountO,__=account.objects.get_or_create(Ido=x['_id']['$oid'])
		accountO.user_idO=x['user_id']
		accountO.amount=x['amount']
		accountO.coins_balance=x['coins_balance']
		accountO.txn_type=x['txn_type']
		accountO.txn_info=x['txn_info']
		accountO.action=x['action']
		accountO.time=x['time']
		accountO.save()
	context['status']="Data is successfully uploaded"
	return HttpResponse(json.dumps(context), content_type='application/json')	


# It will get all data by api
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def get_all_data(request):
	context={}
	data=[]
	for x in account.objects.all():
		data.append(x.as_dict())
	context['data']=data
	print(context)
	return HttpResponse(json.dumps(context), content_type='application/json')	



#it will create acount data one by one using api 
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def create_data(request):
	context={}
	Ido=request.data.get('Ido')
	user_idO=request.data.get('user_idO')
	amount=request.data.get('amount')
	coins_balance=request.data.get('coins_balance')
	txn_type=request.data.get('txn_type')
	txn_info=request.data.get('txn_info')
	action=request.data.get('action')
	time=request.data.get('time')
	accountO=account.objects.create(Ido=Ido)
	accountO.user_idO=user_idO
	accountO.amount=amount
	accountO.coins_balance=coins_balance
	accountO.txn_type=txn_type
	accountO.txn_info=txn_info
	accountO.action=action
	accountO.time=time
	accountO.save()
	context['status']="Data inserted successfully"
	return HttpResponse(json.dumps(context), content_type='application/json')	


#it will update acount data one by one using api 

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def update_data(request):
	context={}
	Ido=request.data.get('Ido')
	user_idO=request.data.get('user_idO')
	amount=request.data.get('amount')
	coins_balance=request.data.get('coins_balance')
	txn_type=request.data.get('txn_type')
	txn_info=request.data.get('txn_info')
	action=request.data.get('action')
	time=request.data.get('time')
	if account.objects.filter(Ido=Ido).exists():
		accountO=account.objects.get(Ido=Ido)
		accountO.user_idO=user_idO
		accountO.amount=amount
		accountO.coins_balance=coins_balance
		accountO.txn_type=txn_type
		accountO.txn_info=txn_info
		accountO.action=action
		accountO.time=time
		accountO.save()
		context['status']="Data inserted successfully"
	else:
		context['status']="Id is not exists"	
	return HttpResponse(json.dumps(context), content_type='application/json')	


#it will delete acount data one by one using api 
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def delete_data(request):
	context={}
	Ido=request.data.get('Ido')
	if account.objects.filter(Ido=Ido).exists():
		accountO=account.objects.get(Ido=Ido)
		account.delete()
		context['status']="Data deleted successfully"
	else:
		context['status']="Id is not exists"	
	return HttpResponse(json.dumps(context), content_type='application/json')	




#its will search the data by id using api
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def search_data_by_id(request):
	context={}
	Ido=request.data.get('Ido')
	if account.objects.filter(Ido=Ido).exists():
		accountO=account.objects.get(Ido=Ido)
		context['amount']=accountO.as_dict()
	else:
		context['status']="Id is not exists"	
	return HttpResponse(json.dumps(context), content_type='application/json')	


#its will search the data by time using api

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def search_data_by_time(request):
	context={}
	time=request.data.get('time')
	if account.objects.filter(time=time).exists():
		accountO=account.objects.filter(time=time)
		account=[]
		for x in account:
			account.append(x.as_dict())
		context['amount']=account	
	else:
		context['status']="Id is not exists"	
	return HttpResponse(json.dumps(context), content_type='application/json')	


#its will search the data between lower amount and uppar amount using api

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def search_data_by_amount(request):
	context={}
	lower_amount=request.data.get('lower_amount')
	upper_amount=request.data.get('upper_amount')
	accountO=account.objects.filter(amount__gte=lower_amount,amount__lte=upper_amount)
	account=[]
	for x in account:
		account.append(x.as_dict())
	context['amount']=account	
	return HttpResponse(json.dumps(context), content_type='application/json')	

#its will search the data between lower coins_balance and uppar coins_balance using api
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def search_data_by_coins_balance(request):
	context={}
	lower_coins_balance=request.data.get('lower_coins_balance')
	upper_coins_balance=request.data.get('upper_coins_balance')
	accountO=account.objects.filter(coins_balance__gte=lower_coins_balance,coins_balance__lte=upper_coins_balance)
	account=[]
	for x in account:
		account.append(x.as_dict())
	context['amount']=account	
	return HttpResponse(json.dumps(context), content_type='application/json')	
