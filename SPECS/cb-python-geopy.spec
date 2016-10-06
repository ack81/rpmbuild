%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name geopy
%define version 1.10.0
%define unmangled_version 1.10.0
%define unmangled_version 1.10.0
%define release 1

Summary: Python Geocoding Toolbox
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: GeoPy Contributors <uijllji@gmail>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://github.com/geopy/geopy
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
