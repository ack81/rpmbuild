%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name netaddr
%define version 0.7.12
%define unmangled_version 0.7.12
%define release 1

Summary: Pythonic manipulation of IPv4, IPv6, CIDR, EUI and MAC network addresses
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: BSD License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: David P. D. Moss <drkjam@gmail.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://github.com/drkjam/netaddr/
BuildRequires: cb-python
AutoReq: 0

%description

A pure Python network address representation and manipulation library.

netaddr provides a Pythonic way of working with :-

- IPv4 and IPv6 addresses and subnets
- MAC addresses, OUI and IAB identifiers, IEEE EUI-64 identifiers
- arbitrary (non-aligned) IP address ranges and IP address sets
- various non-CIDR IP range formats such as nmap and glob-style formats

Included are routines for :-

- generating, sorting and summarizing IP addresses and networks
- performing easy conversions between address notations and formats
- detecting, parsing and formatting network address representations
- performing set-based operations on groups of IP addresses and subnets
- working with arbitrary IP address ranges and formats
- accessing OUI and IAB organisational information published by IEEE
- accessing IP address and block information published by IANA

For details on the latest updates and changes, see :-

    http://github.com/drkjam/netaddr/blob/rel-0.7.x/CHANGELOG

API documentation for the latest release is available here :-

    http://packages.python.org/netaddr/


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
