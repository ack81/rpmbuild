%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name azure-common
%define version 1.1.4
%define unmangled_version 1.1.4
%define unmangled_version 1.1.4
%define release 1

Summary: Microsoft Azure Client Library for Python (Common)
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: Apache License 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Microsoft Corporation <ptvshelp@microsoft.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://github.com/Azure/azure-sdk-for-python
BuildRequires: cb-python
AutoReq: 0

%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure common code.

This package provides shared code by the Azure packages.

If you are looking to install the Azure client libraries, see the
`azure <https://pypi.python.org/pypi/azure>`__ bundle package.


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
