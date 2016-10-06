%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name django-classy-tags
%define version 0.6.2
%define unmangled_version 0.6.2
%define unmangled_version 0.6.2
%define release 1

Summary: Class based template tags for Django
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jonas Obrist <jonas.obrist@divio.ch>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://github.com/ojii/django-classy-tags
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
