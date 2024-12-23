from django.db import models
from django.utils.timezone import now 
import uuid

#BE VERY CAUTIOUS OF META NAMES, THE SHAREDMODELS OF THESE AREN'T DELETED

class Vendor(models.Model):
    vendorid = models.AutoField(primary_key=True, db_column='VendorID') 
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    equipment_types = models.CharField(max_length=200, help_text="Comma-separated list of equipment types")
    preferred = models.BooleanField(default=False)

    class Meta:
        db_table = 'vendor'

    def str(self):
        return self.name

class Equipment(models.Model):
    equipmentid =  models.AutoField(primary_key=True, db_column='EquipmentID')
    type = models.CharField(db_column='Type', max_length=45)  # Field name made lowercase.
    lease_terms = models.CharField(
        db_column='Lease Terms',
        max_length=45,
        blank=True,
        null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.CharField(
        db_column='Description',
        max_length=120,
        blank=True,
        null=True
    )  # Field name made lowercase.
    departmentleased = models.CharField(
        db_column='DepartmentLeased',
        max_length=45,
        blank=True,
        null=True
    )  # Field name made lowercase.
    owned_lease = models.CharField(
        db_column='Owned/Lease',
        max_length=1
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    purchasedate = models.DateField(db_column='PurchaseDate', blank=True, null=True)  # Field name made lowercase.
    warenty_info = models.CharField(
        db_column='Warenty Info',
        max_length=120,
        blank=True,
        null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lease_start = models.DateField(db_column='LeaseStart', blank=True, null=True)  # New field for lease start date.
    lease_end = models.DateField(db_column='LeaseEnd', blank=True, null=True)  # New field for lease end date.
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True, db_column='VendorID')

    class Meta:
        db_table = 'equipment_two'

class Maintenance(models.Model):
    maintenanceid = models.AutoField(primary_key=True, db_column='MaintenanceID')
    equipmentid = models.ForeignKey(Equipment, models.DO_NOTHING, db_column='EquipmentID')
    type = models.CharField(db_column='Type', max_length=45)
    description = models.CharField(db_column='Description', max_length=120, blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=45)
    resolution = models.CharField(db_column='Resolution', max_length=120, blank=True, null=True)
    created_at = models.DateTimeField(default=now, db_column='CreatedAt')
    closed_at = models.DateTimeField(null=True, blank=True, db_column='ClosedAt')  # New field for closure time

    class Meta:
        db_table = 'maintenance_two'
        unique_together = (('maintenanceid', 'equipmentid'),)

class ProblemType(models.Model):
    name = models.CharField(max_length=45, unique=True)

    def str(self):
        return self.name