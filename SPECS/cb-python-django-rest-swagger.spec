%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name django-rest-swagger
%define version 0.3.4
%define unmangled_version 0.3.4
%define unmangled_version 0.3.4
%define release 1

Summary: Swagger UI for Django REST Framework 2.3.8+
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: FreeBSD License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ellery Newcomer <ellery-newcomer@utulsa.edu>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://github.com/marcgibbons/django-rest-swagger
BuildRequires: cb-python
AutoReq: 0

%description

Django REST Swagger

An API documentation generator for Swagger UI and Django REST Framework version 2.3.8+

Installation
From pip:

pip install django-rest-swagger

Project @ https://github.com/marcgibbons/django-rest-swagger
Docs @ http://django-rest-swagger.readthedocs.org/


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
