"""Email backend which calls sendmail (or another mail command)."""
import subprocess
from typing import Iterable

import sysexits
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail.backends.base import BaseEmailBackend


class SendMailBackend(BaseEmailBackend):
    """Backend which sends mail via the "sendmail" command."""

    def send_messages(self, email_messages: Iterable[EmailMessage]):
        """Send multiple emails.

        Parameters
        ----------
        email_messages
            The EmailMessage objects to send.

        Returns
        -------
        The number of email messages sent.
        """
        sent_count = 0
        for message in email_messages:
            if self.send_message(message):
                sent_count += 1

        return sent_count

    def send_message(self, email_message: EmailMessage):
        """Send a single email.

        Parameters
        ----------
        email_message
            The EmailMessage object to send.
        
        Returns
        -------
        True if the email was successfully sent, otherwise False.
        """
        # Collect recipients
        recipients = email_message.recipients()
        if not recipients:
            return False

        # Collect message
        message_bytes = email_message.message().as_bytes()

        # Pick sendmail command to use
        sendmail_command = getattr(settings, "SENDMAIL_COMMAND", "/usr/sbin/sendmail")

        # Attempt mail send
        process = subprocess.run(
            [sendmail_command] + recipients, input=message_bytes, stderr=subprocess.PIPE
        )

        try:
            sysexits.raise_for_returncode(process)
        except subprocess.SubprocessError:
            if self.fail_silently:
                return False
            else:
                raise

        return True
