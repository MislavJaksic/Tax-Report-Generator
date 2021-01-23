import os
import sys

# Adds "tax_report_generator" to sys.path
# Now you can do import with "from tax_report_generator.Sub-Package ..."
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "tax_report_generator"))
)
