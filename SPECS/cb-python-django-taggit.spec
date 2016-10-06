%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name django-taggit
%define version 0.17.1
%define unmangled_version 0.17.1
%define unmangled_version 0.17.1
%define release 1

Summary: django-taggit is a reusable Django application for simple tagging.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Alex Gaynor <alex.gaynor@gmail.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://github.com/alex/django-taggit/tree/master
BuildRequires: cb-python
AutoReq: 0

%description
django-taggit
=============

``django-taggit`` a simpler approach to tagging with Django.  Add ``"taggit"`` to your
``INSTALLED_APPS`` then just add a TaggableManager to your model and go:

.. code:: python

    from django.db import models

    from taggit.managers import TaggableManager

    class Food(models.Model):
        # ... fields here

        tags = TaggableManager()


Then you can use the API like so:

.. code:: python

    >>> apple = Food.objects.create(name="apple")
    >>> apple.tags.add("red", "green", "delicious")
    >>> apple.tags.all()
    [<Tag: red>, <Tag: green>, <Tag: delicious>]
    >>> apple.tags.remove("green")
    >>> apple.tags.all()
    [<Tag: red>, <Tag: delicious>]
    >>> Food.objects.filter(tags__name__in=["red"])
    [<Food: apple>, <Food: cherry>]

Tags will show up for you automatically in forms and the admin.

``django-taggit`` requires Django 1.4.5 or greater.

For more info check out the `documentation <https://django-taggit.readthedocs.org/en/latest/>`_.  And for questions about usage or
development you can contact the
`mailinglist <http://groups.google.com/group/django-taggit>`_.


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
