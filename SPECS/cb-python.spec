%global _python_bytecompile_errors_terminate_build 0
%global __debug_package 1
%define __prefix /opt/cb

Summary: An interpreted, interactive, object-oriented programming language.
Name: cb-python
Version: 2.7.12
Release: 1
License: PSF
Group: Development/Languages
Source: Python-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Prefix: %{__prefix}
Packager: Adam Kinney <akinney@cloudbolt.io>
AutoReq: no
AutoReqProv: no

%description
Python is an interpreted, interactive, object-oriented programming
language.  It incorporates modules, exceptions, dynamic typing, very high
level dynamic data types, and classes. Python combines remarkable power
with very clear syntax. It has interfaces to many system calls and
libraries, as well as to various window systems, and is extensible in C or
C++. It is also usable as an extension language for applications that need
a programmable interface.  Finally, Python is portable: it runs on many
brands of UNIX, on PCs under Windows, MS-DOS, and OS/2, and on the
Mac.

#######
#  PREP
#######
%prep
%setup -n Python-%{version}
# %setup -q

########
#  BUILD
########
%build
./configure \
  --prefix=%{__prefix} \
  --enable-shared \
  --with-threads \
  --with-ensurepip=install
make
# make %{_smp_mflags}

##########
#  INSTALL
##########
%install
make DESTDIR=%{buildroot} install

########
#  CLEAN
########
%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

########
#  FILES
########
%files
%{__prefix}

%changelog
* Mon Dec 20 2004 Sean Reifschneider <jafo-rpms@tummy.com> [2.4-2pydotorg]
- Changing the idle wrapper so that it passes arguments to idle.

