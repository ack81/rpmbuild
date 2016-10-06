%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name django-extensions
%define version 1.5.5
%define unmangled_version 1.5.5
%define unmangled_version 1.5.5
%define release 1

Summary: Extensions for Django
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: MIT License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Bas van Oostveen <v.oostveen@gmail.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://github.com/django-extensions/django-extensions
BuildRequires: cb-python
AutoReq: 0

%description
django-extensions bundles several useful
additions for Django projects. See the project page for more information:
  http://github.com/django-extensions/django-extensions

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
