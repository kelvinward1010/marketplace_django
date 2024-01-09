from django import forms
from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(attrs={
                'placeholder': "Type your message",
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }