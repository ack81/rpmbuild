%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name snowballstemmer
%define version 1.2.0
%define unmangled_version 1.2.0
%define release 1

Summary: This package provides 16 stemmer algorithms (15 + Poerter English stemmer) generated from Snowball algorithms.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Yoshiki Shibukawa <yoshiki at shibu.jp>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://github.com/shibukawa/snowball_py
BuildRequires: cb-python
AutoReq: 0

%description

It includes following language algorithms:

* Danish
* Dutch
* English (Standard, Porter)
* Finnish
* French
* German
* Hungarian
* Italian
* Norwegian
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Turkish

This is a pure Python stemming library. If `PyStemmer <http://pypi.python.org/pypi/PyStemmer>`_ is available, this module uses
it to accelerate.


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
