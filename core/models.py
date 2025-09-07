from django.db import models

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20) # e.g., 'admin', 'donor', 'hospital'

class Donors(models.Model):
    donor_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Users, on_delete=models.CASCADE) # One-to-one relationship
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    contact_no = models.CharField(max_length=15)
    address = models.TextField()
    last_donation_date = models.DateField(null=True, blank=True)
    health_status = models.TextField()

class BloodStock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    blood_group = models.CharField(max_length=5, unique=True)
    units_available = models.IntegerField(default=0)
    expiry_date = models.DateField()

class DonationHistory(models.Model):
    donation_id = models.AutoField(primary_key=True)
    donor = models.ForeignKey(Donors, on_delete=models.CASCADE) # Foreign key to Donors
    date = models.DateField()
    location = models.CharField(max_length=100)
    units_donated = models.IntegerField()

class BloodRequests(models.Model):
    request_id = models.AutoField(primary_key=True)
    requester_name = models.CharField(max_length=100)
    requester_type = models.CharField(max_length=20) # 'hospital' or 'individual'
    blood_group = models.CharField(max_length=5)
    units_needed = models.IntegerField()
    status = models.CharField(max_length=20) # 'pending', 'approved', 'fulfilled'