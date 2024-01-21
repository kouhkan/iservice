from django.contrib import admin

from herfeei.experts.models import Expert, Bookmark, Sample, AvailableTimeExpert, Warranty

admin.site.register(Expert)
admin.site.register(Bookmark)
admin.site.register(Sample)
admin.site.register(AvailableTimeExpert)
admin.site.register(Warranty)
