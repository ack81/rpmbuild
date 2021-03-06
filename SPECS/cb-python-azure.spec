%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name azure
%define version 2.0.0rc5
%define unmangled_version 2.0.0rc5
%define unmangled_version 2.0.0rc5
%define release 1

Summary: Microsoft Azure Client Libraries for Python
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: Apache License 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Microsoft Corporation <ptvshelp@microsoft.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://github.com/Azure/azure-sdk-for-python
BuildRequires: cb-python
AutoReq: 0

%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure bundle.

This package does not contain any code in itself. It installs a set
of packages that provide Microsoft Azure functionality.

All packages in this bundle have been tested with Python 2.7, 3.3, 3.4 and 3.5.


Features
========

This version of the Azure package bundle consists of the following
packages. Follow the links for more information on each package.

-  `azure-mgmt v0.30.0rc5 <https://pypi.python.org/pypi/azure-mgmt/0.30.0rc5>`__
-  `azure-graphrbac v0.30.0rc5 <https://pypi.python.org/pypi/azure-graphrbac/0.30.0rc5>`__
-  `azure-batch v0.30.0rc5 <https://pypi.python.org/pypi/azure-batch/0.30.0rc5>`__
-  `azure-servicebus v0.20.1 <https://pypi.python.org/pypi/azure-servicebus/0.20.1>`__
-  `azure-servicemanagement-legacy v0.20.3 <https://pypi.python.org/pypi/azure-servicemanagement-legacy/0.20.3>`__
-  `azure-storage v0.30.0 <https://pypi.python.org/pypi/azure-storage/0.30.0>`__

Note that if you don't need all of these packages, you can install/uninstall them individually.


Installation
============

To install the Azure package bundle, type:

.. code:: shell

    pip install azure


Upgrade
=======

Upgrading from azure<1.0 is not supported. You must uninstall the old version first.

.. code:: shell

    pip uninstall azure
    pip install azure


Compatibility
=============

Some breaking changes were introduced in azure==1.0.

If you are porting your code from an older version (<1.0), be prepared
to change some import statements and rename exception classes.

For details on the breaking changes, see the
`change log <https://github.com/Azure/azure-sdk-for-python/blob/master/ChangeLog.txt>`__.


Uninstall
=========

Installing the azure bundle package installs several packages.

Use the following script to uninstall all of them.

.. code:: shell

    pip uninstall azure
    pip uninstall azure-mgmt
    pip uninstall azure-mgmt-authorization
    pip uninstall azure-mgmt-batch
    pip uninstall azure-mgmt-cdn
    pip uninstall azure-mgmt-cognitiveservices
    pip uninstall azure-mgmt-commerce
    pip uninstall azure-mgmt-compute
    pip uninstall azure-mgmt-logic
    pip uninstall azure-mgmt-network
    pip uninstall azure-mgmt-notificationhubs
    pip uninstall azure-mgmt-powerbiembedded
    pip uninstall azure-mgmt-redis
    pip uninstall azure-mgmt-resource
    pip uninstall azure-mgmt-scheduler
    pip uninstall azure-mgmt-storage
    pip uninstall azure-mgmt-web
    pip uninstall azure-mgmt-nspkg
    pip uninstall azure-batch
    pip uninstall azure-graphrbac
    pip uninstall azure-servicebus
    pip uninstall azure-storage
    pip uninstall azure-common
    pip uninstall azure-nspkg


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
