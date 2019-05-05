from django.forms import widgets
from django.utils.translation import gettext as _


class SafeChoiceWidgetMixin(widgets.ChoiceWidget):
    def __init__(self, *args, fallback_label=None, **kwargs):
        super().__init__(*args, **kwargs)
        # Label to use for options added to make up for the selected value not being a choice.
        # It can use format variable 'value' to display the raw value.
        # When it is possible to select multiple options, 'index' can be used to indicate the option
        # number.
        self.fallback_label = fallback_label

    def optgroups(self, name, value, attrs=None):
        # Let the base ChoiceWidget do its job
        groups = super().optgroups(name, value, attrs)

        # What options are selected?
        selected_values = set()
        # Keep track of the last used index
        index = 0

        for _1, subgroup, index in groups:
            for option in subgroup:
                if option['selected']:
                    selected_values.add(option['value'])
        # The last used index is our offset for later
        offset = index

        # What values, if any, did not show up as selected options?
        all_values = set(value)
        forgotten_values = all_values - selected_values

        # Short-circuit if all is good (i.e. all values are selected options)
        if not forgotten_values:
            return groups

        # There are some values not available as selected options. Add them.
        for forgotten_index, subvalue in enumerate(forgotten_values):
            # What label shall we use?
            # Gather format variables first
            if self.allow_multiple_selected:
                label_values = {'index': forgotten_index, 'value': subvalue}
            else:
                label_values = {'value': subvalue}

            # Let the user override the default
            if self.fallback_label:
                sublabel = self.fallback_label % label_values
            # We're using the default
            elif self.allow_multiple_selected:
                sublabel = _('Unchanged option %(index)s (%(value)s)') % label_values
            else:
                sublabel = _('Unchanged (%(value)s)') % label_values

            # Set other variables used by create_option()
            group_name = None
            # The index must be consistent, so we're adding these options to the end.
            index = offset + forgotten_index
            selected = True
            subindex = None

            # Create this additional option, using the existing method
            option = self.create_option(
                name,
                subvalue,
                sublabel,
                selected,
                index,
                subindex=subindex,
                attrs=attrs
            )
            # Create this "group" (the additional options are placed outside of any group)
            groups.append((group_name, [option], index))
        return groups


class SafeSelect(SafeChoiceWidgetMixin, widgets.Select):
    pass


class SafeNullBooleanSelect(SafeChoiceWidgetMixin, widgets.NullBooleanSelect):
    pass


class SafeSelectMultiple(SafeChoiceWidgetMixin, widgets.SelectMultiple):
    pass


class SafeCheckboxSelectMultiple(SafeChoiceWidgetMixin, widgets.CheckboxSelectMultiple):
    pass
