%global _python_bytecompile_errors_terminate_build 0
%define debug_package %{nil}
%define __name args
%define version 0.1.0
%define unmangled_version 0.1.0
%define unmangled_version 0.1.0
%define release 1

Summary: Command Arguments for Humans.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Kenneth Reitz <me@kennethreitz.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://github.com/kennethreitz/args
BuildRequires: cb-python
AutoReq: 0

%description

args
~~~~

This simple module gives you an elegant interface for your command line argumemnts.



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
