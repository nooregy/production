from odoo import api
from odoo import fields
from odoo import models
from datetime import date
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
from odoo .exceptions import Warning
import logging
class stock_picking_scan(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def scan_from_ui(self, res_id, created, added):
        company_id = self.env.company.id
        logging.warning("\n Entered Form >>>>>>>>>>>>>>>>>>>>>>>>>>\ n")
        rec = self.env['stock.picking'].search([('id', '=', res_id)])
        rec.scan_products_ids.unlink()
        print("1")
        # print rec.scan_products_ids
        if len(created) > 0 and rec.use_create_lots:
            for created_obj in created.values():
                for obj in created_obj.values():
                    if not obj['expiration_date']:
                        obj['expiration_date']=date.today() + relativedelta(months=+24)
                    if "lot_name" in obj.keys() and not obj['lot_name']:
                        obj['lot_name'] = obj['lot_no']
                    elif "lot_name" not in obj.keys():
                        obj['lot_name'] = obj['lot_no']
                    if "company_id" not in obj.keys():
                        obj['company_id']=company_id
                    del(obj['lot_no'])

                    self.env['stock.production.lot'].create(obj)
        print("2")
        if len(added) > 0:
            scan_lines = []
            for scan_obj in added.values():
                for obj in scan_obj.values():
                    if  obj['expiration_date'] == 'False':
                        obj['expiration_date']=date.today() + relativedelta(months=+24)
                    if "lot_name" in obj.keys() and not obj['lot_name']:
                        obj['lot_name'] = obj['lot_no']
                    elif "lot_name" not in obj.keys():
                        obj['lot_name'] = obj['lot_no']


                    print(obj)
                    scan_lines.append([0, 0, obj])
            rec.scan_products_ids = scan_lines
