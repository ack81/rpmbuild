%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name PyChef
%define version 0.2.2
%define unmangled_version 0.2.2
%define unmangled_version 0.2.2
%define release 1

Summary: Python implementation of a Chef API client.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Noah Kantrowitz <noah@coderanger.net>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://github.com/coderanger/pychef
BuildRequires: cb-python
AutoReq: 0

%description
PyChef
======

.. image:: https://secure.travis-ci.org/coderanger/pychef.png?branch=master
    :target: http://travis-ci.org/coderanger/pychef

A Python API for interacting with a Chef server.

Example
-------

::

    from chef import autoconfigure, Node
    
    api = autoconfigure()
    n = Node('web1')
    print n['fqdn']
    n['myapp']['version'] = '1.0'
    n.save()

Further Reading
---------------

For more information check out http://pychef.readthedocs.org/en/latest/index.html


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
