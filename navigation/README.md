# navigation - glue all modules together
Manage your navigation structure without editing your templates. You just
call the template tag with the name of the navigation you want to have
displayed.

You can have as many separate navigations as you want and order the items
how it fits best.

##### Installation
You do not have to add any configuration options. Just include `navigation`
in `INSTALLED_APPS`.

If you want default entries for your installed applications 
run `python manage.py loaddata navigation`.

###### Configuration
If applications should automatically create navigation items if a model
changes, hook up the signals and add two boolean fields called `published`
and `hidden` to your models.

If `published` is true and `hidden` is false a navigation item will be
created / edited / destroyed whenever you model changes.

###### Example
Import signals from Django and navigation.

    from django.db.models.signals import post_save, pre_delete
    from navigation.signals import update_navigation, delete_navigation

If you want updates for a model called `Page` you just add both signals

    post_save.connect(update_navigation, sender=Page)
    pre_delete.connect(delete_navigation, sender=Page)

Now every time an event happens your `NavItem` will either be updated
or destroyed.

## ToDo

- Signals should first check if `navigation` is in `INSTALLED_APPS`?
- Better submenu handling?
