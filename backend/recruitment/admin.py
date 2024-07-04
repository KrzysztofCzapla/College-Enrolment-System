from django.contrib import admin

from .models import Application, Exam, Offer, OfferStage, University

admin.site.register(Application)
admin.site.register(Exam)
admin.site.register(Offer)
admin.site.register(OfferStage)
admin.site.register(University)
