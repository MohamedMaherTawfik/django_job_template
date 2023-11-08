from django import forms
from django.core.validators import FileExtensionValidator
from django_summernote.widgets import SummernoteWidget,SummernoteInplaceWidget
from .models import job_apply,job


class jobapplyform(forms.ModelForm):
    cv=forms.FileField(
        label='CV',
        widget=forms.ClearableFileInput(attrs={'accept':'.pdf'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='only pdf files are allowed.')]
    )
    class Meta:
        model=job_apply
        fields=['user_name','email','linked_in_profile','github_profile','cv','cover_letter']
        
        
        
class jobform(forms.ModelForm):
    description = forms.CharField(widget=SummernoteWidget())
    
    class Meta:
        model=job    
        fields=['title','location','company','salary_start','salary_end','description','vacancy','job_type','experince','category']      