%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name Django
%define version 1.7.11
%define unmangled_version 1.7.11
%define unmangled_version 1.7.11
%define release 1

Summary: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Django Software Foundation <foundation@djangoproject.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: http://www.djangoproject.com/
BuildRequires: cb-python
AutoReq: 0

%description
UNKNOWN

%prep
%setup -n %{__name}-%{unmangled_version} -n %{__name}-%{unmangled_version}

%build
/opt/cb/bin/python setup.py build

%install
#! /bin/sh
#
# This file becomes the install section of the generated spec file.
#

# This is what dist.py normally does.
/opt/cb/bin/python setup.py install --single-version-externally-managed --root=${RPM_BUILD_ROOT} --record="INSTALLED_FILES"

# Sort the filelist so that directories appear before files. This avoids
# duplicate filename problems on some systems.
touch DIRS
for i in `cat INSTALLED_FILES`; do
  if [ -f ${RPM_BUILD_ROOT}/$i ]; then
    echo $i >>FILES
  fi
  if [ -d ${RPM_BUILD_ROOT}/$i ]; then
    echo %dir $i >>DIRS
  fi
done

# Make sure we match foo.pyo and foo.pyc along with foo.py (but only once each)
sed -e "/\.py[co]$/d" -e "s/\.py$/.py*/" DIRS FILES >INSTALLED_FILES

mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man1/
cp docs/man/* ${RPM_BUILD_ROOT}/%{_mandir}/man1/
cat << EOF >> INSTALLED_FILES
%doc %{_mandir}/man1/*"
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc docs extras AUTHORS INSTALL LICENSE README.rst
