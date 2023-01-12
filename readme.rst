Forked from https://github.com/coddingtonbear/django-mailbox due to the project appearing to be dead and renamed to ```django-inbox``` so
it can eventually be published on pypi without a name collision.

Include ```inbox``` in your INSTALLED_APPS.

Lots of things are wildly out-of-date (like tests and docs), but it works for me.

The original docs are still accurate other than being renamed to ```django-inbox``` and the INSTALLED_APPS name is ```inbox```.

Easily ingest messages from POP3, IMAP, or local mailboxes into your Django application.

This app allows you to either ingest e-mail content from common e-mail services (as long as the service provides POP3 or IMAP support),
or directly receive e-mail messages from ``stdin`` (for locally processing messages from Postfix or Exim4).

These ingested messages will be stored in the database in Django models and you can process their content at will,
or -- if you're in a hurry -- by using a signal receiver.

- Documentation for django-mailbox is available on
  `ReadTheDocs <http://django-mailbox.readthedocs.org/>`_.
- Please post issues on
  `Github <http://github.com/coddingtonbear/django-mailbox/issues>`_.
- Test status available under actions tab
  `Actions <https://github.com/coddingtonbear/django-mailbox/actions>`_.


.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/coddingtonbear/django-mailbox
   :target: https://gitter.im/coddingtonbear/django-mailbox?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
