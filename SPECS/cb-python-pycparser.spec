%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name pycparser
%define version 2.14
%define unmangled_version 2.14
%define unmangled_version 2.14
%define release 1

Summary: C parser in Python
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Eli Bendersky <eliben@gmail.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://github.com/eliben/pycparser
BuildRequires: cb-python
AutoReq: 0

%description

        pycparser is a complete parser of the C language, written in
        pure Python using the PLY parsing library.
        It parses C code into an AST and can serve as a front-end for
        C compilers or analysis tools.
    

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
