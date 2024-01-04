from collections import defaultdict
from itertools import chain
from typing import List, Optional

from pprint import pprint

from .classproperty import classproperty


class NamedAttribute:
    __name_container__ = "__named_attributes__"

    def __set_name__(self, owner, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name


class NamedAttributeMeta(type):

    def __new__(cls, name, bases, cls_dict):
        cls_name_containers = []
        cls_containers = defaultdict(list)
        
        # Get all named attributes from base classes
        for base in bases:
            if hasattr(base, "__attr_name_containers__"):
                base_name_containers = getattr(base, "__attr_name_containers__")
                cls_name_containers.extend(base_name_containers)
                for name_container in base_name_containers:
                    cls_containers[name_container].extend(getattr(base, name_container, []))
        
        # Get all named attributes from this class
        for attr, attr_value in cls_dict.items():
            if isinstance(attr_value, NamedAttribute):
                attr_value.__set_name__(cls, attr)
                container = attr_value.__name_container__
                cls_containers[container].append(attr)
                if container not in cls_name_containers:
                    cls_name_containers.append(container)
        
        # Update class dictionary
        if "__attr_name_containers__" in cls_dict:
            cls_dict["__attr_name_containers__"] = list(
                set(cls_dict["__attr_name_containers__"] + cls_name_containers)
            )
        else:
            cls_dict["__attr_name_containers__"] = cls_name_containers
        cls_dict.update(cls_containers)
        
        return super().__new__(cls, name, bases, cls_dict)
    

class NamedAttributeContainer(metaclass=NamedAttributeMeta):
    def __new_instance__(cls, instance):
        return instance

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance = cls.__new_instance__(cls, instance)
        for k, v in kwargs.items():
            if k in cls.named_attributes:
                setattr(instance, k, v)
        return instance
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classproperty
    def attribute_name_containers(cls) -> List[str]:
        return cls.__attr_name_containers__
    
    @classproperty
    def named_attributes(cls) -> List[str]:
        return list(chain.from_iterable([getattr(cls, container, []) for container in cls.attribute_name_containers]))
    
    @classmethod
    def get_name_container(cls, container_name: str) -> Optional[List[str]]:
        return getattr(cls, container_name, None)
    
    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(f'{k}={getattr(self, k)}' for k in self.named_attributes)})"