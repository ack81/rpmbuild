%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name futures
%define version 3.0.5
%define unmangled_version 3.0.5
%define unmangled_version 3.0.5
%define release 1

Summary: Backport of the concurrent.futures package from Python 3.2
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Alex Gronholm <alex.gronholm+pypi@nextday.fi>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://github.com/agronholm/pythonfutures
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
