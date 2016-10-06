%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name ipython_genutils
%define version 0.1.0
%define unmangled_version 0.1.0
%define unmangled_version 0.1.0
%define release 1

Summary: Vestigial utilities from IPython
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: IPython Development Team <ipython-dev@scipy.org>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://ipython.org
BuildRequires: cb-python
AutoReq: 0

%description
Pretend this doesn't exist. Nobody should use it.

%prep
%setup -n %{__name}-%{unmangled_version} -n %{__name}-%{unmangled_version}

%build
/opt/cb/bin/python setup.py build

%install
/opt/cb/bin/python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
