%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name oauth2
%define version 1.5.211
%define unmangled_version 1.5.211
%define unmangled_version 1.5.211
%define release 1

Summary: library for OAuth version 1.0
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: MIT License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Joe Stump <joe@simplegeo.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://github.com/simplegeo/python-oauth2
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
