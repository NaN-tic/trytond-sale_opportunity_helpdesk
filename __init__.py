# This file is part of the sale_opportunity_helpdesk module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .helpdesk import *
from .getmail import *

def register():
    Pool.register(
        Helpdesk,
        SaleOpportunityHelpdesk,
        GetmailServer,
        module='sale_opportunity_helpdesk', type_='model')
