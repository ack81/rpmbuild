%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name django-appconf
%define version 1.0.1
%define unmangled_version 1.0.1
%define unmangled_version 1.0.1
%define release 1

Summary: A helper class for handling configuration defaults of packaged apps gracefully.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jannis Leidel <jannis@leidel.info>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://django-appconf.readthedocs.org/
BuildRequires: cb-python
AutoReq: 0

%description
django-appconf
==============

.. image:: https://secure.travis-ci.org/jezdez/django-appconf.png?branch=develop
    :alt: Build Status
    :target: http://travis-ci.org/jezdez/django-appconf

A helper class for handling configuration defaults of packaged Django
apps gracefully.

.. note::

    This app precedes Django's own AppConfig_ classes that act as
    "objects [to] store metadata for an application" inside Django's
    app loading mechanism. In other words, they solve a related but
    different use case than django-appconf and can't easily be used
    as a replacement. The similarity in name is purely coincidental.

.. _AppConfig: https://docs.djangoproject.com/en/stable/ref/applications/#django.apps.AppConfig

Overview
--------

Say you have an app called ``myapp`` with a few defaults, which you want
to refer to in the app's code without repeating yourself all the time.
``appconf`` provides a simple class to implement those defaults. Simply add
something like the following code somewhere in your app files::

    from appconf import AppConf

    class MyAppConf(AppConf):
        SETTING_1 = "one"
        SETTING_2 = (
            "two",
        )

.. note::

    ``AppConf`` classes depend on being imported during startup of the Django
    process. Even though there are multiple modules loaded automatically,
    only the ``models`` modules (usually the ``models.py`` file of your
    app) are guaranteed to be loaded at startup. Therefore it's recommended
    to put your ``AppConf`` subclass(es) there, too.

The settings are initialized with the capitalized app label of where the
setting is located at. E.g. if your ``models.py`` with the ``AppConf`` class
is in the ``myapp`` package, the prefix of the settings will be ``MYAPP``.

You can override the default prefix by specifying a ``prefix`` attribute of
an inner ``Meta`` class::

    from appconf import AppConf

    class AcmeAppConf(AppConf):
        SETTING_1 = "one"
        SETTING_2 = (
            "two",
        )

        class Meta:
            prefix = 'acme'

The ``MyAppConf`` class will automatically look at Django's global settings
to determine if you've overridden it. For example, adding this to your site's
``settings.py`` would override ``SETTING_1`` of the above ``MyAppConf``::

    ACME_SETTING_1 = "uno"

In case you want to use a different settings object instead of the default
``'django.conf.settings'``, set the ``holder`` attribute of the inner
``Meta`` class to a dotted import path::

    from appconf import AppConf

    class MyAppConf(AppConf):
        SETTING_1 = "one"
        SETTING_2 = (
            "two",
        )

        class Meta:
            prefix = 'acme'
            holder = 'acme.conf.settings'

If you ship an ``AppConf`` class with your reusable Django app, it's
recommended to put it in a ``conf.py`` file of your app package and
import ``django.conf.settings`` in it, too::

    from django.conf import settings
    from appconf import AppConf

    class MyAppConf(AppConf):
        SETTING_1 = "one"
        SETTING_2 = (
            "two",
        )

In the other files of your app you can easily make sure the settings
are correctly loaded if you import Django's settings object from that
module, e.g. in your app's ``views.py``::

    from django.http import HttpResponse
    from myapp.conf import settings

    def index(request):
        text = 'Setting 1 is: %s' % settings.MYAPP_SETTING_1
        return HttpResponse(text)



%prep
%setup -n %{__name}-%{unmangled_version} -n %{__name}-%{unmangled_version}

%build
/opt/cb/bin/python setup.py build

%install
/opt/cb/bin/python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
