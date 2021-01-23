import pytest

from tests import context
from tax_report_generator.command_line_parsing import parser



class TestParser(object):
  @pytest.fixture(scope="function")
  def basic_parser():
    #setup
    yield parser.Parser()
    #teardown
    print "Finished!"
  
  def test_ParseCorrectArguments(self, basic_parser):
    
  def test_ParseIncorrectArguments(self):
    