%global _python_bytecompile_errors_terminate_build 0
%define debug_package %{nil}
%define __name django-haystack
%define version 2.4.0
%define unmangled_version 2.4.0
%define unmangled_version 2.4.0
%define release 1

Summary: Pluggable search for Django.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Daniel Lindsley <daniel@toastdriven.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://haystacksearch.org/
BuildRequires: cb-python
AutoReq: 0

%description
========
Haystack
========

:author: Daniel Lindsley
:date: 2013/07/28

Haystack provides modular search for Django. It features a unified, familiar
API that allows you to plug in different search backends (such as Solr_,
Elasticsearch_, Whoosh_, Xapian_, etc.) without having to modify your code.

.. _Solr: http://lucene.apache.org/solr/
.. _Elasticsearch: http://elasticsearch.org/
.. _Whoosh: https://bitbucket.org/mchaput/whoosh/
.. _Xapian: http://xapian.org/

Haystack is BSD licensed, plays nicely with third-party app without needing to
modify the source and supports advanced features like faceting, More Like This,
highlighting, spatial search and spelling suggestions.

You can find more information at http://haystacksearch.org/.


Getting Help
============

There is a mailing list (http://groups.google.com/group/django-haystack/)
available for general discussion and an IRC channel (#haystack on
irc.freenode.net).


Documentation
=============

* Development version: http://docs.haystacksearch.org/
* v2.3.X: http://django-haystack.readthedocs.org/en/v2.3.0/
* v2.2.X: http://django-haystack.readthedocs.org/en/v2.2.0/
* v2.1.X: http://django-haystack.readthedocs.org/en/v2.1.0/
* v2.0.X: http://django-haystack.readthedocs.org/en/v2.0.0/
* v1.2.X: http://django-haystack.readthedocs.org/en/v1.2.7/
* v1.1.X: http://django-haystack.readthedocs.org/en/v1.1/

Build Status
============

.. image:: https://travis-ci.org/django-haystack/django-haystack.svg?branch=master
   :target: https://travis-ci.org/django-haystack/django-haystack

Requirements
============

Haystack has a relatively easily-met set of requirements.

* Python 2.7+ or Python 3.3+
* Django 1.6+

Additionally, each backend has its own requirements. You should refer to
http://django-haystack.readthedocs.org/en/latest/installing_search_engines.html for more
details.


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
