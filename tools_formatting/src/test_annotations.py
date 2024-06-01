import pytest
from src.annotations import Point, locate


@pytest.mark.parametrize(
    "defined_object,expected",
    (
        (locate, {"latitude": float, "longitude": float, "return": Point}),
        (Point, {"lat": float, "long": float}),
    ),
)
def test_annotations(defined_object, expected):
    """test the class/functions against its expected annotations"""
    assert getattr(defined_object, "__annotations__") == expected
