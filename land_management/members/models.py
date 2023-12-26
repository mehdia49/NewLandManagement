from django.db import models
from .enums import TransactionType,TenureType,InfrastructureType
# Create your models here.

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.admin_id}"


class LandOwner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=255)
    phone_number = models.PositiveIntegerField()
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.owner_id}'

    
class LandPlot(models.Model):
    plot_id = models.AutoField(primary_key=True)
    location = models.TextField() 
    area = models.IntegerField()
    ownerid = models.ForeignKey(LandOwner, on_delete=models.CASCADE, default=" ")

    def __str__(self):
        return f"Plot {self.plot_id}, Owner ID: {self.ownerid.owner_id}"


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10, default=" ")
    password = models.CharField(max_length=50, default=" ")
    location = models.TextField(default=" ")
    admin = models.OneToOneField(Admin, on_delete=models.CASCADE, null=True)
    owner = models.OneToOneField(LandOwner, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.username}, {self.user_id}'
    

    
class LandTransaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(max_length=20,choices=[(transactionType.name, transactionType.value) for transactionType in TransactionType])
    plot = models.ForeignKey(LandPlot, on_delete=models.CASCADE)
    transaction_date = models.DateField()

    def __str__(self):
        return f'Transaction ID: {self.transaction_id}, Plot ID: {self.plot.plot_id}, transaction_type: {self.transaction_type}'
    

class LandTenure(models.Model):
    tenure_id = models.AutoField(primary_key=True)
    plot = models.ForeignKey(LandPlot, on_delete=models.CASCADE)
    tenure_type = models.CharField(max_length=20,choices=[(tenureType.name, tenureType.value) for tenureType in TenureType]
    )
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'Tenure ID: {self.tenure_id}, Plot ID: {self.plot.plot_id}'

class LandValuation(models.Model):
    valuation_id = models.AutoField(primary_key=True)
    plot = models.ForeignKey(LandPlot, on_delete=models.CASCADE)
    valuation_amount = models.DecimalField(max_digits=10, decimal_places=2)
    valuation_date = models.DateField()
    market_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Valuation ID: {self.valuation_id}, Plot ID: {self.plot.plot_id}'
    

class Infrastructure(models.Model):
    infrastructure_id = models.AutoField(primary_key=True)
    plot = models.ForeignKey(LandPlot, on_delete=models.CASCADE)
    infrastructure_type = models.CharField(max_length=20,choices=[(infraType.name, infraType.value) for infraType in InfrastructureType]
    )
    infrastructure_name = models.CharField(max_length=100)

    def __str__(self):
        return f'Infrastructure ID: {self.infrastructure_id}, Plot ID: {self.plot.plot_id}'
    
    
class AdmissionForm(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    city = models.CharField(max_length=10, choices=[("Lahore", "Lahore"), ("Sahiwal", "Sahiwal"), ("Okara", "Okara")])
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"