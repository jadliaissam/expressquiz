from django import template
from django.shortcuts import resolve_url

register = template.Library()


@register.filter
def none(value):
    if value or value == 0:
        return value
    else:
        return "N/A"


@register.filter
def logo(image):
    if image:
        if image.file_storagebackend.code == "local":
            return resolve_url('view_image', image.file_id)
        else:
            return "http://docs.google.com/uc?export=open&id={}".format(image.file_id)
    else:
        return "https://via.placeholder.com/150"


@register.filter
def price(value):
    if value or value == 0:
        return '{} DH'.format(value)
    else:
        return "N/A"


@register.filter
def view_url(doc):
    if doc.file.file_storagebackend.code == "local":
        return resolve_url("view_document", doc.pk)
    if doc.file.file_storagebackend.code == "gdrive":
        return "http://docs.google.com/uc?export=open&id={}".format(doc.file.file_id)


@register.filter
def download_url(doc):
    if doc.file.file_storagebackend.code == "local":
        return resolve_url("download_document", doc.pk)
    if doc.file.file_storagebackend.code == "gdrive":
        return "http://docs.google.com/uc?export=download&id={}".format(doc.file.file_id)


@register.filter
def form_alert(errors):
    if errors:
        return "background-color: antiquewhite"
    else:
        return "background-color: white"


@register.filter
def get_settings(settings, code):
    return settings.filter(code=code)


@register.filter
def collapse(url, keyword):
    return "collapsed" if keyword in url else ""