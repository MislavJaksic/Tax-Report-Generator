"""
    tax-report-generator.py
    ------------------

    Runs the project.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys
from lxml import etree

from tax_report_generator.package_one import module_one
from tax_report_generator import lxmler


def main(args):
    """main() will be run if you run this script directly"""

    tree = etree.parse("ObrazacURA.xml")
    root = tree.getroot()
    print(root[2][0].tag)
    print(root[2][0].text)
    # print(list(root[2][0]))
    # print(etree.tostring(root, pretty_print=True))
    sum = get_sum_of_all_sub_elements_with_tag_pattern_of_element("R10", root)
    print(sum)
    sum = get_sum_of_all_sub_elements_with_tag_pattern_of_element("R11", root)
    print(sum)


def load_tree(file_path):
    tree = etree.parse(file_path)
    return tree


def get_tree_root(tree):
    root = tree.getroot()
    return root


def CreateElement(tag):
    return etree.Element(tag)


def get_tag(element):
    tag_with_namespace_prefix = element.tag
    return get_tag_without_namespace_prefix(tag_with_namespace_prefix)


def get_tag_without_namespace_prefix(tag_with_namespace_prefix):
    return tag_with_namespace_prefix.split("}")[-1]


def set_element_text(element, data):
    if type(data) is float:
        data = transform_data.RoundHalfUp(data, 2)

    if type(data) is numpy.float64:
        data = transform_data.RoundHalfUp(data, 2)

    if type(data) is pandas._libs.tslibs.timedeltas.Timedelta:
        if data.components.hours == 0:
            if data.components.minutes == 0:
                if data.components.seconds == 0:
                    data = transform_data.GetDays(data)

    if type(data) is pandas._libs.tslibs.timestamps.Timestamp:
        data = transform_data.GetDate(data)

    element.text = str(data)


def add_sub_element_to_element(child_element, element):
    child_copy = copy.deepcopy(child_element)
    element.append(child_copy)


def insert_sub_element_to_element_at_index(child_element, element, index):
    child_copy = copy.deepcopy(child_element)
    element.insert(index, child_copy)


def get_sub_elements(parent_element):
    return list(parent_element)


def get_sub_elements_with_tag_pattern(parent_element, pattern):
    tag_pattern_sub_elements = []
    sub_elements = get_sub_elements(parent_element)
    for element in sub_elements:
        tag = get_tag(element)
        if pattern in tag:
            tag_pattern_sub_elements.append(element)

    return tag_pattern_sub_elements


def get_all_sub_elements(parent_element):
    child_elements = get_sub_elements(parent_element)

    for child_element in parent_element:
        child_elements.extend(get_all_sub_elements(child_element))

    return child_elements


def get_all_sub_elements_with_tag_pattern(parent_element, pattern):
    tag_pattern_sub_elements = []
    sub_elements = get_all_sub_elements(parent_element)
    for element in sub_elements:
        tag = get_tag(element)
        if pattern in tag:
            tag_pattern_sub_elements.append(element)

    return tag_pattern_sub_elements


def get_sum_of_sub_elements_with_tag_pattern_of_element(pattern, element):
    all_children = get_sub_elements(element)
    sum = 0.0
    for child_element in all_children:
        child_tag = get_tag_without_namespace_prefix(child_element.tag)
        if pattern in child_tag:
            sum += float(child_element.text)

    return sum


def get_sum_of_all_sub_elements_with_tag_pattern_of_element(pattern, element):
    all_children = get_all_sub_elements(element)
    sum = 0.0
    for child_element in all_children:
        child_tag = get_tag_without_namespace_prefix(child_element.tag)
        if pattern in child_tag:
            sum += float(child_element.text)

    return sum


def WriteTreeToFile(tree, file_name):
    tree.write(file_name)


def PrintTree(tree):
    root = GetTreeRoot(tree)
    PrintElement(root)


def PrintElement(element):
    print(etree.tostring(element, pretty_print=True))


def run():
    """Entry point for the runnable script."""
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run()."""
    run()
