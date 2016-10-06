%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name enum34
%define version 1.1.6
%define unmangled_version 1.1.6
%define unmangled_version 1.1.6
%define release 1

Summary: Python 3.4 Enum backported to 3.3, 3.2, 3.1, 2.7, 2.6, 2.5, and 2.4
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: BSD License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ethan Furman <ethan@stoneleaf.us>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://bitbucket.org/stoneleaf/enum34
BuildRequires: cb-python
AutoReq: 0

%description
enum --- support for enumerations
========================================

An enumeration is a set of symbolic names (members) bound to unique, constant
values.  Within an enumeration, the members can be compared by identity, and
the enumeration itself can be iterated over.

    from enum import Enum

    class Fruit(Enum):
        apple = 1
        banana = 2
        orange = 3

    list(Fruit)
    # [<Fruit.apple: 1>, <Fruit.banana: 2>, <Fruit.orange: 3>]

    len(Fruit)
    # 3

    Fruit.banana
    # <Fruit.banana: 2>

    Fruit['banana']
    # <Fruit.banana: 2>

    Fruit(2)
    # <Fruit.banana: 2>

    Fruit.banana is Fruit['banana'] is Fruit(2)
    # True

    Fruit.banana.name
    # 'banana'

    Fruit.banana.value
    # 2

Repository and Issue Tracker at https://bitbucket.org/stoneleaf/enum34.


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
