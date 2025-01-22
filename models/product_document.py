from odoo import fields, models

class ProductDocument(models.Model):
    _inherit = 'product.document'
    
    attached_on_sale = fields.Boolean(
        string="Attached on Sales", 
        groups='sales_team.group_sale_salesman,export.res_groups_124_e6fc1b6e'
    )