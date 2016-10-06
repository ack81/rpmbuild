%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name flake8
%define version 2.5.4
%define unmangled_version 2.5.4
%define unmangled_version 2.5.4
%define release 1

Summary: the modular source code checker: pep8, pyflakes and co
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ian Cordasco <graffatcolmingov@gmail.com>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://gitlab.com/pycqa/flake8
BuildRequires: cb-python
AutoReq: 0

%description
======
Flake8
======

Flake8 is a wrapper around these tools:

- PyFlakes
- pep8
- Ned Batchelder's McCabe script

Flake8 runs all the tools by launching the single ``flake8`` script.
It displays the warnings in a per-file, merged output.

It also adds a few features:

- files that contain this line are skipped::

    # flake8: noqa

- lines that contain a ``# noqa`` comment at the end will not issue warnings.
- a Git and a Mercurial hook.
- a McCabe complexity checker.
- extendable through ``flake8.extension`` entry points.


QuickStart
==========

::

    pip install flake8

To run flake8 just invoke it against any directory or Python module::

    $ flake8 coolproject
    coolproject/mod.py:97:1: F401 'shutil' imported but unused
    coolproject/mod.py:625:17: E225 missing whitespace around operato
    coolproject/mod.py:729:1: F811 redefinition of function 'readlines' from line 723
    coolproject/mod.py:1028:1: F841 local variable 'errors' is assigned to but never used

The outputs of PyFlakes *and* pep8 (and the optional plugins) are merged
and returned.

flake8 offers an extra option: --max-complexity, which will emit a warning if
the McCabe complexity of a function is higher than the value.  By default it's
deactivated::

    $ flake8 --max-complexity 12 coolproject
    coolproject/mod.py:97:1: F401 'shutil' imported but unused
    coolproject/mod.py:625:17: E225 missing whitespace around operator
    coolproject/mod.py:729:1: F811 redefinition of unused 'readlines' from line 723
    coolproject/mod.py:939:1: C901 'Checker.check_all' is too complex (12)
    coolproject/mod.py:1028:1: F841 local variable 'errors' is assigned to but never used
    coolproject/mod.py:1204:1: C901 'selftest' is too complex (14)

This feature is quite useful to detect over-complex code.  According to McCabe,
anything that goes beyond 10 is too complex.
See https://en.wikipedia.org/wiki/Cyclomatic_complexity.


Frequently Asked Questions
==========================

Why does flake8 pin the version of pep8?
----------------------------------------

Version 1.6 of pep8 doesn't work properly with flake8.  Until pep8 releases a
version that works, flake8 pins the version of pep8 so that flake8 will work as
a whole.

Is flake8 broken?
-----------------

Flake8 combines two other projects that are significant on their own: pep8 and
PyFlakes. If flake8 is doing something you don't like, it is quite likely that
the problem lies in one of those other projects.  You can run them separately
to see if they are the cause of your difficulties.  We greatly appreciate your
efforts to diagnose the source of the problem before reporting bugs against
flake8.


Questions or Feedback
=====================

If you have questions you'd like to ask the developers, or feedback you'd like
to provide, feel free to use the mailing list: code-quality@python.org We
would love to hear from you. Additionally, if you have a feature you'd like to
suggest, the mailing list would be the best place for it.

.. _links:

Links
=====

* `flake8 documentation <http://flake8.readthedocs.org/en/latest/>`_

* `pep8 documentation <http://pep8.readthedocs.org/en/latest/>`_


CHANGES
=======

2.5.4 - 2016-02-11
------------------

- **Bug** Missed an attribute rename during the v2.5.3 release.

2.5.3 - 2016-02-11
------------------

- **Bug** Actually parse ``output_file`` and ``enable_extensions`` from config
  files

2.5.2 - 2016-01-30
------------------

- **Bug** Parse ``output_file`` and ``enable_extensions`` from config files

- **Improvement** Raise upper bound on mccabe plugin to allow for version
  0.4.0

2.5.1 - 2015-12-08
------------------

- **Bug** Properly look for ``.flake8`` in current working directory
  (`GitLab#103`_)

- **Bug** Monkey-patch ``pep8.stdin_get_value`` to cache the actual value in
  stdin. This helps plugins relying on the function when run with
  multiprocessing. (`GitLab#105`_, `GitLab#107`_)

.. _GitLab#103: https://gitlab.com/pycqa/flake8/issues/103
.. _GitLab#105: https://gitlab.com/pycqa/flake8/issues/105
.. _GitLab#107: https://gitlab.com/pycqa/flake8/issues/107

