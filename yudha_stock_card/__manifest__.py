{
	"name": "Yudha Stock Card",
	"version": "1.0",
	"depends": [
		"stock","uom"
	],
	"author": "Albertus Restiyanto Pramayudha",
	"website": "https://github.com/bikers1",
    'category': 'Warehouse',
	'price':'40',
    'currency': 'EUR',
	"summary" : "This modul to display stock card per product per Warehouse and product summary per Warehouse",
	"description": """  stock,
	                    stock card,
	                    stock card in odoo,
	                    stock card per location,
	                    stockcard,
	                    stock card per product,
			    stock card summary,
	                    product,
	                    product summary per warehouse,
			    reporting in odoo,
			    report product,
			    report product per warehouse,
			    summary product,
			    report summary product,
			    custome report,
			    custome report in odoo,
			    odoo report,
			    custume report,
			    custume report in odoo,
                      	    custume report,
                            custume report in odoo,
                            costume report,
                            costume report in odoo,
                            customize report,
                            customize report in odoo,			    
			    summary,
""",
	"data": [
		'views/yudha_stock_card_summary_view.xml',
		'views/yudha_stock_card_menu.xml',
		'views/yudha_stock_card_view.xml',
		'report/yudha_stock_card.xml',
		'report/yudha_stock_card_summary.xml',
		'security/ir.model.access.csv',
        # 'security/groups.xml',
	],
	"application": True,
	"installable": True,
    'auto_install': False,
    "images": ["static/description/icon.png"],
}
