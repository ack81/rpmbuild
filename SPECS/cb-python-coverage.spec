%global _python_bytecompile_errors_terminate_build 0
%define debug_package %{nil}
%define __name coverage
%define version 4.1
%define unmangled_version 4.1
%define unmangled_version 4.1
%define release 1

Summary: Code coverage measurement for Python
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: Apache 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Ned Batchelder and others <ned@nedbatchelder.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://coverage.readthedocs.io
BuildRequires: cb-python
AutoReq: 0

%description
.. Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
.. For details: https://bitbucket.org/ned/coveragepy/src/default/NOTICE.txt

===========
Coverage.py
===========

Code coverage testing for Python.

|  |license| |versions| |status| |docs|
|  |ci-status| |win-ci-status| |codecov|
|  |kit| |format| |downloads|

Coverage.py measures code coverage, typically during test execution. It uses
the code analysis tools and tracing hooks provided in the Python standard
library to determine which lines are executable, and which have been executed.

Coverage.py runs on CPython 2.6, 2.7, and 3.3 through 3.6; PyPy 4.0 and 5.1;
and PyPy3 2.4.

Documentation is on `Read the Docs <https://coverage.readthedocs.io>`_.
Code repository and issue tracker are on `Bitbucket <http://bitbucket.org/ned/coveragepy>`_,
with a mirrored repository on `GitHub <https://github.com/nedbat/coveragepy>`_.

**New in 4.1:** much-improved branch coverage.

New in 4.0: ``--concurrency``, plugins for non-Python files, setup.cfg
support, --skip-covered, HTML filtering, and more than 50 issues closed.


Getting Started
---------------

See the `quick start <https://coverage.readthedocs.io/#quick-start>`_
section of the docs.


License
-------

Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0.
For details, see https://bitbucket.org/ned/coveragepy/src/default/NOTICE.txt.


.. |ci-status| image:: https://travis-ci.org/nedbat/coveragepy.svg?branch=master
    :target: https://travis-ci.org/nedbat/coveragepy
    :alt: Build status
.. |win-ci-status| image:: https://ci.appveyor.com/api/projects/status/bitbucket/ned/coveragepy?svg=true
    :target: https://ci.appveyor.com/project/nedbat/coveragepy
    :alt: Windows build status
.. |docs| image:: https://readthedocs.org/projects/coverage/badge/?version=latest&style=flat
    :target: https://coverage.readthedocs.io
    :alt: Documentation
.. |reqs| image:: https://requires.io/github/nedbat/coveragepy/requirements.svg?branch=master
    :target: https://requires.io/github/nedbat/coveragepy/requirements/?branch=master
    :alt: Requirements status
.. |kit| image:: https://badge.fury.io/py/coverage.svg
    :target: https://pypi.python.org/pypi/coverage
    :alt: PyPI status
.. |format| image:: https://img.shields.io/pypi/format/coverage.svg
    :target: https://pypi.python.org/pypi/coverage
    :alt: Kit format
.. |downloads| image:: https://img.shields.io/pypi/dw/coverage.svg
    :target: https://pypi.python.org/pypi/coverage
    :alt: Weekly PyPI downloads
.. |versions| image:: https://img.shields.io/pypi/pyversions/coverage.svg
    :target: https://pypi.python.org/pypi/coverage
    :alt: Python versions supported
.. |status| image:: https://img.shields.io/pypi/status/coverage.svg
    :target: https://pypi.python.org/pypi/coverage
    :alt: Package stability
.. |license| image:: https://img.shields.io/pypi/l/coverage.svg
    :target: https://pypi.python.org/pypi/coverage
    :alt: License
.. |codecov| image:: http://codecov.io/github/nedbat/coveragepy/coverage.svg?branch=master
    :target: http://codecov.io/github/nedbat/coveragepy?branch=master
    :alt: Coverage!


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
