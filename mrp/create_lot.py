
from odoo import _, api, models
from odoo.exceptions import UserError

class MrpProduction(models.Model):
    _description = 'Production Order'
    _date_name = 'date_planned_start'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'priority desc, date_planned_start asc,id'



    def action_generate_serial(self):
        self.ensure_one()
        self.lot_producing_id = 120
        if self.move_finished_ids.filtered(lambda m: m.product_id == self.product_id).move_line_ids:
            self.move_finished_ids.filtered(lambda m: m.product_id == self.product_id).move_line_ids.lot_id = self.lot_producing_id
        if self.product_id.tracking == 'serial':
            self._set_qty_producing()

            # self.env['stock.lot'].create({
            #     'product_id': self.product_id.id,
            #     'company_id': self.company_id.id,
            #     'name': self.env['stock.lot']._get_next_serial(self.company_id, self.product_id) or self.env[
            #         'ir.sequence'].next_by_code('stock.lot.serial'),
            # })