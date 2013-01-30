# catntent
Over the last few years I have build many websites. Most of them
shared a common set of features like news systems or blogs, static
pages and a way to contact the company or individual.

catntent provides a foundation for those projects. Sometimes code
is added to an app for a certain project, sometimes it is not
necessary. But even if code is added - I try to make sure a simple
git merge brings your codebase up to the current release without
breaking anything or introducing trouble with updated libraries.

catntent consists of several different apps. There are no
dependencies bettween apps. Some of them are just helpers you can use but do not
have to. Every app sticks to the default Django layout, the code
should be easy to understand and extend for someone with some
experience with the framework. If apps provide functionality for 
other apps are using it is done
using signals, so each app can still work without another one.

## Applications
catntent currently consists of eight applications.

- blog: a tumblelog supporting different types of posts
- message: a pretty simple contact form
- navigation: build custom menus and include them with template tags
- pages: ordinary pages. Just displaying text, you know?
- portfolio: present your latest projects, customers and testimonials
- profiles: show everyone your awesome team

This two applications are not finished yet, but will be included in
the first official release. 

- dashboard: a user friendly replacement for Djangos admin interface
- notify: get notifications if something happens.

The other six applications are feature
complete and are likely not changed before everything is finished.
For more informations and the documentation check the `README.md` in
the app directory.

## Installation
Download or checkout the the master branch of this repository. This
one will always contain the current stable version.

catntent reads the complete configuration from environment variables.
You can find an example configuration in `docs/environment.example`.

If you have no prior experience with Django, do not know what a media and
static root is or how to setup a database I suggest you first read the 
official Django tutorial.

###### requirements
For a detailed list see `requirements.txt`. Basically catntent
runs on a pretty simple Django stack without any obscure 3rd party
requirements.

This installs both, development and deployment libraries. Development
related apps like django-debug-toolbar are disabled in production, so
this should not be a problem.

Default database engine is PostgreSQL.
