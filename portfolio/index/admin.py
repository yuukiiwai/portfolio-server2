from django.contrib import admin
from django import forms
from .models import History,Strong,StrongExp,Studystate

# Register your models here.
@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    model = History
    list_display = ["when","event","order"]

admin.site.register(Strong)

class StrongExpForm(forms.ModelForm):
    class Meta:
        model = StrongExp
        fields = ["exp"]

    exp = forms.CharField(
        widget=forms.Textarea( attrs={"maxlength":str(StrongExp.exp.field.max_length),} ) )

@admin.register(StrongExp)
class StrongExpAdmin(admin.ModelAdmin):
    model = StrongExp
    list_display = ["strong","exp"]
    form = StrongExpForm

@admin.register(Studystate)
class StudystateAdmin(admin.ModelAdmin):
    model = Studystate
    list_display = ["state","tech","imgurl"]