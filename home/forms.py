from django import forms
from .models import Profile, BlogPost

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_no', 'bio', 'facebook', 'instagram', 'linkedin', 'image', )
     
        
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titre du Post'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom du titre'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Contenu du Post'}),
        }