# This file is part of the sale_opportunity_helpdesk module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import helpdesk
from . import getmail

def register():
    Pool.register(
        helpdesk.Helpdesk,
        helpdesk.SaleOpportunityHelpdesk,
        module='sale_opportunity_helpdesk', type_='model')
    Pool.register(
        getmail.GetmailServer,
        depends=['getmail'],
        module='sale_opportunity_helpdesk', type_='model')
