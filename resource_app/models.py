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

    def __str__(self):
        full_name = self.prov_lname + ', ' + self.prov_fname + ' ' + self.prov_midinital
        return  full_name

class BuildingChoice(models.Model):
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
    provider = models.ForeignKey(Provider, on_delete = models.CASCADE)
    building_choice = models.CharField(max_length=200, choices=BUILDING_CHOICES, default=MAIN_CAMPUS)
    votes = models.IntegerField(default=0)