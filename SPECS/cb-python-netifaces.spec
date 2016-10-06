%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name netifaces
%define version 0.10.4
%define unmangled_version 0.10.4
%define unmangled_version 0.10.4
%define release 1

Summary: Portable network interface information.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: MIT License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Alastair Houghton <alastair@alastairs-place.net>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://bitbucket.org/al45tair/netifaces
BuildRequires: cb-python
AutoReq: 0

%description
netifaces 0.10.4
================

.. image:: https://drone.io/bitbucket.org/al45tair/netifaces/status.png
   :target: https://drone.io/bitbucket.org/al45tair/netifaces/latest
   :alt: Build Status

1. What is this?
----------------

It's been annoying me for some time that there's no easy way to get the
address(es) of the machine's network interfaces from Python.  There is
a good reason for this difficulty, which is that it is virtually impossible
to do so in a portable manner.  However, it seems to me that there should
be a package you can easy_install that will take care of working out the
details of doing so on the machine you're using, then you can get on with
writing Python code without concerning yourself with the nitty gritty of
system-dependent low-level networking APIs.

This package attempts to solve that problem.

2. How do I use it?
-------------------

First you need to install it, which you can do by typing::

  tar xvzf netifaces-0.10.4.tar.gz
  cd netifaces-0.10.4
  python setup.py install

Once that's done, you'll need to start Python and do something like the
following::

>>> import netifaces

Then if you enter

>>> netifaces.interfaces()
['lo0', 'gif0', 'stf0', 'en0', 'en1', 'fw0']

you'll see the list of interface identifiers for your machine.

You can ask for the addresses of a particular interface by doing

>>> netifaces.ifaddresses('lo0')
{18: [{'addr': ''}], 2: [{'peer': '127.0.0.1', 'netmask': '255.0.0.0', 'addr': '127.0.0.1'}], 30: [{'peer': '::1', 'netmask': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', 'addr': '::1'}, {'peer': '', 'netmask': 'ffff:ffff:ffff:ffff::', 'addr': 'fe80::1%lo0'}]}

Hmmmm.  That result looks a bit cryptic; let's break it apart and explain
what each piece means.  It returned a dictionary, so let's look there first::

  { 18: [...], 2: [...], 30: [...] }

Each of the numbers refers to a particular address family.  In this case, we
have three address families listed; on my system, 18 is ``AF_LINK`` (which means
the link layer interface, e.g. Ethernet), 2 is ``AF_INET`` (normal Internet
addresses), and 30 is ``AF_INET6`` (IPv6).

But wait!  Don't use these numbers in your code.  The numeric values here are
system dependent; fortunately, I thought of that when writing netifaces, so
the module declares a range of values that you might need.  e.g.

>>> netifaces.AF_LINK
18

Again, on your system, the number may be different.

So, what we've established is that the dictionary that's returned has one
entry for each address family for which this interface has an address.  Let's
take a look at the ``AF_INET`` addresses now:

>>> addrs = netifaces.ifaddresses('lo0')
>>> addrs[netifaces.AF_INET]
[{'peer': '127.0.0.1', 'netmask': '255.0.0.0', 'addr': '127.0.0.1'}]

You might be wondering why this value is a list.  The reason is that it's
possible for an interface to have more than one address, even within the
same family.  I'll say that again: *you can have more than one address of
the same type associated with each interface*.

*Asking for "the" address of a particular interface doesn't make sense.*

Right, so, we can see that this particular interface only has one address,
and, because it's a loopback interface, it's point-to-point and therefore
has a *peer* address rather than a broadcast address.

Let's look at a more interesting interface.

>>> addrs = netifaces.ifaddresses('en0')
>>> addrs[netifaces.AF_INET]
[{'broadcast': '10.15.255.255', 'netmask': '255.240.0.0', 'addr': '10.0.1.4'}, {'broadcast': '192.168.0.255', 'addr': '192.168.0.47'}]

This interface has two addresses (see, I told you...)  Both of them are
regular IPv4 addresses, although in one case the netmask has been changed
from its default.  The netmask *may not* appear on your system if it's set
to the default for the address range.

Because this interface isn't point-to-point, it also has broadcast addresses.

Now, say we want, instead of the IP addresses, to get the MAC address; that
is, the hardware address of the Ethernet adapter running this interface.  We
can do

>>> addrs[netifaces.AF_LINK]
[{'addr': '00:12:34:56:78:9a'}]

Note that this may not be available on platforms without getifaddrs(), unless
they happen to implement ``SIOCGIFHWADDR``.  Note also that you just get the
address; it's unlikely that you'll see anything else with an ``AF_LINK`` address.
Oh, and don't assume that all ``AF_LINK`` addresses are Ethernet; you might, for
instance, be on a Mac, in which case:

>>> addrs = netifaces.ifaddresses('fw0')
>>> addrs[netifaces.AF_LINK]
[{'addr': '00:12:34:56:78:9a:bc:de'}]

No, that isn't an exceptionally long Ethernet MAC address---it's a FireWire
address.

As of version 0.10.0, you can also obtain a list of gateways on your
machine:

>>> netifaces.gateways()
{2: [('10.0.1.1', 'en0', True), ('10.2.1.1', 'en1', False)], 30: [('fe80::1', 'en0', True)], 'default': { 2: ('10.0.1.1', 'en0'), 30: ('fe80::1', 'en0') }}

This dictionary is keyed on address family---in this case, ``AF_INET``---and
each entry is a list of gateways as ``(address, interface, is_default)`` tuples.
Notice that here we have two separate gateways for IPv4 (``AF_INET``); some
operating systems support configurations like this and can either route packets
based on their source, or based on administratively configured routing tables.

For convenience, we also allow you to index the dictionary with the special
value ``'default'``, which returns a dictionary mapping address families to the
default gateway in each case.  Thus you can get the default IPv4 gateway with

>>> gws = netifaces.gateways()
>>> gws['default'][netifaces.AF_INET]
('10.0.1.1', 'en0')

Do note that there may be no default gateway for any given address family;
this is currently very common for IPv6 and much less common for IPv4 but it
can happen even for ``AF_INET``.

BTW, if you're trying to configure your machine to have multiple gateways for
the same address family, it's a very good idea to check the documentation for
your operating system *very* carefully, as some systems become extremely
confused or route packets in a non-obvious manner.

I'm very interested in hearing from anyone (on any platform) for whom the
``gateways()`` method doesn't produce the expected results.  It's quite
complicated extracting this information from the operating system (whichever
operating system we're talking about), and so I expect there's at least one
system out there where this just won't work.

3. This is great!  What platforms does it work on?
--------------------------------------------------

It gets regular testing on OS X, Linux and Windows.  It has also been used
successfully on Solaris, and it's expected to work properly on other UNIX-like
systems as well.  If you are running something that is not supported, and
wish to contribute a patch, please use BitBucket to send a pull request.

4. What license is this under?
------------------------------

It's an MIT-style license.  Here goes:

Copyright (c) 2007-2014 Alastair Houghton

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

5. Why the jump to 0.10.0?
--------------------------

Because someone released a fork of netifaces with the version 0.9.0.
Hopefully skipping the version number should remove any confusion.  In 
addition starting with 0.10.0 Python 3 is now supported and other 
features/bugfixes have been included as well.  See the CHANGELOG for a
more complete list of changes.


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
