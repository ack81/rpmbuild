%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name pyasn1
%define version 0.1.8
%define unmangled_version 0.1.8
%define unmangled_version 0.1.8
%define release 1

Summary: ASN.1 types and codecs
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ilya Etingof <ilya@glas.net> <ilya@glas.net>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://sourceforge.net/projects/pyasn1/
BuildRequires: cb-python
AutoReq: 0

%description
A pure-Python implementation of ASN.1 types and DER/BER/CER codecs (X.208).

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
