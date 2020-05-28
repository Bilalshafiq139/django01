from django.db import models

class edit(models.Model):
    DISTRICT_CHOICES= (
        ('Lahore', 'Lahore'),
        ('Islamabad', 'Islamabad'),
        ('Sahiwal', 'Sahiwal'),
    )
    PROGRAM_CHOICES=(
        ('BBIT','BBIT'),
        ('MBIT', 'MBIT'),
    )
    STATUS_CHOICES=(
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    COUNTRY_CHOICES= (
        ('Pakistan', 'Pakistan'),
        ('Turkey', 'Turkey'),
        ('Thailand', 'Thailand'),
        ('Others', 'Others'),
    )
    RELIGION_CHOICES = (
        ('Islam', 'Islam'),
        ('Christanity', 'Christanity'),
        ('Other', 'Other'),
    )
    MARTIAL_STATUS=(
        ('Married', 'Married'),
        ('Single', 'Single'),
        ('Divorced', 'Divorced'),
    )
    GENDER_CHOICES=(
        ('Male', 'Male'),
        ('Fe-Male', 'Fe-Male'),
        ('Other', 'Other'),
    )

    Form_no = models.CharField(max_length=20)
    Status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    Applicant_name = models.CharField(max_length=200)
    Father_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    CNIC = models.CharField(max_length=20)
    Address = models.CharField(max_length=200)
    Hafiz_e_Quran = models.BooleanField()
    District = models.CharField(max_length=100, choices=DISTRICT_CHOICES)
    Religion = models.CharField(max_length=50, choices=RELIGION_CHOICES)
    Country = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    Program = models.CharField(max_length=50, choices=PROGRAM_CHOICES)
    DOB=models.DateField()
    Gender= models.CharField(max_length=40, choices=GENDER_CHOICES)
    Martial_Status= models.CharField(max_length=50, choices=MARTIAL_STATUS)



