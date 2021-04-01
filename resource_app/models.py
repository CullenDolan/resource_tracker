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
