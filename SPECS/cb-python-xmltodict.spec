%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name xmltodict
%define version 0.9.2
%define unmangled_version 0.9.2
%define unmangled_version 0.9.2
%define release 1

Summary: Makes working with XML feel like you are working with JSON
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Martin Blech <martinblech@gmail.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://github.com/martinblech/xmltodict
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
