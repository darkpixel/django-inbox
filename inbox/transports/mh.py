from mailbox import MH
from inbox.transports.generic import GenericFileMailbox


class MHTransport(GenericFileMailbox):
    _variant = MH
