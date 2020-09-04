import jsonpickle

import symphony.rest.endpoints as sym_ep
import symphony.utility as sym_util

from symphony.api_base import APIBase
from models.messaging import MessageAttachment

class Messaging(APIBase):
    def __init__(self, session):
        super().__init__(session)

    def send_housekeeper_report(self, stream_id: str, message: str, attachment: MessageAttachment=None):
        body_list = [('message', sym_util.format_symphony_message(message))]

        if attachment:
            att = (attachment.filename, attachment.data, attachment.mime_type)
            body_list.append(('attachment', att))


        ep = self.get_endpoint(sym_ep.send_message(stream_id))
        self.rest_callout(method='postv2', endpoint=ep, body_object=body_list)



