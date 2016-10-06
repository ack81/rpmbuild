%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name pysaml2
%define version 2.2.0
%define unmangled_version 2.2.0
%define unmangled_version 2.2.0
%define release 1

Summary: Python implementation of SAML Version 2 to be used in a WSGI environment
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: Apache 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Roland Hedberg <roland.hedberg@adm.umu.se>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://github.com/rohe/pysaml2
BuildRequires: cb-python
AutoReq: 0

%description
UNKNOWN

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
