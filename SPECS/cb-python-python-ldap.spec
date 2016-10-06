%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name python-ldap
%define version 2.4.20
%define unmangled_version 2.4.20
%define unmangled_version 2.4.20
%define release 1

Summary: Python modules for implementing LDAP clients
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: Python style
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: python-ldap project
Packager: Adam Kinney <akinney@cloudbolt.io>
Provides: python-ldap
Requires: python libldap-2_4
Url: http://www.python-ldap.org/
Distribution: openSUSE 11.x
BuildRequires: cb-python
AutoReq: 0

%description
python-ldap:
  python-ldap provides an object-oriented API to access LDAP directory servers
  from Python programs. Mainly it wraps the OpenLDAP 2.x libs for that purpose.
  Additionally the package contains modules for other LDAP-related stuff
  (e.g. processing LDIF, LDAPURLs, LDAPv3 schema, LDAPv3 extended operations
  and controls, etc.). 
  

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
%doc CHANGES README INSTALL TODO Demo/