2.5.0 - 2015-10-26
------------------

- **Improvement** Raise cap on PyFlakes for Python 3.5 support

- **Improvement** Avoid deprecation warnings when loading extensions
  (`GitLab#59`_, `GitLab#90`_)

- **Improvement** Separate logic to enable "off-by-default" extensions
  (`GitLab#67`_)

- **Bug** Properly parse options to setuptools Flake8 command (`GitLab!41`_)

- **Bug** Fix exceptions when output on stdout is truncated before Flake8
  finishes writing the output (`GitLab#69`_)

- **Bug** Fix error on OS X where Flake8 can no longer acquire or create new
  semaphores (`GitLab#74`_)

.. _GitLab!41: https://gitlab.com/pycqa/flake8/merge_requests/41
.. _GitLab#59: https://gitlab.com/pycqa/flake8/issues/59
.. _GitLab#67: https://gitlab.com/pycqa/flake8/issues/67
.. _GitLab#69: https://gitlab.com/pycqa/flake8/issues/69
.. _GitLab#74: https://gitlab.com/pycqa/flake8/issues/74
.. _GitLab#90: https://gitlab.com/pycqa/flake8/issues/90

2.4.1 - 2015-05-18
------------------

- **Bug** Do not raise a ``SystemError`` unless there were errors in the
  setuptools command. (`GitLab#39`_, `GitLab!23`_)

- **Bug** Do not verify dependencies of extensions loaded via entry-points.

- **Improvement** Blacklist versions of pep8 we know are broken

.. _GitLab#39: https://gitlab.com/pycqa/flake8/issues/39
.. _GitLab!23: https://gitlab.com/pycqa/flake8/merge_requests/23

2.4.0 - 2015-03-07
------------------

- **Bug** Print filenames when using multiprocessing and ``-q`` option.
  (`GitLab#31`_)

- **Bug** Put upper cap on dependencies. The caps for 2.4.0 are:

  - ``pep8 < 1.6`` (Related to `GitLab#35`_)

  - ``mccabe < 0.4``

  - ``pyflakes < 0.9``

  See also `GitLab#32`_

- **Bug** Files excluded in a config file were not being excluded when flake8
  was run from a git hook. (`GitHub#2`_)

- **Improvement** Print warnings for users who are providing mutually
  exclusive options to flake8. (`GitLab#8`_, `GitLab!18`_)

- **Feature** Allow git hook configuration to live in ``.git/config``.
  See the updated `VCS hooks docs`_ for more details. (`GitLab!20`_)

.. _GitHub#2: https://github.com/pycqa/flake8/pull/2
.. _GitLab#8: https://gitlab.com/pycqa/flake8/issues/8
.. _GitLab#31: https://gitlab.com/pycqa/flake8/issues/31
.. _GitLab#32: https://gitlab.com/pycqa/flake8/issues/32
.. _GitLab#35: https://gitlab.com/pycqa/flake8/issues/35
.. _GitLab!18: https://gitlab.com/pycqa/flake8/merge_requests/18
.. _GitLab!20: https://gitlab.com/pycqa/flake8/merge_requests/20
.. _VCS hooks docs: https://flake8.readthedocs.org/en/latest/vcs.html

2.3.0 - 2015-01-04
------------------

- **Feature**: Add ``--output-file`` option to specify a file to write to
  instead of ``stdout``.

- **Bug** Fix interleaving of output while using multiprocessing
  (`GitLab#17`_)

.. _GitLab#17: https://gitlab.com/pycqa/flake8/issues/17

2.2.5 - 2014-10-19
------------------

- Flush standard out when using multiprocessing

- Make the check for "# flake8: noqa" more strict

2.2.4 - 2014-10-09
------------------

- Fix bugs triggered by turning multiprocessing on by default (again)

  Multiprocessing is forcibly disabled in the following cases:

  - Passing something in via stdin

  - Analyzing a diff

  - Using windows

- Fix --install-hook when there are no config files present for pep8 or
  flake8.

- Fix how the setuptools command parses excludes in config files

- Fix how the git hook determines which files to analyze (Thanks Chris
  Buccella!)

2.2.3 - 2014-08-25
------------------

- Actually turn multiprocessing on by default

2.2.2 - 2014-07-04
------------------

- Re-enable multiprocessing by default while fixing the issue Windows users
  were seeing.

2.2.1 - 2014-06-30
------------------

- Turn off multiple jobs by default. To enable automatic use of all CPUs, use
  ``--jobs=auto``. Fixes #155 and #154.

