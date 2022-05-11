from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class BusinessStream(models.Model):
    # business_stream_id = models.AutoField(db_column= id)
    business_stream_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'business_stream'


class Company(models.Model):
    company_name = models.CharField(max_length=50)
    company_description = models.CharField(max_length=500, blank=True, null=True)
    company_website_url = models.CharField(max_length=50, blank=True, null=True)
    establishment_date = models.DateTimeField(blank=True, null=True)
    business_stream = models.ForeignKey(BusinessStream, models.DO_NOTHING, blank=True, null=True)
    password = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'company'


class EducationalDetail(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    degree_certificate_name = models.CharField(max_length=45)
    major = models.CharField(max_length=30)
    percentage = models.FloatField(blank=True, null=True)
    cgpa = models.FloatField(db_column='CGPA', blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateTimeField(blank=True, null=True)
    completion_detail = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'educational_detail'


class ExperienceDetail(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    job_title = models.CharField(max_length=30)
    company_name = models.CharField(max_length=50)
    job_location_city = models.CharField(max_length=20, blank=True, null=True)
    job_location_state = models.CharField(max_length=20, blank=True, null=True)
    job_location_country = models.CharField(max_length=20, blank=True, null=True)
    is_current_job = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experience_detail'


class JobApplications(models.Model):
    job_post = models.ForeignKey('JobPost', models.DO_NOTHING)
    job_seeker = models.ForeignKey('JobSeeker', models.DO_NOTHING)
    apply_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_applications'


class JobLocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street_address = models.CharField(max_length=30)
    zip_code = models.IntegerField()

    class Meta:
        db_table = 'job_location'


class JobPost(models.Model):
    created_date = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    job_description = models.CharField(max_length=100, blank=True, null=True)
    job_location = models.ForeignKey('JobLocation', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('Company', models.DO_NOTHING, blank=True, null=True)
    job_type = models.ForeignKey('JobType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'job_post'


class JobSeeker(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING,null=True)
    f_name = models.CharField(max_length=20,blank=True, null=True)
    l_name = models.CharField(max_length=20,blank=True, null=True)
    current_salary = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=15, blank=True, null=True)
    is_annual_monthly = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'job_seeker'

class JobType(models.Model):
    job_type = models.CharField(max_length=20,unique=True)

    class Meta:
        db_table = 'job_type'


class SeekerSkillSet(models.Model):
    skill = models.ForeignKey('SkillSet', models.DO_NOTHING)
    seeker = models.ForeignKey('User', models.DO_NOTHING)
    skill_level = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seeker_skill_set'


class SkillSet(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skill_set'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_type = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=10,null=True)
    dob = models.DateTimeField(blank=True, null=True) 
    is_active = models.IntegerField(blank=True, null=True)
    phone_no = models.CharField(max_length=24,unique=True,null=True)

    class Meta:
        db_table = 'user'


class UserLog(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    last_login_date = models.DateTimeField(blank=True, null=True)
    last_job_apply_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_log'
