from django.db import models

class Provider(models.Model):
    # create the choices for the dept
    PEDIATRICS = 'PEDIATRICS'
    SURGERY = 'SURGERY'
    PRIMARYCARE = 'PRIMARY CARE'
    DEPT_CHOICES = [
        (PEDIATRICS,'PEDIATRICS'),
        (SURGERY,'SURGERY'),
        (PRIMARYCARE,'PRIMARY CARE'),
    ]

    epic_id = models.IntegerField(primary_key=True, default=0) # NumberInput is the default form input type
    prov_fname = models.CharField(max_length=50)
    prov_midinital = models.CharField(max_length=1)
    prov_lname = models.CharField(max_length=100)
    prov_division = models.CharField(max_length=200)
    prov_department = models.CharField(max_length=200, choices=DEPT_CHOICES, default=PEDIATRICS)
    prov_email = models.EmailField()
    prov_hospital = models.CharField(max_length=200)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  
    # this is the primary key that building choice is looking at
    def __str__(self):
        full_name = str(self.epic_id) + ' - ' + self.prov_lname
        #full_name = self.prov_lname + ', ' + self.prov_fname + ' ' + self.prov_midinital
        return  full_name

class Building(models.Model):
    MAIN_CAMPUS = 'MAIN CAMPUS'
    SATELLITE_1 = 'SATELLITE 1'
    SATELLITE_2 = 'SATELLITE 2'
    SATELLITE_3 = 'SATELLITE 3'
    BUILDING_CHOICES = [
        (MAIN_CAMPUS,'MAIN CAMPUS'),
        (SATELLITE_1,'SATELLITE 1'),
        (SATELLITE_2,'SATELLITE 2'),
        (SATELLITE_3,'SATELLITE 3'),
    ]

    FLOOR_1 = 'FLOOR 1'
    FLOOR_2 = 'FLOOR 2'
    FLOOR_3 = 'FLOOR 3'
    FLOOR_CHOICES = [
        (FLOOR_1, 'FLOOR 1'),
        (FLOOR_2, 'FLOOR 2'),
        (FLOOR_3, 'FLOOR 3'),
    ]
    
    ROOM_1 = 'ROOM 1'
    ROOM_2 = 'ROOM 2'
    ROOM_3 = 'ROOM 3'
    ROOM_CHOICES = [
        (ROOM_1, 'ROOM 1'),
        (ROOM_2, 'ROOM 2'),
        (ROOM_3, 'ROOM 3'),
    ]
    building = models.CharField(max_length=50, choices=BUILDING_CHOICES, default=MAIN_CAMPUS)
    floor = models.CharField(max_length=50, choices=FLOOR_CHOICES, default=FLOOR_1)
    room = models.CharField(max_length=50, choices=ROOM_CHOICES, default=ROOM_1)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # return the building choice instead of the 
    def __str__(self):
        return self.building + '-' + self.floor + '-' + self.room

class Schedule(models.Model):
    datetime = models.DateTimeField()
    duration = models.DurationField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    location = models.ForeignKey(Building, on_delete=models.CASCADE)