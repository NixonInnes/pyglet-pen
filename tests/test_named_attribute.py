import pytest

from pyglet_pen.utilities.named_attribute import NamedAttribute, NamedAttributeContainer


def test_named_attribute_descriptor():
    a = NamedAttribute()
    a.__set_name__(None, "test")
    assert a.name == "test"


def test_named_attribute_container():
    class TestClass(NamedAttributeContainer):
        a = NamedAttribute()
        b = NamedAttribute()
        c = NamedAttribute()
    
    assert TestClass.a.name == "a"
    assert TestClass.b.name == "b"
    assert TestClass.c.name == "c"

    assert hasattr(TestClass, "__attr_name_containers__")
    assert NamedAttribute.__name_container__ in TestClass.__attr_name_containers__

    assert "a" in TestClass.named_attributes
    assert "b" in TestClass.named_attributes
    assert "c" in TestClass.named_attributes

def test_named_attribute_container_instance():
    class TestClass(NamedAttributeContainer):
        a = NamedAttribute()
        b = NamedAttribute()
        c = NamedAttribute()
    
    instance = TestClass(a=1, b=2, c=3, d=4)
    assert instance.a == 1
    assert instance.b == 2
    assert instance.c == 3
    with pytest.raises(AttributeError):
        assert instance.d == 4

    assert hasattr(instance, "__attr_name_containers__")
    assert NamedAttribute.__name_container__ in instance.__attr_name_containers__

    assert "a" in instance.named_attributes
    assert "b" in instance.named_attributes
    assert "c" in instance.named_attributes
    assert "d" not in instance.named_attributes