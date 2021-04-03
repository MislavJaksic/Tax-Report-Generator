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


def run():
    """Entry point for the runnable script."""
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run()."""
    run()
