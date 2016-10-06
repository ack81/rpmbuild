%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name django-debug-toolbar
%define version 1.3.2
%define unmangled_version 1.3.2
%define unmangled_version 1.3.2
%define release 1

Summary: A configurable set of panels that display various debug information about the current request/response.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Rob Hudson <rob@cogit8.org>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://github.com/django-debug-toolbar/django-debug-toolbar
BuildRequires: cb-python
AutoReq: 0

%description
====================
Django Debug Toolbar
====================

.. image:: https://secure.travis-ci.org/django-debug-toolbar/django-debug-toolbar.png
    :alt: Build Status
    :target: http://travis-ci.org/django-debug-toolbar/django-debug-toolbar

The Django Debug Toolbar is a configurable set of panels that display various
debug information about the current request/response and when clicked, display
more details about the panel's content.

Here's a screenshot of the toolbar in action:

.. image:: https://raw.github.com/django-debug-toolbar/django-debug-toolbar/master/example/django-debug-toolbar.png
   :width: 908
   :height: 557

In addition to the built-in panels, a number of third-party panels are
contributed by the community.

The current version of the Debug Toolbar is 1.3.2. It works on Django 1.4 to 1.8.

If you're using Django 1.4, you will need Django ≥ 1.4.2 and Python ≥ 2.6.5.
If you're using Django ≥ 1.5, there aren't any restrictions.

Documentation, including installation and configuration instructions, is
available at http://django-debug-toolbar.readthedocs.org/.

The Django Debug Toolbar is released under the BSD license, like Django
itself. If you like it, please consider contributing!

The Django Debug Toolbar was originally created by Rob Hudson <rob@cogit8.org>
in August 2008 and was further developed by many contributors_.

.. _contributors: https://github.com/django-debug-toolbar/django-debug-toolbar/graphs/contributors


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
