%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name certifi
%define version 2016.2.28
%define unmangled_version 2016.2.28
%define unmangled_version 2016.2.28
%define release 1

Summary: Python package for providing Mozilla's CA Bundle.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: ISC
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Kenneth Reitz <me@kennethreitz.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://certifi.io/
BuildRequires: cb-python
AutoReq: 0

%description
Certifi: Python SSL Certificates
================================

`Certifi`_ is a carefully curated collection of Root Certificates for
validating the trustworthiness of SSL certificates while verifying the identity
of TLS hosts. It has been extracted from the `Requests`_ project.

Installation
------------

``certifi`` is available on PyPI. Simply install it with ``pip``::

    $ pip install certifi

Usage
-----

To reference the installed CA Bundle, you can use the built-in function::

    >>> import certifi

    >>> certifi.where()
    '/usr/local/lib/python2.7/site-packages/certifi/cacert.pem'

Enjoy!

1024-bit Root Certificates
~~~~~~~~~~~~~~~~~~~~~~~~~~

Browsers and certificate authorities have concluded that 1024-bit keys are
unacceptably weak for certificates, particularly root certificates. For this
reason, Mozilla has removed any weak (i.e. 1024-bit key) certificate from its
bundle, replacing it with an equivalent strong (i.e. 2048-bit or greater key)
certifiate from the same CA. Because Mozilla removed these certificates from
its bundle, ``certifi`` removed them as well.

Unfortunately, old versions of OpenSSL (less than 1.0.2) sometimes fail to
validate certificate chains that use the strong roots. For this reason, if you
fail to validate a certificate using the ``certifi.where()`` mechanism, you can
intentionally re-add the 1024-bit roots back into your bundle by calling
``certifi.old_where()`` instead. This is not recommended in production: if at
all possible you should upgrade to a newer OpenSSL. However, if you have no
other option, this may work for you.

.. _`Certifi`: http://certifi.io/en/latest/
.. _`Requests`: http://docs.python-requests.org/en/latest/


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
