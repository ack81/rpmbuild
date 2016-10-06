%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name ipython
%define version 4.0.0
%define unmangled_version 4.0.0
%define unmangled_version 4.0.0
%define release 1

Summary: IPython: Productive Interactive Computing
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: The IPython Development Team <ipython-dev@scipy.org>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://ipython.org
BuildRequires: cb-python
AutoReq: 0

%description

IPython provides a rich toolkit to help you make the most out of using Python
interactively.  Its main components are:

* A powerful interactive Python shell
* A `Jupyter <http://jupyter.org/>`_ kernel to work with Python code in Jupyter
  notebooks and other interactive frontends.

The enhanced interactive Python shells have the following main features:

* Comprehensive object introspection.

* Input history, persistent across sessions.

* Caching of output results during a session with automatically generated
  references.

* Extensible tab completion, with support by default for completion of python
  variables and keywords, filenames and function keywords.

* Extensible system of 'magic' commands for controlling the environment and
  performing many tasks related either to IPython or the operating system.

* A rich configuration system with easy switching between different setups
  (simpler than changing $PYTHONSTARTUP environment variables every time).

* Session logging and reloading.

* Extensible syntax processing for special purpose situations.

* Access to the system shell with user-extensible alias system.

* Easily embeddable in other Python programs and GUIs.

* Integrated access to the pdb debugger and the Python profiler.

The latest development version is always available from IPython's `GitHub
site <http://github.com/ipython>`_.


%prep
%setup -n %{__name}-%{unmangled_version} -n %{__name}-%{unmangled_version}

%build
/opt/cb/bin/python setup.py build

%install
/opt/cb/bin/python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
