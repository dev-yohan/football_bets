from django import forms

class ObjectListField(forms.CharField):
    def prepare_value(self, value):
        if not value:
            return ''

        newvalue = {}
        for key, val in value.__dict__.items():
            if type(val) is unicode:
                newvalue[key] = val

        return ", ".join(["%s=%s" % (k, v) for k, v in newvalue.items()])

    def to_python(self, value):
        if not value:
            return {}

        obj = {}
        lst = [item.strip() for item in value.split(',')]
        for item in lst:
            val = item.split('=');
            obj[val[0]] = val[1]

        return obj