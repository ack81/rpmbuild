%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name pycrypto
%define version 2.6.1
%define unmangled_version 2.6.1
%define release 1

Summary: Cryptographic modules for Python.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Dwayne C. Litzenberger <dlitz@dlitz.net>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://www.pycrypto.org/
BuildRequires: cb-python
AutoReq: 0

%description
UNKNOWN

%prep
%setup -n %{__name}-%{unmangled_version}

%build
env CFLAGS="$RPM_OPT_FLAGS" /opt/cb/bin/python setup.py build

%install
/opt/cb/bin/python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
