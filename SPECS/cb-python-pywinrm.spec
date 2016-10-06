%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name pywinrm
%define version 0.0.3
%define unmangled_version 0.0.3
%define release 1

Summary: Python library for Windows Remote Management
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: MIT license
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Alexey Diyan <alexey.diyan@gmail.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://github.com/diyan/pywinrm/
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
