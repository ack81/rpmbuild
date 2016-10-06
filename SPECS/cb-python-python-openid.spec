%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name python-openid
%define version 2.2.5
%define unmangled_version 2.2.5
%define release 1

Summary: OpenID support for servers and consumers.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: JanRain <openid@janrain.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://github.com/openid/python-openid
BuildRequires: cb-python
AutoReq: 0

%description
This is a set of Python packages to support use of
the OpenID decentralized identity system in your application.  Want to enable
single sign-on for your web site?  Use the openid.consumer package.  Want to
run your own OpenID server? Check out openid.server.  Includes example code
and support for a variety of storage back-ends.

%prep
%setup -n %{__name}-%{unmangled_version}

%build
/opt/cb/bin/python setup.py build

%install
/opt/cb/bin/python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