2.2.0 - 2014-06-22
------------------

- New option ``doctests`` to run Pyflakes checks on doctests too
- New option ``jobs`` to launch multiple jobs in parallel
- Turn on using multiple jobs by default using the CPU count
- Add support for ``python -m flake8`` on Python 2.7 and Python 3
- Fix Git and Mercurial hooks: issues #88, #133, #148 and #149
- Fix crashes with Python 3.4 by upgrading dependencies
- Fix traceback when running tests with Python 2.6
- Fix the setuptools command ``python setup.py flake8`` to read
  the project configuration


2.1.0 - 2013-10-26
------------------

- Add FLAKE8_LAZY and FLAKE8_IGNORE environment variable support to git and
  mercurial hooks
- Force git and mercurial hooks to repsect configuration in setup.cfg
- Only check staged files if that is specified
- Fix hook file permissions
- Fix the git hook on python 3
- Ignore non-python files when running the git hook
- Ignore .tox directories by default
- Flake8 now reports the column number for PyFlakes messages


2.0.0 - 2013-02-23
------------------

- Pyflakes errors are prefixed by an ``F`` instead of an ``E``
- McCabe complexity warnings are prefixed by a ``C`` instead of a ``W``
- Flake8 supports extensions through entry points
- Due to the above support, we **require** setuptools
- We publish the `documentation <https://flake8.readthedocs.org/>`_
- Fixes #13: pep8, pyflakes and mccabe become external dependencies
- Split run.py into main.py, engine.py and hooks.py for better logic
- Expose our parser for our users
- New feature: Install git and hg hooks automagically
- By relying on pyflakes (0.6.1), we also fixed #45 and #35


1.7.0 - 2012-12-21
------------------

- Fixes part of #35: Exception for no WITHITEM being an attribute of Checker
  for Python 3.3
- Support stdin
- Incorporate @phd's builtins pull request
- Fix the git hook
- Update pep8.py to the latest version


1.6.2 - 2012-11-25
------------------

- fixed the NameError: global name 'message' is not defined (#46)


1.6.1 - 2012-11-24
------------------

- fixed the mercurial hook, a change from a previous patch was not properly
  applied
- fixed an assumption about warnings/error messages that caused an exception
  to be thrown when McCabe is used


1.6 - 2012-11-16
----------------

- changed the signatures of the ``check_file`` function in flake8/run.py,
  ``skip_warning`` in flake8/util.py and the ``check``, ``checkPath``
  functions in flake8/pyflakes.py.
- fix ``--exclude`` and ``--ignore`` command flags (#14, #19)
- fix the git hook that wasn't catching files not already added to the index
  (#29)
- pre-emptively includes the addition to pep8 to ignore certain lines.
  Add ``# nopep8`` to the end of a line to ignore it. (#37)
- ``check_file`` can now be used without any special prior setup (#21)
- unpacking exceptions will no longer cause an exception (#20)
- fixed crash on non-existent file (#38)


1.5 - 2012-10-13
----------------

- fixed the stdin
- make sure mccabe catches the syntax errors as warnings
- pep8 upgrade
- added max_line_length default value
- added Flake8Command and entry points if setuptools is around
- using the setuptools console wrapper when available


1.4 - 2012-07-12
----------------

- git_hook: Only check staged changes for compliance
- use pep8 1.2


1.3.1 - 2012-05-19
------------------

- fixed support for Python 2.5


1.3 - 2012-03-12
----------------

- fixed false W402 warning on exception blocks.


1.2 - 2012-02-12
----------------

- added a git hook
- now Python 3 compatible
- mccabe and pyflakes have warning codes like pep8 now


1.1 - 2012-02-14
----------------

- fixed the value returned by --version
- allow the flake8: header to be more generic
- fixed the "hg hook raises 'physical lines'" bug
- allow three argument form of raise
- now uses setuptools if available, for 'develop' command


1.0 - 2011-11-29
----------------

- Deactivates by default the complexity checker
- Introduces the complexity option in the HG hook and the command line.


0.9 - 2011-11-09
----------------

- update pep8 version to 0.6.1
- mccabe check: gracefully handle compile failure


0.8 - 2011-02-27
----------------

- fixed hg hook
- discard unexisting files on hook check


0.7 - 2010-02-18
----------------

- Fix pep8 initialization when run through Hg
- Make pep8 short options work when run through the command line
- Skip duplicates when controlling files via Hg


0.6 - 2010-02-15
----------------

- Fix the McCabe metric on some loops


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
