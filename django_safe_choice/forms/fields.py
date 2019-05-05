import logging
from django.forms.fields import ChoiceField, TypedChoiceField
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)


"""
This did not work out, simply because the existing value is not known to the Field methods. They
are run at the time where the forms are defined, i.e. when Django is starting up. Only the widgets
are run at "runtime".
"""
class SafeCallableChoiceIterator:
    def __init__(self, choices_func, mask_error, default):
        self.choices_func = choices_func
        self.mask_error = mask_error
        self.default = default

    def __iter__(self):
        # This is where the function is actually executed
        try:
            yield from self.choices_func()
        except Exception:
            if not self.mask_error:
                raise
            logger.exception('Failed to obtain choices')
            yield from [(self.default, _('Unchanged (options failed to load)'))]


class SafeChoiceField(ChoiceField):
    def __init__(self, *, choices=(), mask_error=False, **kwargs):
        # Set our property first, since _set_choices is triggered by super().__init__
        self.__choices = None
        self.mask_error = mask_error
        super().__init__(**kwargs)
        self.choices = choices

    def _get_choices(self):
        return self.__choices

    def _set_choices(self, value):
        # Adapted from Django core. Cannot override due to Django's way of implementing this
        # Setting choices also sets the choices on the widget.
        # chocies can be any iterable, but we call list() on it because
        # it will be consumed more than once.
        if callable(value):
            value = SafeCallableChoiceIterator(value, self.mask_error, self.initial)
        else:
            value = list(value)

        self.__choices = self.widget.choices = value

    choices = property(_get_choices, _set_choices)


class SafeTypedChoiceField(TypedChoiceField):
    def __init__(self, *, choices=(), mask_error=False, **kwargs):
        # ChoiceField does not define this in its __init__ for some reason, avoid trouble on copy
        self._choices = None
        # Set our property first, since _set_choices is triggered by super().__init__
        self.__choices = None
        self.mask_error = mask_error
        super().__init__(**kwargs)
        self.choices = choices

    def _get_choices(self):
        return self.__choices

    def _set_choices(self, value):
        # Adapted from Django core. Cannot override due to Django's way of implementing this
        # Setting choices also sets the choices on the widget.
        # chocies can be any iterable, but we call list() on it because
        # it will be consumed more than once.
        if callable(value):
            value = SafeCallableChoiceIterator(value, self.mask_error, self.initial)
        else:
            value = list(value)

        self.__choices = self.widget.choices = value

    choices = property(_get_choices, _set_choices)
