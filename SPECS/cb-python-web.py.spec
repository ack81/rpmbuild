%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name web.py
%define version 0.37
%define unmangled_version 0.37
%define release 1

Summary: web.py: makes web apps
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: Public domain
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Anand Chitipothu <anandology@gmail.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url:  http://webpy.org/
BuildRequires: cb-python
AutoReq: 0

%description
Think about the ideal way to write a web app. Write the code to make it happen.

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
