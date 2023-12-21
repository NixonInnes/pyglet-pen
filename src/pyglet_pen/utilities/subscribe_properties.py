from typing import Callable

from .named_descriptor import NamedDescriptor, NamedDescriptorMeta
from .types import T


class SubscribableProperty[T](NamedDescriptor):
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


class SubscribeProperties(metaclass=NamedDescriptorMeta):
    __extend_named_descriptors__ = True
    
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance._subscriptions = {}
        for k, v in kwargs.items():
            if k in cls.__named_descriptors__:
                setattr(instance, k, v)
        return instance
    
    def subscribe_to_property(self, property_name: str, callback: Callable[[T], None]):
        self._subscriptions.setdefault(property_name, []).append(callback)

    @property
    def property_names(self):
        return self.__named_descriptors__
    
    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(f'{k}={getattr(self, k)}' for k in self.property_names)})"
