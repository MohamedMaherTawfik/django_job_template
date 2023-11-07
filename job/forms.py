from django import forms
from django.core.validators import FileExtensionValidator
from .models import job_apply


class jobapplyform(forms.ModelForm):
    cv=forms.FileField(
        label='CV',
        widget=forms.ClearableFileInput(attrs={'accept':'.pdf'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf'],message='only pdf files are allowed.')]
    )
    class Meta:
        model=job_apply
        fields=['user_name','email','linked_in_profile','github_profile','cv','cover_letter']