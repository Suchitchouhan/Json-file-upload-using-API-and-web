from django.db import models

# Create your models here.
class account(models.Model):
	Ido=models.CharField(default="",max_length=300)
	user_idO=models.CharField(default="",max_length=300)
	amount=models.IntegerField(default=0)
	coins_balance=models.IntegerField(default=0)
	txn_type=models.CharField(default="",max_length=300)
	txn_info=models.CharField(default="",max_length=300)
	action=models.CharField(default="",max_length=300)
	time=models.CharField(default="",max_length=300)
	def __str__(self):
		return self.Ido
	def as_dict(self):
		return {"id":self.Ido,"user_id":self.user_idO,'amount':self.amount,"coins_balance":self.coins_balance,'txn_type':self.txn_type,'txn_info':self.txn_info,'action':self.action,'time':self.time}	
