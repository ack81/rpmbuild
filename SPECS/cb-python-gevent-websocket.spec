%global _python_bytecompile_errors_terminate_build 1
%define debug_package %{nil}
%define __name gevent-websocket
%define version 0.9.5
%define unmangled_version 0.9.5
%define unmangled_version 0.9.5
%define release 1

Summary: Websocket handler for the gevent pywsgi server, a Python network library
Name: cb-python-%{__name}
Version: %{version}
Release: %{release}
Source0: %{__name}-%{unmangled_version}.tar.gz
License: Copyright 2011-2013 Jeffrey Gelens <jeffrey@noppo.pro>
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{__name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jeffrey Gelens <jeffrey@noppo.pro>
Packager: Adam Kinney <akinney@cloudbolt.io>
Url: https://bitbucket.org/Jeffrey/gevent-websocket
BuildRequires: cb-python
AutoReq: 0

%description
================
gevent-websocket
================

`gevent-websocket`_ is a WebSocket library for the gevent_ networking library.

Features include:

- Integration on both socket level or using an abstract interface.
- RPC and PubSub framework using `WAMP`_ (WebSocket Application
  Messaging Protocol).
- Easily extendible using a simple WebSocket protocol plugin API


::

    from geventwebsocket import WebSocketServer, WebSocketApplication, Resource

    class EchoApplication(WebSocketApplication):
        def on_open(self):
            print "Connection opened"

        def on_message(self, message):
            self.ws.send(message)

        def on_close(self, reason):
            print reason

    WebSocketServer(
        ('', 8000),
        Resource({'/': EchoApplication})
    ).serve_forever()

or a low level implementation::

    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    def websocket_app(environ, start_response):
        if environ["PATH_INFO"] == '/echo':
            ws = environ["wsgi.websocket"]
            message = ws.receive()
            ws.send(message)

    server = pywsgi.WSGIServer(("", 8000), websocket_app,
        handler_class=WebSocketHandler)
    server.serve_forever()

More examples can be found in the ``examples`` directory. Hopefully more
documentation will be available soon.

Installation
------------

The easiest way to install gevent-websocket is directly from PyPi_ using pip or
setuptools by running the commands below::

    $ pip install gevent-websocket


Gunicorn Worker
^^^^^^^^^^^^^^^

Using Gunicorn it is even more easy to start a server. Only the
`websocket_app` from the previous example is required to start the server.
Start Gunicorn using the following command and worker class to enable WebSocket
funtionality for the application.

::

    gunicorn -k "geventwebsocket.gunicorn.workers.GeventWebSocketWorker" wsgi:websocket_app

Performance
^^^^^^^^^^^

`gevent-websocket`_ is pretty fast, but can be accelerated further by
installing `wsaccel <https://github.com/methane/wsaccel>`_ and `ujson` or `simplejson`::

    $ pip install wsaccel ujson

`gevent-websocket`_ automatically detects ``wsaccell`` and uses the Cython
implementation for UTF8 validation and later also frame masking and
demasking.

Get in touch
^^^^^^^^^^^^

Get in touch on IRC #gevent on Freenode or on the Gevent `mailinglist
<https://groups.google.com/forum/#!forum/gevent>`_. Issues can be created
on `Bitbucket <https://bitbucket.org/Jeffrey/gevent-websocket/issues?status=new&status=open>`_.

.. _WAMP: http://www.wamp.ws
.. _gevent-websocket: http://www.bitbucket.org/Jeffrey/gevent-websocket/
.. _gevent: http://www.gevent.org/
.. _Jeffrey Gelens: http://www.gelens.org/
.. _PyPi: http://pypi.python.org/pypi/gevent-websocket/
.. _repository: http://www.bitbucket.org/Jeffrey/gevent-websocket/
.. _RFC6455: http://datatracker.ietf.org/doc/rfc6455/?include_text=1


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
