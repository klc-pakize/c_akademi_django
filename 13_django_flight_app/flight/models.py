from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Flight(models.Model):
    AİRLİNES = (
        ("THY","TÜRK HAVAYOLLARI"),
        ("PHT","PEGASUS HAVA TAŞIMACILIĞI"),
        ("AJH","ATLAS JET HAVACILIK"),
        ("OİT","ONUR AİR TAŞIMACILIK")
    )

    flight_number = models.CharField(max_length=10, unique=True)
    operation_airlines = models.CharField(max_length=15, choices=AİRLİNES)
    departure_city = models.CharField(max_length=30)
    arrival_city = models.CharField(max_length=30)
    date_of_departure = models.DateField()
    estimated_time_of_departure = models.TimeField()
    
    def __str__(self):
        return f'{self.flight_number} - {self.departure_city} - {self.arrival_city}'
    
class Passenger(models.Model):           # cooper - jason - murat ... 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Reservation(models.Model):  #(cooper - murat)  - (cooper - jason) - () ....
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    passenger = models.ManyToManyField(Passenger, related_name='reservations')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reservation')

    def __str__(self):
        return f'{self.flight}'