from tests import context

import pytest
from lxml import etree

from tests import settings

# Learner's tests


@pytest.fixture(scope="module")
def tree():
    tree = etree.parse(settings.test_xml_file_path)
    yield tree


@pytest.fixture(scope="module")
def root(tree):
    root = tree.getroot()
    yield root


class TestRoot:
    def test_get_tag(self, root):
        pass

    def test_get_tag_no_namespace(self, root):
        pass

    def test_get_sub_elements(self, root):
        pass

    def test_get_sub_elements_with_tag_filter(self, root):
        pass


# class TestGet:
#     def test_good(self, cache):
#         assert cache["key"] == "value"
#
#     def test_bad(self, cache):
#         with pytest.raises(KeyError):
#             cache["bad"]
#
#
# class TestSet:
#     def test_dict_of_dict(self, cache, dict_of_dict):
#         cache.set("dict_of_dict", dict_of_dict, expire=60, read=False, tag="data")
#         assert cache["dict_of_dict"]["Alice"] == {"Bob": 1}
#         assert cache["dict_of_dict"]["Alice"]["Bob"] == 1
#
#     def test_class(self, cache, class_of_primitives):
#         cache.set("class", class_of_primitives, expire=60, read=False, tag="data")
#         assert cache["class"].integer == 1
#         assert cache["class"].string == "Alice"
