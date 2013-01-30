# pages - ordinary text
You enter text and it is displayed on your page. It is that
simple so I will not waste your time explaining what text is
or what your page is.

Oh, you can add relations - for example you can create a page
called "Service" and many subpages like "Hardware Service",
"Software Service", "Massage Service",...

##### Installation
You do not have to add any configuration options. Just include `pages`
in `INSTALLED_APPS`.

###### Dependencies
Pages depends on `navigation`. If you do not want automatically updated
navigations remove

    from django.db.models.signals import post_save, pre_delete
    from navigation.signals import update_navigation, delete_navigation
    post_save.connect(update_navigation, sender=Page)
    pre_delete.connect(delete_navigation, sender=Page)

from `pages/models.py` and you have an independent application.