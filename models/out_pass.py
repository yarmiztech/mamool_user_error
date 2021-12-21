from odoo import fields, models, api



class OrderLinesOutPass(models.Model):
    _inherit = 'order.lines.out.pass'

    @api.onchange('mamool')
    def check_mamool(self):
        return None