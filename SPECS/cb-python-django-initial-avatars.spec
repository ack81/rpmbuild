%global _python_bytecompile_errors_terminate_build 0
%define debug_package %{nil}
%define __name django-initial-avatars
%define version 0.8.1
%define unmangled_version 0.8.1
%define unmangled_version 0.8.1
%define release 1

Summary: A simple Django app to get avatars based on username and initials if no gravatars is associated with the email address.
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: BSD License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Mathieu Requillart <mrequillart@axiome.io>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://github.com/axiome-oss/django-initial-avatars
BuildRequires: cb-python
AutoReq: 0

%description
django-initial-avatars

======================

.. image:: https://badge.fury.io/py/django-initial-avatars.svg  
    :target: https://badge.fury.io/py/django-initial-avatars
.. image:: https://travis-ci.org/axiome-oss/django-initial-avatars.svg?branch=master
    :target: https://travis-ci.org/axiome-oss/django-initial-avatars

django-initial-avatars is a simple Django app which generates avatars based on username and initials. If django_gravatar is installed, user's gravatar is preferred.

Examples
-----------

* API endpoint

.. image:: https://metod-site.s3.amazonaws.com/media/25/initial_avatars.png
    :target: http://www.metod.io/fr/blog/2015/12/02/release-django-initial-avatars/
    :alt: example of django-initial-avatars on Metod
    
* Template tag

.. image:: https://metod-site.s3.amazonaws.com/media/25/initial_avatars_email.png
    :target: http://www.metod.io/fr/blog/2015/12/02/release-django-initial-avatars/
    :alt: example of django-initial-avatars in Metod emails

Dependencies
------------

Generating avatars requires a `Pillow` installation with `freetype` support.

``freetype`` can easily be installed on ubuntu with::
	
	$ sudo aptitude install libfreetype6-dev

or on OS X with `homebrew`::

    $ brew install freetype

Make sure the following packet are installed on your system to enable PNG and JPG support on Pillow::

    $ sudo aptitude install libjpeg-dev zlib1g-dev libpng12-dev

Pillow may need to be rebuilt after installing the libraries.

Font licensing
--------------

The font ``Ubuntu Monospace`` is used to generate the avatar.
The font is licensed under the Ubuntu Font Licence, see the
`License <http://font.ubuntu.com/licence/>`_

Quick start
-----------
1. install app requirements

2. install django-initial-avatars through pip::

    pip install django-initial-avatars

3. If you want to use gravatar for users who have one, install django-gravatar2::

    pip install django-gravatar2

4. Add "django-initial-avatars" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'initial_avatars',
        ['django_gravatar',]
    )

5. Include the django-initial-avatar URLconf in your project urls.py like this::

    url(r'^avatar/', include('initial_avatars.urls')),

6. Launch development server::

	python manage.py runserver

7. Each user has now an endpoint for his avatar::

	localhost:8000/avatar/user_id/[size/]

8. In your templates, use::

    {% load initialavatar %}

    {% get_initial_avatar user [size] ['shape'] %}

    {% get_initial_avatar user.email [size] ['shape'] %}


Settings
-----------

A few settings are at your disposal

* AVATAR_STORAGE_BACKEND allows you to use a custom storage backend instead of the default one::

    AVATAR_STORAGE_BACKEND = 'myproject.custom_storages.AvatarStorage'

* AVATAR_STORAGE_FOLDER allows you to customize the root folder on the storage backend, default to 'avatars'::

    AVATAR_STORAGE_FOLDER = 'myfolder'

* AVATAR_DEFAULT_SHAPE allows you to choose the default shape of the image, possible options are 'circle' or 'square', default to 'square'

  More shapes can be easily addded, just open an issue on github::

    AVATAR_DEFAULT_SHAPE = 'circle'

* GRAVATAR_DEFAULT_SIZE allows you to choose the default size of the image, setting name used for compatibility with django_gravatar, default to '80'::

    GRAVATAR_DEFAULT_SIZE = 100

Tests
--------------

Django-initial-avatars is provided with tests, they require django-gravatar2 and tox

You can launch them in the virtualenv like this::

        tox

It might happen that a calculated position fails because of a minor difference in the result, don't care about it.

Contributions
--------------

Contributions are welcome ! Feel free to write an issue for any feedback you have or send a pull request on `Github <https://github.com/axiome-oss/django-initial-avatars>`_

Used on
--------------

* `Metod <http://www.metod.io/>`_
* Add your website here !


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
