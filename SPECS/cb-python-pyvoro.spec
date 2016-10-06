%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name pyvoro
%define version 1.3.2
%define unmangled_version 1.3.2
%define release 1

Summary: 2D and 3D Voronoi tessellations: a python entry point for the voro++ library.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Joe Jordan <joe.jordan@imperial.ac.uk>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://github.com/joe-jordan/pyvoro
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
