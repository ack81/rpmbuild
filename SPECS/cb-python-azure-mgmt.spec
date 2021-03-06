%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name azure-mgmt
%define version 0.30.0rc5
%define unmangled_version 0.30.0rc5
%define unmangled_version 0.30.0rc5
%define release 1

Summary: Microsoft Azure Resource Management Client Libraries for Python
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

This is the Microsoft Azure Resource Management bundle.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package does not contain any code in itself. It installs a set
of packages that provide management APIs for the various Azure services.

All packages in this bundle have been tested with Python 2.7, 3.3, 3.4 and 3.5.

For a more complete set of Azure libraries, see the `azure <https://pypi.python.org/pypi/azure>`__ bundle package.


Compatibility
=============

**IMPORTANT**: If you have an earlier version of the azure package
(version < 1.0), you should uninstall it before installing this package.

You can check the version using pip:

.. code:: shell

    pip freeze

If you see azure==0.11.0 (or any version below 1.0), uninstall it first:

.. code:: shell

    pip uninstall azure


Features
========

This version of the Azure Management package bundle consists of the
following packages. Follow the links for more information on each package.

-  `azure-mgmt-authorization v0.30.0rc5 <https://pypi.python.org/pypi/azure-mgmt-authorization/0.30.0rc5>`__
-  `azure-mgmt-batch v0.30.0rc5 <https://pypi.python.org/pypi/azure-mgmt-batch/0.30.0rc5>`__
-  `azure-mgmt-cdn v0.30.0rc5 <https://pypi.python.org/pypi/azure-mgmt-cdn/0.30.0rc5>`__
-  `azure-mgmt-cognitiveservices v0.30.0rc5 <https://pypi.python.org/pypi/azure-mgmt-cognitiveservices/0.30.0rc5>`__
-  `azure-mgmt-compute v0.30.0rc5 <https://pypi.python.org/pypi/azure-mgmt-compute/0.30.0rc5>`__
-  `azure-mgmt-logic v0.30.0rc5 <https://pypi.python.org/pypi/azure-mgmt-logic/0.30.0rc5>`__
-  `azure-mgmt-network v0.30.0rc5 <https://pypi.python.org/pypi/azure-mgmt-network/0.30.0rc5>`__
-  `azure-mgmt-notificationhubs v0.30.0rc5 <https://pypi.python.org/pypi/azure-mgmt-notificationhubs/0.30.0rc5>`__
-  `azure-mgmt-powerbiembedded v0.30.0rc5 <https://pypi.python.org/pypi/azure-mgmt-powerbiembedded/0.30.0rc5>`__
-  `azure-mgmt-redis v0.30.0rc5 <https://pypi.python.org/pypi/azure-mgmt-redis/0.30.0rc5>`__
-  `azure-mgmt-resource v0.30.0rc5 <https://pypi.python.org/pypi/azure-mgmt-resource/0.30.0rc5>`__
-  `azure-mgmt-scheduler v0.30.0rc5 <https://pypi.python.org/pypi/azure-mgmt-scheduler/0.30.0rc5>`__
-  `azure-mgmt-storage v0.30.0rc5 <https://pypi.python.org/pypi/azure-mgmt-storage/0.30.0rc5>`__
-  `azure-mgmt-web v0.30.0rc5 <https://pypi.python.org/pypi/azure-mgmt-web/0.30.0rc5>`__

Note that if you don't need all of these packages, you can install/uninstall them individually.


Installation
============

To install the Azure Resource Management bundle, type:

.. code:: shell

    pip install azure-mgmt



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
