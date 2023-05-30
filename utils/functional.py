def get_constant_attributes_from_class(class_name):
    attributes = list(class_name.__dict__.keys())
    return list(filter(lambda x: x.isupper(), attributes))
