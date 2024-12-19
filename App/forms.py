from django import forms
from .models import VisitorFeedback

class VisitorFeedbackForm(forms.ModelForm):
    class Meta:
        model = VisitorFeedback
        fields = ['name', 'email', 'visit_date', 'overall_experience', 
                 'cleanliness_rating', 'staff_rating', 'facilities_rating', 'comments']
        widgets = {
            'visit_date': forms.DateInput(attrs={'type': 'date'}),
            'comments': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Please share your experience...'}),
        } 