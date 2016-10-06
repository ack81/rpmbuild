%global _python_bytecompile_errors_terminate_build 0
%define debug_package %{nil}
%define __name bigsuds
%define version 1.0.1
%define unmangled_version 1.0.1
%define release 1

Summary: Library for F5 Networks iControl API
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: F5 Networks, Inc. <noreply@f5.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://devcentral.f5.com
BuildRequires: cb-python
AutoReq: 0

%description
UNKNOWN

%prep
%setup -n %{__name}-%{unmangled_version}

%build
/opt/cb/bin/python setup.py build

%install
/opt/cb/bin/python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
