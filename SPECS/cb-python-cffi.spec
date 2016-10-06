%global _python_bytecompile_errors_terminate_build 0
%define debug_package %{nil}
%define __name cffi
%define version 1.2.1
%define unmangled_version 1.2.1
%define unmangled_version 1.2.1
%define release 1

Summary: Foreign Function Interface for Python calling C code.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Armin Rigo, Maciej Fijalkowski <python-cffi@googlegroups.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://cffi.readthedocs.org
BuildRequires: cb-python
AutoReq: 0

%description

CFFI
====

Foreign Function Interface for Python calling C code.
Please see the `Documentation <http://cffi.readthedocs.org/>`_.

Contact
-------

`Mailing list <https://groups.google.com/forum/#!forum/python-cffi>`_


%prep
%setup -n %{__name}-%{unmangled_version} -n %{__name}-%{unmangled_version}

%build
env CFLAGS="$RPM_OPT_FLAGS" /opt/cb/bin/python setup.py build

%install
/opt/cb/bin/python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
