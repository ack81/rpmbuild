%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name azure-storage
%define version 0.32.0
%define unmangled_version 0.32.0
%define unmangled_version 0.32.0
%define release 1

Summary: Microsoft Azure Storage Client Library for Python
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
Url: https://github.com/Azure/azure-storage-python
BuildRequires: cb-python
AutoReq: 0

%description
Microsoft Azure Storage SDK for Python
======================================

This project provides a client library in Python that makes it easy to
consume Microsoft Azure Storage services. For documentation please see
the Microsoft Azure `Python Developer Center`_ and our `GitHub.io Reference`_ Page.

    If you are looking for the Service Bus or Azure Management
    libraries, please visit
    https://github.com/Azure/azure-sdk-for-python.


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

If you are upgrading from a version older than 0.30.0, see the upgrade doc, the 
usage samples in the samples directory, and the ChangeLog and BreakingChanges.

Features
========

-  Blob

   -  Create/Read/Update/Delete Containers
   -  Create/Read/Update/Delete Blobs
   -  Advanced Blob Operations

-  Queue

   -  Create/Delete Queues
   -  Insert/Peek Queue Messages
   -  Advanced Queue Operations

-  Table

   -  Create/Read/Update/Delete Tables
   -  Create/Read/Update/Delete Entities
   -  Batch operations
   -  Advanced Table Operations

-  Files

   -  Create/Update/Delete Shares
   -  Create/Update/Delete Directories
   -  Create/Read/Update/Delete Files
   -  Advanced File Operations

Getting Started
===============

Download
--------

Option 1: Via PyPi
~~~~~~~~~~~~~~~~~~

To install via the Python Package Index (PyPI), type:
::

    pip install azure-storage

Option 2: Source Via Git
~~~~~~~~~~~~~~~~~~~~~~~~

To get the source code of the SDK via git just type:

::

    git clone git://github.com/Azure/azure-storage-python.git
    cd ./azure-storage-python
    python setup.py install

Option 3: Source Zip
~~~~~~~~~~~~~~~~~~~~

Download a zip of the code via GitHub or PyPi. Then, type:

::

    cd ./azure-storage-python
    python setup.py install

Minimum Requirements
--------------------

-  Python 2.7, 3.3, 3.4, or 3.5.
-  See setup.py for dependencies

Usage
-----

To use this SDK to call Microsoft Azure storage services, you need to
first `create an account`_.

Code Sample
-----------

See the samples directory for blob, queue, table, and file usage samples.

Need Help?
==========

Be sure to check out the Microsoft Azure `Developer Forums on MSDN`_ or
the `Developer Forums on Stack Overflow`_ if you have trouble with the
provided code.

Contribute Code or Provide Feedback
===================================

If you would like to become an active contributor to this project, please
follow the instructions provided in `Azure Projects Contribution
Guidelines`_. You can find more details for contributing in the [CONTRIBUTING.md doc](CONTRIBUTING.md).

If you encounter any bugs with the library, please file an issue in the
`Issues`_ section of the project.

Learn More
==========

-  `Python Developer Center`_
-  `Azure Storage Service`_
-  `Azure Storage Team Blog`_
-  `GitHub.io Reference`_

.. _Python Developer Center: http://azure.microsoft.com/en-us/develop/python/
.. _GitHub.io Reference: http://azure.github.io/azure-storage-python/
.. _here: https://github.com/Azure/azure-storage-python/archive/master.zip
.. _create an account: https://account.windowsazure.com/signup
.. _Developer Forums on MSDN: http://social.msdn.microsoft.com/Forums/windowsazure/en-US/home?forum=windowsazuredata
.. _Developer Forums on Stack Overflow: http://stackoverflow.com/questions/tagged/azure+windows-azure-storage
.. _Azure Projects Contribution Guidelines: http://azure.github.io/guidelines.html
.. _Issues: https://github.com/Azure/azure-storage-python/issues
.. _Azure Storage Service: http://azure.microsoft.com/en-us/documentation/services/storage/
.. _Azure Storage Team Blog: http://blogs.msdn.com/b/windowsazurestorage/


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
