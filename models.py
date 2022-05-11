# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BusinessStream(models.Model):
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

    class Meta:
        managed = False
        db_table = 'company'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
        managed = False
        db_table = 'job_location'


class JobPost(models.Model):
    created_date = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    job_description = models.CharField(max_length=100, blank=True, null=True)
    job_location = models.ForeignKey(JobLocation, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    job_type = models.ForeignKey('JobType', models.DO_NOTHING)
    posted_by_user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'job_post'


class JobSeeker(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    current_salary = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=15, blank=True, null=True)
    is_annual_monthly = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_seeker'


class JobType(models.Model):
    job_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
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
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    is_active = models.IntegerField(blank=True, null=True)
    phone_no = models.models.CharField(max_length=24,unique=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserLog(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    last_login_date = models.DateTimeField(blank=True, null=True)
    last_job_apply_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_log'
