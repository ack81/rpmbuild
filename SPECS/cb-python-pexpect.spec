%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name pexpect
%define version 3.3
%define unmangled_version 3.3
%define release 1

Summary: Pexpect allows easy control of interactive console applications.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: ISC license
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Noah Spurrier; Thomas Kluyver; Jeff Quast <noah@noah.org; thomas@kluyver.me.uk; contact@jeffquast.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://pexpect.readthedocs.org/
BuildRequires: cb-python
AutoReq: 0

%description

Pexpect is a pure Python module for spawning child applications; controlling
them; and responding to expected patterns in their output. Pexpect works like
Don Libes' Expect. Pexpect allows your script to spawn a child application and
control it as if a human were typing commands.

Pexpect can be used for automating interactive applications such as ssh, ftp,
passwd, telnet, etc. It can be used to a automate setup scripts for duplicating
software package installations on different servers. It can be used for
automated software testing. Pexpect is in the spirit of Don Libes' Expect, but
Pexpect is pure Python. Unlike other Expect-like modules for Python, Pexpect
does not require TCL or Expect nor does it require C extensions to be compiled.
It should work on any platform that supports the standard Python pty module.
The Pexpect interface was designed to be easy to use.


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
