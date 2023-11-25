from django.db import models
class Department(models.Model):
    dept_name=models.CharField(max_length=50)
    dept_decs=models.TextField(max_length=500)
    def __str__(self):
        return self.dept_name
class Doctore(models.Model):
    doc_name=models.CharField(max_length=50)
    doc_dep=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to="images")
    def __str__(self):
        return self.doc_name
class Booking(models.Model):
    p_name=models.CharField(max_length=50)
    p_phone=models.CharField(max_length=12)
    doc_name=models.ForeignKey(Doctore,on_delete=models.CASCADE)
    booking_on=models.DateField(auto_now_add=True) 
    booked_to=models.DateTimeField()
    def __str__(self):
        return self.p_name

# Create your models here.
