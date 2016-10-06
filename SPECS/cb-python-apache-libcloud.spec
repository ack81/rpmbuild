%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name apache-libcloud
%define version 0.20.1
%define unmangled_version 0.20.1
%define unmangled_version 0.20.1
%define release 1

Summary: A standard Python library that abstracts away differences among multiple cloud provider APIs. For more information and documentation, please see http://libcloud.apache.org
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: Apache License (2.0)
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Apache Software Foundation <dev@libcloud.apache.org>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://libcloud.apache.org/
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
