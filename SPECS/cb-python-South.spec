%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name South
%define version 1.0.2
%define unmangled_version 1.0.2
%define unmangled_version 1.0.2
%define release 1

Summary: South: Migrations for Django
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Andrew Godwin & Andy McCurdy <south@aeracode.org>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://south.aeracode.org/
BuildRequires: cb-python
AutoReq: 0

%description
South is an intelligent database migrations library for the Django web framework. It is database-independent and DVCS-friendly, as well as a whole host of other features.

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
