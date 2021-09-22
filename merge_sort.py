
# # Merge Sort Algorithm

# def merge_sort1(arr):
#     if len(arr) <= 1:
#         return
#     mid = len(arr)//2

#     left = arr[:mid]
#     right = arr[mid:]

#     left = merge_sort1(left)
#     right = merge_sort1(right)

#     return merge_sorted_list(left, right)

# def merge_sorted_list(a, b):
#     sorted_list = []
#     print(a)
#     len_a = len(a)
#     len_b = len(b)
#     i = j = 0
    
#     while i<len_a and j<len_b:
#         if a[i]<=b[j]:
#             sorted_list.append(a[i])
#             i +=1
#         else:
#             sorted_list.append(b[j])
#             j += 1
#     while i<len_a:
#         sorted_list.append(a[i])
#         i = i+1
#     while j<len_b:
#         sorted_list.append(b[j])
#         j += 1
#     return sorted_list

# def insert(list1):
#     for i in range(1)

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

def contact_form_handle(request):
    if request.method == 'GET':
        form = ContactForm()
    # The request method 'POST' indicates
    # that the form was submitted
    if request.method == 'POST':  # 1
    # We are creating a form instanse to save the form data
        form = ContactForm(request.POST)  # 2
        # Validate the form
        if form.is_valid(): 
            # if the submitted data is valid
            # the perform the following operations
            
            name = form.cleaned_data['name'],
            email = form.cleaned_data['email'],
            mobile = form.cleaned_data['mobile'],
            message =  form.cleaned_data['message']
            form.save()
            # After the operation was successful,
            # redirect to some other page
            return redirect('/success/')  

    return render(request, 'contact_form.html', {'form': form})























