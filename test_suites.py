import unittest
import HtmlTestRunner

from test_check_price import TestGroceryCart
from test_count_items import TestGroceryCart
from test_create_order import TestGroceryOrder
from test_find_cheapest_product import TestCart
from test_find_expensive_product import TestCart
from test_get_a_single_order import TestGroceryOrder
from test_get_all_items import TestGroceryCart
from test_modify_item_from_cart import TestCart
from test_replace_an_item_from_cart import TestCart
from test_search_in_cart import TestGroceryCart


class TestSuite(unittest.TestCase):

    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(TestCart),
                              unittest.defaultTestLoader.loadTestsFromTestCase(TestGroceryCart),
                              unittest.defaultTestLoader.loadTestsFromTestCase(TestGroceryOrder)])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports = True,
            report_title = "Test Execution Report",
            report_name = "Test Results"
        )

        runner.run(tests_to_run)