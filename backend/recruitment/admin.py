from django.contrib import admin

from .models import Application, Exam, Offer, OfferStage, University, ExamsGroup

admin.site.register(Application)
admin.site.register(Exam)
admin.site.register(ExamsGroup)
admin.site.register(Offer)
admin.site.register(OfferStage)
admin.site.register(University)
