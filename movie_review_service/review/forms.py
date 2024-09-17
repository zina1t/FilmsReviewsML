from django import forms

class ReviewForm(forms.Form):
    review = forms.CharField(label='Film Review', max_length=500, widget=forms.Textarea)
