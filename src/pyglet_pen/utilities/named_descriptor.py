

class NamedDescriptor:
    def __set_name__(self, owner, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name


class NamedDescriptorMeta(type):
    __name_container__ = "__named_descriptors__"
    def __new__(cls, name, bases, cls_dict):
        cls_dict[cls.__name_container__] = []
        for base in bases:
            if base_name_container:=getattr(base, cls.__name_container__):
                cls_dict[cls.__name_container__].extend(base_name_container)
        for attr, attr_value in cls_dict.items():
            if isinstance(attr_value, NamedDescriptor):
                attr_value.__set_name__(cls, attr)
                cls_dict[cls.__name_container__].append(attr)
        return super().__new__(cls, name, bases, cls_dict)
    

class NamedPropertyDescriptor(NamedDescriptor):
    pass

class NamedPropertyDescriptorMeta(NamedDescriptorMeta):
    __name_container__ = "__named_property__"


class NamedConfigDescriptor(NamedDescriptor):
    pass


class NamedPropertyConfigDescriptorMeta(type):
    __config_name_container__ = "__named_config__"
    __property_name_container__ = "__named_property__"

    def __new__(cls, name, bases, cls_dict):
        cls_dict[cls.__config_name_container__] = []
        cls_dict[cls.__property_name_container__] = []
        for base in bases:
            if base_config_name_container:=getattr(base, cls.__config_name_container__):
                cls_dict[cls.__config_name_container__].extend(base_config_name_container)
            if base_property_name_container:=getattr(base, cls.__property_name_container__):
                cls_dict[cls.__property_name_container__].extend(base_property_name_container)
        for attr, attr_value in cls_dict.items():
            if isinstance(attr_value, NamedConfigDescriptor):
                attr_value.__set_name__(cls, attr)
                cls_dict[cls.__config_name_container__].append(attr)
            elif isinstance(attr_value, NamedPropertyDescriptor):
                attr_value.__set_name__(cls, attr)
                cls_dict[cls.__property_name_container__].append(attr)
        return super().__new__(cls, name, bases, cls_dict)