%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name decorator
%define version 4.0.2
%define unmangled_version 4.0.2
%define unmangled_version 4.0.2
%define release 1

Summary: Better living through Python with decorators
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: new BSD License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Michele Simionato <michele.simionato@gmail.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://github.com/micheles/decorator
BuildRequires: cb-python
AutoReq: 0

%description
Decorator module
=================

:Author: Michele Simionato
:E-mail: michele.simionato@gmail.com
:Requires: Python 2.6+
:Download page: http://pypi.python.org/pypi/decorator
:Installation: ``pip install decorator``
:License: BSD license

Installation
-------------

If you are lazy, just perform

 `$ pip install decorator`

which will install just the module on your system.

If you prefer to install the full distribution from source, including
the documentation, download the tarball_, unpack it and run

 `$ python setup.py install`

in the main directory, possibly as superuser.

.. _tarball: http://pypi.python.org/pypi/decorator


Testing
--------

Run

 `$ python src/tests/test.py -v`

or (if you have setuptools installed)

 `$ python setup.py test`

Notice that you may run into trouble if in your system there
is an older version of the decorator module; in such a case remove the
old version. It is safe even to copy the module `decorator.py` over
an existing one, since version 4.0 is backward-compatible.

Documentation
--------------

There are various versions of the documentation:

-  `HTML version`_ 
-  `PDF version`_ 

.. _HTML version: http://pythonhosted.org/decorator/documentation.html
.. _PDF version: https://github.com/micheles/decorator/blob/4.0.1/documentation.pdf

Repository
---------------

The project is hosted on GitHub. You can look at the source here:

 https://github.com/micheles/decorator


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
