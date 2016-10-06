%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name pickleshare
%define version 0.5
%define unmangled_version 0.5
%define unmangled_version 0.5
%define release 1

Summary: Tiny 'shelve'-like database with concurrency support
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ville Vainio <vivainio@gmail.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://github.com/vivainio/pickleshare
BuildRequires: cb-python
AutoReq: 0

%description
PickleShare - a small 'shelve' like datastore with concurrency support

Like shelve, a PickleShareDB object acts like a normal dictionary. Unlike shelve,
many processes can access the database simultaneously. Changing a value in 
database is immediately visible to other processes accessing the same database.

Concurrency is possible because the values are stored in separate files. Hence
the "database" is a directory where *all* files are governed by PickleShare.

Example usage::
    
    from pickleshare import *
    db = PickleShareDB('~/testpickleshare')
    db.clear()
    print "Should be empty:",db.items()
    db['hello'] = 15
    db['aku ankka'] = [1,2,313]
    db['paths/are/ok/key'] = [1,(5,46)]
    print db.keys()

This module is certainly not ZODB, but can be used for low-load
(non-mission-critical) situations where tiny code size trumps the 
advanced features of a "real" object database.

Installation guide: pip install path pickleshare


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
