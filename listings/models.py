from django.db import models
from django.forms import ModelForm

from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.
class Listing(models.Model):
    # Choices
    Car_Models = [
        ('Alfa Romeo','Alfa Romeo'),('Audi','Audi'),('BMW','BMW'),('Chevrolet','Chevrolet'),
        ('Chrysler','Chrysler'),('Citroen','Citroen'),('Dodge','Dodge'),('Fiat','Fiat'),
        ('Ford','Ford'),('Honda','Honda'),('Hyundai','Hyundai'),('Isuzu','Isuzu'),
        ('Jaguar','Jaguar'),('Jeep','Jeep'),('Kia','Kia'),('Land Rover','Land Rover'),
        ('Lexus','Lexus'),('Mazda','Mazda'),('Mercedes Benz','Mercedes Benz'),('Mini','Mini'),
        ('Mitsubishi','Mitsubishi'),('Nissan','Nissan'),('Opel','Opel'),('Peugeot','Peugeot'),
        ('Subaru','Subaru'),('Suzuki','Suzuki'),('Toyota','Toyota'),('Volkswagen','Volkswagen'),
        ('Volvo','Volvo'),('Other','Other')
    ]
    Transmission = [
        ('Automatic','Automatic'),('Manual','Manual'),
    ]

    Fuel_Type = [
        ('Petrol','Petrol'),('Diesel','Diesel'),
    ]
    Dealership = [
        ('Gaborone','Gaborone'),('Palapye','Palapye'),('Francistown','Francistown')
    ]
    Body_Type = [
        ('Compact','Compact'),('Hatchback','Hatchback'),('Sedan','Sedan'),('SUV','SUV'),
        ('Van','Van'),('PickUp','PickUp'),('Sport','Sport')
    ]
    Seats = [
        ('2','2'),('3','3'),('4','4'),('5','5'),
        ('6','6'),('7','7'),('8','>7')
    ]
    Doors = [
        ('2','2'),('3','3'),('4','4'),('5','5')
    ]
    Year = [
        ('1990','Older than 1990'),('1991','After 1991'),('1992','1992'),('1993','1993'),
        ('1994','1994'),('1995','1995'),('1996','1996'),('1997','1997'),
        ('1998','1998'),('1999','1999'),('2000','2000'),('2001','2001'),
        ('2002','2002'),('2003','2003'),('2004','2004'),('2005','2005'),
        ('2006','2006'),('2007','2007'),('2008','2008'),('2009','2009'),
        ('2010','2010'),('2011','2011'),('2012','2012'),('2013','2013'),
        ('2014','2014'),('2015','2015'),('2016','2016'),('2017','2017'),
        ('2018','2018'),('2019','2019'),('2020','2020')
    ]
    Available = [
        ('No','No'),('Yes','Yes')
    ]
   

    # Fields
    title = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=2002, default="72 621 902")
    available = models.CharField(max_length=50, choices=Available, default="No")
    brand_model = models.CharField(max_length=50, choices=Car_Models, default="Model (All)")
    transmission = models.CharField(max_length=20 , choices=Transmission, default="Transmission (All)")
    fuel_type = models.CharField(max_length=20, choices=Fuel_Type, default="Fuel Type (All)")
    price = models.PositiveIntegerField(blank=True, null=True)
    mileage  = models.PositiveIntegerField(blank=True, null=True)
    year = models.CharField(max_length=20, choices=Year, default="Year (All)")
    dealership = models.CharField(max_length=20 , choices=Dealership, default="Dealership (All)")
    body_type = models.CharField(max_length=20, choices=Body_Type, default="Body Types (All)")
    seat = models.CharField(max_length=20, choices=Seats, default="Seats (All)")
    engine = models.FloatField(validators=[MinValueValidator(0)], blank=True, null=True)
    photo_main = models.ImageField(upload_to= 'photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/ %m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to= 'photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title #This is used in the admin area as the main field to be displayed


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['brand_model', 'transmission', 'fuel_type','dealership', 'body_type', 'price', 'year', 'mileage']


    