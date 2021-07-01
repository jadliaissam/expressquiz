custom_html = {
    'icons': {
        "up": {"class": "fas fa-arrow-circle-up", "style": "color : teal; font-size: 1.5rem; margin : 5px",
               "title": "Déplacer en Haut"},
        "down": {"class": "fas fa-arrow-circle-down", "style": "color : red; font-size: 1.5rem; margin : 5px",
                 "title": "Déplacer en Bas"},
        "view": {"class": "fas fa-search-plus", "style": "font-size: 1.5rem; margin : 5px", "title": "Plus de Détails"},
        "edit": {"class": "fas fa-edit", "style": "font-size: 1.5rem; margin : 5px", "title": "Editer"},
        "delete": {"class": "fas fa-trash", "style": "font-size: 1.5rem; margin : 5px;", "title": "Supprimer"},
        "view_doc": {"class": "fas fa-eye", "style": "font-size: 1.5rem; margin : 5px", "title": "Visualiser"},
        "download": {"class": "fas fa-download", "style": "font-size: 1.5rem; margin : 5px", "title": "Télécharger"},
        "phone": {"class": "fas fa-phone", "style": "font-size: 1.5rem; margin : 5px", "title": "Appel Fixe"},
        "gsm": {"class": "fas fa-mobile-alt", "style": "font-size: 1.5rem; margin : 5px", "title": "Appel GSM"},
        "sms": {"class": "fas fa-envelope", "style": "font-size: 1.5rem; margin : 5px", "title": "Envoyer SMS"},
        "whatsapp": {"class": "fab fa-whatsapp", "style": "font-size: 1.5rem; margin : 5px",
                     "title": "Message Whatsapp"},
        "mail": {"class": "fas fa-at", "style": "font-size: 1.5rem; margin : 5px", "title": "Envoyer Email"},
    }
}


def my_context(request):
    context_data = dict()
    context_data['WIDGET_ERROR_CLASS'] = "text-small animated pulse text-danger alert-dismissible fade show"
    context_data['CUSTOM_HTML'] = custom_html
    #    context_data['WIDGET_REQUIRED_CLASS'] = "text-small animated pulse text-danger alert-dismissible fade show"
    return context_data
