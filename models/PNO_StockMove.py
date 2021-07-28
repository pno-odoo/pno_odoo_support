# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools import dumpstacks
import logging
_logger = logging.getLogger(__name__)


class StockMove(models.Model):
    _inherit = 'stock.move'

    def write(self, vals):
        if 'product_uom_qty' in vals:
            _logger.warning('write PNO extra logs')
            _logger.warning(vals)
            _logger.warning(dumpstacks())
        return super().write(vals)

    def _write(self, vals):
        if 'product_uom_qty' in vals:
            _logger.warning('_write PNO extra logs')
            _logger.warning(vals)
            _logger.warning(dumpstacks())
        return super()._write(vals)

    def _merge_moves(self, merge_into=False):
        _logger.warning('_merge_moves PNO extra logs')
        for move in self:
            _logger.warning(move.read())
        return super()._merge_moves(merge_into=False)