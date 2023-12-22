from itertools import chain
from typing import Callable

from .classproperty import classproperty
from .named_descriptor2 import NamedDescriptor, NamedDescriptorMeta
from .types import T


class AttributeSubscriber[T](NamedDescriptor):
    def __init__(self, default: T):
        self._default = default
    
    def __get__(self, instance, owner) -> T:
        if instance is None:
            return self
        return instance.__dict__.get(self, self._default)
    
    def __set__(self, instance, value: T):
        instance.__dict__[self] = value
        for callback in instance._subscriptions.get(self.name, []):
            callback(value)
    
    def __delete__(self, instance):
        del instance.__dict__[self]


class SubscriberContainer(metaclass=NamedDescriptorMeta):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance._subscriptions = {}
        for k, v in kwargs.items():
            if k in cls.named_attributes:
                setattr(instance, k, v)
        return instance
    
    @classproperty
    def named_attributes(cls):
        return cls.get_subscribable_attribute_names()

    @classmethod
    def get_subscribable_attribute_names(cls):
        return list(chain.from_iterable([getattr(cls, container) for container in cls.__name_containers__]))
    

    def subscribe_to_attribute(self, attr_name: str, callback: Callable[[T], None]):
        self._subscriptions.setdefault(attr_name, []).append(callback)

    @property
    def attribute_name_containers(self):
        return self.__name_containers__
    
    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(f'{k}={getattr(self, k)}' for k in self.named_attributes)})"
