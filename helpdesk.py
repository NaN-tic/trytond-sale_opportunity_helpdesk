# This file is part of the sale_opportunity_helpdesk module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Helpdesk', 'SaleOpportunityHelpdesk']


class Helpdesk(metaclass=PoolMeta):
    __name__ = 'helpdesk'
    opportunities = fields.Many2Many('sale.opportunity.helpdesk', 'helpdesk',
        'opportunity', 'Opportunities', states={
            'readonly': Eval('state').in_(['cancel', 'done']),
            'invisible': ~Eval('kind').in_(['opportunity', 'generic']),
            },
        depends=['state'])

    @classmethod
    def __setup__(cls):
        super(Helpdesk, cls).__setup__()
        value = ('opportunity', 'Opportunity')
        if not value in cls.kind.selection:
            cls.kind.selection.append(value)


class SaleOpportunityHelpdesk(ModelSQL):
    'Sale Opportunity - Helpdesk'
    __name__ = 'sale.opportunity.helpdesk'
    _table = 'sale_opportunity_helpdesk_rel'
    opportunity = fields.Many2One('sale.opportunity', 'Opportunity',
        ondelete='CASCADE', select=True, required=True)
    helpdesk = fields.Many2One('helpdesk', 'Helpdesk', ondelete='RESTRICT',
        select=True, required=True)
