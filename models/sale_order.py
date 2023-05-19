from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Loan Order"

    confirmed_user_id = fields.Boolean(string="confirmed")