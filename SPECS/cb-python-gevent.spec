%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name gevent
%define version 1.0.2
%define unmangled_version 1.0.2
%define unmangled_version 1.0.2
%define release 1

Summary: Coroutine-based network library
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Denis Bilenko <denis.bilenko@gmail.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://www.gevent.org/
BuildRequires: cb-python
AutoReq: 0

%description
gevent_
=======

gevent_ is a coroutine-based Python networking library.

Features include:

* Fast event loop based on libev_.
* Lightweight execution units based on greenlet_.
* Familiar API that re-uses concepts from the Python standard library.
* Cooperative sockets with SSL support.
* DNS queries performed through c-ares_ or a threadpool.
* Ability to use standard library and 3rd party modules written for standard blocking sockets

gevent_ is `inspired by eventlet`_ but features more consistent API, simpler implementation and better performance. Read why others `use gevent`_ and check out the list of the `open source projects based on gevent`_.

gevent_ is written and maintained by `Denis Bilenko`_ and is licensed under MIT license.


get gevent
----------

Install Python 2.5, 2.6 or 2.7, and greenlet_ extension.

Download the latest release from `Python Package Index`_ or clone `the repository`_.

Read the documentation online at http://www.gevent.org

Post feedback and issues on the `bug tracker`_, `mailing list`_, blog_ and `twitter (@gevent)`_.


installing from github
----------------------

To install the latest development version:

  pip install cython git+git://github.com/gevent/gevent.git#egg=gevent


running tests
-------------

  python setup.py build

  cd greentest

  PYTHONPATH=.. python testrunner.py --config ../known_failures.py


.. _gevent: http://www.gevent.org
.. _greenlet: http://pypi.python.org/pypi/greenlet
.. _libev: http://libev.schmorp.de/
.. _c-ares: http://c-ares.haxx.se/
.. _inspired by eventlet: http://blog.gevent.org/2010/02/27/why-gevent/
.. _use gevent: http://groups.google.com/group/gevent/browse_thread/thread/4de9703e5dca8271
.. _open source projects based on gevent: https://github.com/gevent/gevent/wiki/Projects
.. _Denis Bilenko: http://denisbilenko.com
.. _Python Package Index: http://pypi.python.org/pypi/gevent
.. _the repository: https://github.com/gevent/gevent
.. _bug tracker: https://github.com/gevent/gevent/wiki/Projects
.. _mailing list: http://groups.google.com/group/gevent
.. _blog: http://blog.gevent.org
.. _twitter (@gevent): http://twitter.com/gevent


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
