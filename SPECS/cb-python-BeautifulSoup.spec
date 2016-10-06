%global _python_bytecompile_errors_terminate_build 0
%define debug_package %{nil}
%define __name BeautifulSoup
%define version 3.2.1
%define unmangled_version 3.2.1
%define release 1

Summary: HTML/XML parser for quick-turnaround applications like screen-scraping.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Leonard Richardson <leonardr@segfault.org>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://www.crummy.com/software/BeautifulSoup/
BuildRequires: cb-python
AutoReq: 0

%description
Beautiful Soup parses arbitrarily invalid SGML and provides a variety of methods and Pythonic idioms for iterating and searching the parse tree.

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
