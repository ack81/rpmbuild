%global _python_bytecompile_errors_terminate_build 0
%define debug_package %{nil}
%define __name aliyun-python-sdk-core
%define version 2.0.30
%define unmangled_version 2.0.30
%define unmangled_version 2.0.30
%define release 1

Summary: The core module of Aliyun Python sdk.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: Apache
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Aliyun <aliyun-developers-efficiency@list.alibaba-inc.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://develop.aliyun.com/sdk/python
BuildRequires: cb-python
AutoReq: 0

%description
======================
aliyun-python-sdk-core
======================


This is the core module of Aliyun Python SDK.

Aliyun Python SDK is the official software development kit. It makes things easy to integrate your Python application,
library, or script with Aliyun services.

This module works on Python versions:

   * 2.6.5 and greater


Documentation:

Please visit http://develop.aliyun.com/sdk/python

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
