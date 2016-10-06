%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name docutils
%define version 0.12
%define unmangled_version 0.12
%define release 1

Summary: Docutils -- Python Documentation Utilities
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: public domain, Python, 2-Clause BSD, GPL 3 (see COPYING.txt)
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: docutils-develop list <docutils-develop@lists.sourceforge.net>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://docutils.sourceforge.net/
BuildRequires: cb-python
AutoReq: 0

%description
Docutils is a modular system for processing documentation
into useful formats, such as HTML, XML, and LaTeX.  For
input Docutils supports reStructuredText, an easy-to-read,
what-you-see-is-what-you-get plaintext markup syntax.

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
%doc BUGS.txt COPYING.txt FAQ.txt HISTORY.txt README.txt RELEASE-NOTES.txt THANKS.txt docs/ licenses/
