from django.db import models
from accounts.models import companyUser, studentUser
# Create your models here.


class placementInfo(models.Model):
    company_username = models.ForeignKey(
        companyUser, default=None, on_delete=models.CASCADE)
    company_name = models.CharField(default='', max_length=255)
    package = models.CharField(default='', max_length=255)
    domain = models.CharField(max_length=255, default='')
    cgpa_req = models.FloatField(default=0)
    backlog = models.IntegerField(default=0)
    comimg = models.ImageField(upload_to='Images/')
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=13)
    company_website = models.URLField(default='')
    regform_link = models.URLField(
        default='https://forms.gle/VNgHt2XeRaDn65Wv6')
    status = models.BooleanField(default=False)

    @staticmethod
    def placement_by_id(ids):
        if ids:
            return placementInfo.objects.filter(company_username=ids)
        else:
            return placementInfo.objects.all()

    def __str__(self):
        return str(self.id)


class internshipInfo(models.Model):
    company_username = models.ForeignKey(
        companyUser, default=None, on_delete=models.CASCADE)
    company_name = models.CharField(default='', max_length=255)
    stipend = models.CharField(default='', max_length=255)
    domain = models.CharField(max_length=255, default='')
    cgpa_req = models.FloatField(default=0)
    workduration = models.IntegerField(default=0)
    modeofwork = models.CharField(default='', max_length=255)
    comimg = models.ImageField(upload_to='Images/')
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=13)
    company_website = models.URLField(default='')
    regform_link = models.URLField(
        default='https://forms.gle/VNgHt2XeRaDn65Wv6')
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @staticmethod
    def internship_by_id(ids):
        if ids:
            return internshipInfo.objects.filter(company_username=ids)
        else:
            return internshipInfo.objects.all()


class Student_placement(models.Model):
    student_username = models.ForeignKey(
        studentUser, default=None, on_delete=models.CASCADE)
    placement_id = models.ForeignKey(
        placementInfo, default=None, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)

    @staticmethod
    def placement_by_id(ids):
        if ids:
            return Student_placement.objects.filter(placement_id=ids)
        else:
            return Student_placement.objects.all()


class Student_internship(models.Model):
    student_username = models.ForeignKey(
        studentUser, default=None, on_delete=models.CASCADE)
    internship_id = models.ForeignKey(
        internshipInfo, default=None, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)

    @staticmethod
    def internship_by_id(ids):
        if ids:
            return Student_internship.objects.filter(internship_id=ids)
        else:
            return Student_internship.objects.all()
