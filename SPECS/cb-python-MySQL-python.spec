%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name MySQL-python
%define version 1.2.3
%define unmangled_version 1.2.3
%define unmangled_version 1.2.3
%define release 1

Summary: Python interface to MySQL
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: GPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: MySQL-python SourceForge Project
Packager: Adam Kinney <akinney@cloudbolt.io>
Requires: python
Url: http://sourceforge.net/projects/mysql-python
Distribution: Red Stains Linux
BuildRequires: cb-python
AutoReq: 0

%description

=========================
Python interface to MySQL
=========================

MySQLdb is an interface to the popular MySQL_ database server for
Python.  The design goals are:

- Compliance with Python database API version 2.0 [PEP-0249]_

- Thread-safety

- Thread-friendliness (threads will not block each other)

MySQL-3.23 through 5.0 and Python-2.3 through 2.6 are currently
supported. Python-3.0 will be supported in a future release.

MySQLdb is `Free Software`_.

.. _MySQL: http://www.mysql.com/
.. _`Free Software`: http://www.gnu.org/
.. [PEP-0249] http://www.python.org/peps/pep-0249.html

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
# %doc README MANIFEST doc/*.txt
