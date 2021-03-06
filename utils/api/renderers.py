from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.renderers import JSONRenderer
import re


def underscoreToCamel(match):
    return match.group()[0] + match.group()[2].upper()


def camelize(data):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            new_key = re.sub(r"[a-z]_[a-z]", underscoreToCamel, key)
            new_dict[new_key] = camelize(value)
        return new_dict
    if isinstance(data, (list, tuple)):
        for i in range(len(data)):
            data[i] = camelize(data[i])
        return data
    return data


class CamelCaseJSONRenderer(JSONRenderer):
    """
    https://gist.github.com/vbabiy/5842073
    """
    def render(self, data, *args, **kwargs):
        return super(CamelCaseJSONRenderer, self).render(camelize(data), *args, **kwargs)

class CamelCaseBrowsableAPIRenderer(BrowsableAPIRenderer):
    def render(self, data, *args, **kwargs):
        return super(CamelCaseBrowsableAPIRenderer, self).render(
            camelize(
                data, 
                **{"no_underscore_before_number": False, "ignore_fields": None}
            ), 
            *args, 
            **kwargs
        )