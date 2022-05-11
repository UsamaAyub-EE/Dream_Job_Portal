# Generated by Django 4.0.4 on 2022-05-10 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_stream_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'business_stream',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EducationalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_certificate_name', models.CharField(max_length=45)),
                ('major', models.CharField(max_length=30)),
                ('percentage', models.FloatField(blank=True, null=True)),
                ('cgpa', models.FloatField(blank=True, db_column='CGPA', null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('completion_detail', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'educational_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExperienceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('job_title', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=50)),
                ('job_location_city', models.CharField(blank=True, max_length=20, null=True)),
                ('job_location_state', models.CharField(blank=True, max_length=20, null=True)),
                ('job_location_country', models.CharField(blank=True, max_length=20, null=True)),
                ('is_current_job', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'experience_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JobApplications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'job_applications',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SeekerSkillSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_level', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'seeker_skill_set',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SkillSet',
            fields=[
                ('skill_id', models.AutoField(primary_key=True, serialize=False)),
                ('skill_name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'skill_set',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login_date', models.DateTimeField(blank=True, null=True)),
                ('last_job_apply_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('company_description', models.CharField(blank=True, max_length=500, null=True)),
                ('company_website_url', models.CharField(blank=True, max_length=50, null=True)),
                ('establishment_date', models.DateTimeField(blank=True, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('business_stream', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='website.businessstream')),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='JobLocation',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('street_address', models.CharField(max_length=30)),
                ('zip_code', models.IntegerField()),
            ],
            options={
                'db_table': 'job_location',
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'job_type',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.IntegerField(blank=True, null=True)),
                ('phone_no', models.CharField(max_length=24, null=True, unique=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(blank=True, max_length=20, null=True)),
                ('l_name', models.CharField(blank=True, max_length=20, null=True)),
                ('current_salary', models.IntegerField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, max_length=15, null=True)),
                ('is_annual_monthly', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='website.user')),
            ],
            options={
                'db_table': 'job_seeker',
            },
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.IntegerField(blank=True, null=True)),
                ('job_description', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='website.company')),
                ('job_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='website.joblocation')),
                ('job_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='website.jobtype')),
            ],
            options={
                'db_table': 'job_post',
            },
        ),
    ]