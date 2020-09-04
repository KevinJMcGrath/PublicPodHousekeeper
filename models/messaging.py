class MessageAttachment:
    def __init__(self, name: str, mime_type, data):
        self.filename = name
        self.mime_type = mime_type
        self.data = data