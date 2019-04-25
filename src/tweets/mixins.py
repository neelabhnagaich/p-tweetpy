
from django.forms.utils import ErrorList
from django import forms

class FormUserNeededMixin(object):

     def form_valid(self, form):
        if self.request.user.is_authenticated() :
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form.errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['User must be logged in'])
            return self.form_invalid(form)

class UserOwnerMixin(object):

    def form_valid(self,form):
        if form.instance.user == self.request.user:
            return super(UserOwnerMixin, self).form_valid(form)
        else:
            form.errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['you cannot modify the content'])
            return self.form_invalid(form)

