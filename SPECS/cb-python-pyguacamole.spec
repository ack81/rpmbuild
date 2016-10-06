%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name pyguacamole
%define version 0.3
%define unmangled_version 0.3
%define unmangled_version 0.3
%define release 1

Summary: A Guacamole python client library.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: The MIT License (MIT)
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Mohab Usama <mohab.usama@gmail.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://github.com/mohabusama/pyguacamole
BuildRequires: cb-python
AutoReq: 0

%description
===========
PyGuacamole
===========

A Python client library for communication with `Guacamole <http://guac-dev.org/>`_ server (guacd)

.. image:: https://travis-ci.org/mohabusama/pyguacamole.svg?branch=master
    :target: https://travis-ci.org/mohabusama/pyguacamole

.. image:: https://img.shields.io/pypi/v/pyguacamole.svg
   :target: https://python.org/pypi/pyguacamole/

.. image:: https://img.shields.io/pypi/dm/pyguacamole.svg
   :target: https://python.org/pypi/pyguacamole/

.. image:: https://img.shields.io/github/license/mohabusama/pyguacamole.svg
   :target: https://python.org/pypi/pyguacamole/

.. image:: https://img.shields.io/pypi/status/pyguacamole.svg
   :target: https://python.org/pypi/pyguacamole/


Installation
============

Using pip

::

    $ pip install pyguacamole


From source

::

    $ python setup.py install


Usage
=====

GuacamoleClient handles communication with a running *guacd* server via `Guacamole Protocol <http://guac-dev.org/doc/gug/protocol-reference.html>`_.

GuacamoleClient must be used by a broker server which handles communication with a Javscript application running in the browser. GuacamoleClient implements the methods that enables communication with guacd server (send & receive).

First step should be establishing *handshake* with guacd server, then
Broker server should handle instruction sending and receiving:

- **send**: send instruction *to* guacd server
- **receive**: receive instruction *from* guacd server

::

    >>> from guacamole.client import GuacamoleClient
    >>> client = GuacamoleClient('127.0.0.1', 4822)
    >>> client.handshake(protocol='rdp', hostname='localhost', port=3389)


Once instruction is received from guacd server, it should be sent immediately to the browser

::

    >>> instruction = client.receive()
    >>> instruction
    '4.size,1.0,4.1024,3.768;'

and once instruction is sent from browser, it should be sent immediately to guacd server

::

    >>> instruction = '5.mouse,3.400,3.500;'
    >>> client.send(instruction)


Notes
=====

PyGuacamole is released under the `MIT License <https://raw.githubusercontent.com/mohabusama/pyguacamole/master/LICENSE>`_ and is based on the initial effort by Rescale `django-guacamole <https://github.com/rescale/django-guacamole>`_ project.


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
