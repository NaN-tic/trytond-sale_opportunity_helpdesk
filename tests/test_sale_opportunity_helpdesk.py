# This file is part of the sale_opportunity_helpdesk module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SaleOpportunityHelpdeskTestCase(ModuleTestCase):
    'Test Sale Opportunity Helpdesk module'
    module = 'sale_opportunity_helpdesk'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleOpportunityHelpdeskTestCase))
    return suite