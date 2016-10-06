%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name pyvmomi
%define version 5.5.0
%define unmangled_version 5.5.0
%define unmangled_version 5.5.0
%define release 1

Summary: VMware vSphere Python SDK
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: Apache
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: VMware, Inc. <jhu@vmware.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://github.com/vmware/pyvmomi
BuildRequires: cb-python
AutoReq: 0

%description
pyVmomi is a Python SDK for the VMware vSphere API that allows you to
manipulate ESX, ESXi, and vCenter using scripts.

To get started, check out the examples in `sample/poweronvm.py` and
`sample/getallvms.py`.

You can install this as a package. Just run `python setup.py bdist_egg`
and then use `pip` or `easy_install` to deploy it on your system.

There are other bindings of this API in other languages. See:

* **vijava** (Java): http://vijava.sourceforge.net/
* **rbvmomi** (Ruby): https://github.com/vmware/rbvmomi
* **vSphere SDK for Perl** (non-free): https://my.vmware.com/group/vmware/details?downloadGroup=VSP510-SDKPERL-510&productId=285

Have fun!


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
