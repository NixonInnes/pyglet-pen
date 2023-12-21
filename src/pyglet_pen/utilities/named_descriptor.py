

class NamedDescriptor:
    def __set_name__(self, owner, name):
        self.__name = name
        #owner.__dict__.setdefault("__named_descriptors__", []).append(name)
    
    @property
    def name(self):
        return self.__name


class NamedDescriptorMeta(type):
    def __new__(cls, name, bases, cls_dict):
        cls_dict["__named_descriptors__"] = []
        for base in bases:
            if hasattr(base, "__named_descriptors__"):
                cls_dict["__named_descriptors__"].extend(base.__named_descriptors__)
        for attr, attr_value in cls_dict.items():
            if isinstance(attr_value, NamedDescriptor):
                attr_value.__set_name__(cls, attr)
                cls_dict["__named_descriptors__"].append(attr)
        return super().__new__(cls, name, bases, cls_dict)