# raven-dj
An Online invoicing system prototype made with django.

Current Version:	raven 1.0
Tested:				No

Functionalities:

--Add Invoices
--Move Invoices to trash
--Delete Invoices
--Sent Invoices to recipients via emails

Note:

For development purposed, 'django.core.mail.backends.console.EmailBackend' is used as the email backend so mails sent through the app won't be actually delivered to the recipients, but it will be shown in the console running the server program.
