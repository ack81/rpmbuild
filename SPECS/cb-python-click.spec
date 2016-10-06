%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name click
%define version 6.3
%define unmangled_version 6.3
%define unmangled_version 6.3
%define release 1

Summary: A simple wrapper around optparse for powerful command line utilities.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Armin Ronacher <armin.ronacher@active-4.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://github.com/mitsuhiko/click
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
