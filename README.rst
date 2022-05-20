django-sendmail-backend
=======================

A simple Django email backend, which uses an installed ``sendmail``-like command to
dispatch mail.

Based on https://github.com/perenecabuto/django-sendmail-backend.

Features
--------

Compared to the default SMTP backend, ``django-sendmail-backend``:

- Lets Django get on with other things (rather than waiting for emails to be delivered).

- Integrates better with other system / OS notifications (e.g. error messages from cron.)

- Is easier to debug. (Django may fail silently while sending mail, whereas your
  local mailserver will at least write to a log.)

Usage
-----

To use this backend:

1. Install a local mailserver with a ``sendmail``-like command.
   For example ``msmtp``, ``postfix``, ``DragonFly Mail Agent``, or ``exim``.
   Configure the mailserver to send mail to your host (the one from the
   `EMAIL_HOST <https://docs.djangoproject.com/en/dev/ref/settings/#email-host>`_ setting).


2. Install ``django-sendmail-backend`` from pip.

.. code-block:: bash

  $ pip install django-sendmail-backend

Make sure to use ``django-sendmail-backend`` and not ``django_sendmail_backend``.


3. Add the following to your Django ``settings.py``

.. code-block:: python

    # settings.py
    EMAIL_BACKEND = "sendmail.SendMailBackend"
    
    # replace with the path to your ``sendmail``-like command
    SENDMAIL_COMMAND = "/usr/sbin/sendmail"

That's all!

License
-------

Copyright (c) 2022 Christopher McDonald

Distributed under the terms of the
`MIT <https://github.com/chris-mcdo/django-sendmail-backend/blob/main/LICENSE>`_
license.
