%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name ipaddress
%define version 1.0.14
%define unmangled_version 1.0.14
%define unmangled_version 1.0.14
%define release 1

Summary: IPv4/IPv6 manipulation library
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: Python Software Foundation License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Philipp Hagemeister <phihag@phihag.de>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://github.com/phihag/ipaddress
BuildRequires: cb-python
AutoReq: 0

%description
Port of the 3.3+ ipaddress module to 2.6, 2.7, 3.2

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
