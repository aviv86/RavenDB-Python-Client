class DocumentConvention(object):
    def __init__(self):
        self.max_number_of_request_per_session = 30
        self.max_ids_to_catch = 32

    @staticmethod
    def default_transform_type_tag_name(name):
        count = sum(1 for c in name if c.isupper())
        if count <= 1:
            return name.lower() + 's'
        return name + 's'

    @staticmethod
    def build_default_metadata(entity):
        return {"Raven-Entity-Name": str(entity.__class__.__name__ + 's'), "Raven-Python-Type": str(entity.__class__)}
