from django.contrib import admin

# Register your models here.
from .models import BusinessStream
admin.site.register(BusinessStream)

from .models import Company
admin.site.register(Company)

from .models import EducationalDetail
admin.site.register(EducationalDetail)

from .models import ExperienceDetail
admin.site.register(ExperienceDetail)

from .models import JobApplications
admin.site.register(JobApplications)

from .models import JobLocation
admin.site.register(JobLocation)

from .models import JobPost
admin.site.register(JobPost)

from .models import JobSeeker
admin.site.register(JobSeeker)

from .models import JobType
admin.site.register(JobType)

from .models import SeekerSkillSet
admin.site.register(SeekerSkillSet)

from .models import SkillSet
admin.site.register(SkillSet)

from .models import User
admin.site.register(User)

from .models import UserLog
admin.site.register(UserLog)

