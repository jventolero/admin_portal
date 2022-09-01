from django.db import models

# Create your models here.
class BusinessPermit(models.Model):
    personel_assignment = models.CharField("Personel Assignment", max_length=245, default="Melvin Daza")
    location = models.CharField("Location", max_length=245, default="Muntinlupa City")
    stores = models.CharField("Stores", max_length=245, default="ATC 1")
    company = models.CharField("Company", max_length=245, default="APTGSI")
    business_permit_start = models.DateField("Business Permit Start", auto_now=True)
    business_permit_end = models.DateField("Business Permit End", auto_now=True)
    business_permit_renew = models.DateField("Business Permit Renew", auto_now=True)
    brgy_permit_start = models.DateField("Brgy Permit Start", auto_now=True)
    brgy_permit_end = models.DateField("Brgy Permit End", auto_now=True)
    bgry_permit_renew = models.DateField("Brgy Permit Renew", auto_now=True)
    insurance_start = models.DateField("Insurance Start", auto_now=True)
    insurance_end = models.DateField("Insurance End", auto_now=True)
    #conformance = models.CharField()
    #tourism_cert = models.CharField()
    enviromental_clearance_start = models.DateField("Enviromental Clearance Start", auto_now=True)
    enviromental_clearance_end = models.DateField("Enviromental Clearance End", auto_now=True)
    zoning = models.CharField("Zoning", max_length=245, default="N/A")
    cert_of_final_electrical_inspection_start = models.DateField("Certification of Final Electrical Inspection Start", auto_now=True)
    cert_of_final_electrical_inspection_end = models.DateField("Certification of Final Electrical Inspection End", auto_now=True)
    signage_permit_start = models.DateField("Signage Permit Start", auto_now=True)
    signage_permit_end = models.DateField("Signage Permit End", auto_now=True)
    cedula_start = models.DateField("Cedula Start", auto_now=True)
    cedula_end = models.DateField("Cedula End", auto_now=True)
    fsic_start = models.DateField("FSIC Start", auto_now=True)
    fsic_end = models.DateField("FSIC End", auto_now=True)
    sanitary_start = models.DateField("Sanitary Permit Start", auto_now=True)
    sanitary_end = models.DateField("Sanitary Permit End", auto_now=True)
    bir_0605_start = models.DateField("BIR 605 Start", auto_now=True)
    bir_0605_end = models.DateField("BIR 605 End", auto_now=True)

    

