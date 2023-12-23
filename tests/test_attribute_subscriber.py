import pytest

from pyglet_pen.utilities.attribute_subscriber import AttributeSubscriber, SubscriberContainer


def test_attribute_subscriber_descriptor():
    a = AttributeSubscriber(1)
    a.__set_name__(None, "test")
    assert a.name == "test"


def test_subscriber_container_base():
    class TestClass(SubscriberContainer):
        a = AttributeSubscriber(1)
        b = AttributeSubscriber(2)
        c = AttributeSubscriber("test")
    
    assert TestClass.a.name == "a"
    assert TestClass.b.name == "b"
    assert TestClass.c.name == "c"

    assert hasattr(TestClass, "__attr_name_containers__")
    assert AttributeSubscriber.__name_container__ in TestClass.__attr_name_containers__

    assert "a" in TestClass.named_attributes
    assert "b" in TestClass.named_attributes
    assert "c" in TestClass.named_attributes

def test_subscriber_container_base_instance():
    class TestClass(SubscriberContainer):
        a = AttributeSubscriber(1)
        b = AttributeSubscriber(2)
        c = AttributeSubscriber("test")
    
    instance = TestClass(a=1, b=2, c="test", d=4)
    assert instance.a == 1
    assert instance.b == 2
    assert instance.c == "test"
    with pytest.raises(AttributeError):
        assert instance.d == 4

    assert hasattr(instance, "__attr_name_containers__")
    assert AttributeSubscriber.__name_container__ in instance.__attr_name_containers__

    assert "a" in instance.named_attributes
    assert "b" in instance.named_attributes
    assert "c" in instance.named_attributes
    assert "d" not in instance.named_attributes