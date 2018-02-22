from pylovepdf.task import Task


class Compress(Task):

    def __init__(self, public_key, verify_ssl):

        self.tool = 'compress'
        self.compression_level = 'recommended'

        super(Compress, self).__init__(public_key, True, verify_ssl)

    @property
    def allowed_properties(self):

        return 'compression_level',

    @property
    def compression_level_values(self):
        return 'low', 'extreme', 'recommended'

    def process(self):

        payload = super(Compress, self).process()
        payload = self.as_dict(payload, self.allowed_properties)

        return payload




