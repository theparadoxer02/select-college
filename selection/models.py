from django.db import models
# from multiselectfield import MultiSelectField
# Create your models here.


class Courses(models.Model):
    # college_choices = (
    #     ('B.tech', 'B.tech'),
    #     ('diploma', 'Diploma'),
    #     ('mba', 'MBA'),
    #     ('pgdm', 'PGDM'),
    # )
    courses_offered = models.CharField(max_length=40, default='', unique=True)

    def __str__(self):
        return str(self.courses_offered)


class City(models.Model):
    city = models.CharField(max_length=200, default='', unique=True)

    def __str__(self):
        return self.city


class Location(models.Model):
    address = models.CharField(max_length=200, default='')
    city = models.ForeignKey(City, null=True)

    def __str__(self):
        return self.address


class College(models.Model):

    city_selection = (
        ('Delhi', 'Delhi'),
        ('Noida', 'Noida'),
        ('Bangalore', 'Bangalore'),
        ('Gurgaon', 'Gurgaon')
    )

    level_choices = (
        ('graduation', 'graduation'),
        ('post-graduation', 'post-graduation')
    )
    name = models.CharField(max_length=100, default='', unique=True)
    city = models.ForeignKey(City, null=True)
    address = models.ForeignKey(Location, on_delete=models.CASCADE)
    courses_offered = models.ForeignKey(Courses, on_delete=models.CASCADE)
    level = models.CharField(
        choices=level_choices, default='graduation', max_length=20
    )

    class Meta:
        verbose_name = "College"
        verbose_name_plural = "Colleges"

    def __str__(self):
        return self.name

    def get_city(self):
        return self.location.city()


class CollegeInfo(models.Model):
    courses = models.ForeignKey(Courses)
    college = models.ForeignKey(College)
    fee = models.CharField(max_length=10)
    average_salary = models.CharField(max_length=100)

    def __str__(self):
        return self.college.name
