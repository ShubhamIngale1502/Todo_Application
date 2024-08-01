from django import forms
from .models import Todo_Task

Status = [('In Progress','In Progress'),('Completed','Completed'),('Cancel','Cancel'),('Pending','Pending')]
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo_Task
        fields = '__all__'
        
        widgets = {
            'task_name': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light',
            }),
            'task_description': forms.Textarea(attrs={
                'class': 'form-control bg-dark text-light',
                }),
            'task_status': forms.Select(choices=Status, attrs={
                'class': 'form-control bg-dark text-light'
            }),
            'task_deadline':forms.DateInput(attrs={
                'class': 'form-control bg-dark text-light'
            }),
            'task_created_date':forms.DateInput(attrs={
                'class': 'form-control bg-dark text-light'
            }),
            'task_completed_date':forms.DateInput(attrs={
                'class': 'form-control bg-dark text-light'
            })
        }
class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo_Task
        fields = ['task_status'] 