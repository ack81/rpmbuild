%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name lxml
%define version 3.4.4
%define unmangled_version 3.4.4
%define unmangled_version 3.4.4
%define release 1

Summary: Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: lxml dev team <lxml-dev@lxml.de>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://lxml.de/
BuildRequires: cb-python
AutoReq: 0

%description
lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries.  It
provides safe and convenient access to these libraries using the ElementTree
API.

It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT, C14N and much more.

To contact the project, go to the `project home page
<http://lxml.de/>`_ or see our bug tracker at
https://launchpad.net/lxml

In case you want to use the current in-development version of lxml,
you can get it from the github repository at
https://github.com/lxml/lxml .  Note that this requires Cython to
build the sources, see the build instructions on the project home
page.  To the same end, running ``easy_install lxml==dev`` will
install lxml from
https://github.com/lxml/lxml/tarball/master#egg=lxml-dev if you have
an appropriate version of Cython installed.


After an official release of a new stable series, bug fixes may become
available at
https://github.com/lxml/lxml/tree/lxml-3.4 .
Running ``easy_install lxml==3.4bugfix`` will install
the unreleased branch state from
https://github.com/lxml/lxml/tarball/lxml-3.4#egg=lxml-3.4bugfix
as soon as a maintenance branch has been established.  Note that this
requires Cython to be installed at an appropriate version for the build.

3.4.4 (2015-04-25)
==================

Bugs fixed
----------

* An ElementTree compatibility test added in lxml 3.4.3 that failed in
  Python 3.4+ was removed again.




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
