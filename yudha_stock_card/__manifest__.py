{
	"name": "Yudha Stock Card",
	"version": "12.0.0.0",
	"depends": [
		"stock",
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
	                    product,
	                    product summary per warehouse,
""",
	"data": [
		"views/yudha_stock_card_view.xml",
		'views/yudha_stock_card_summary_view.xml',
		'views/yudha_stock_card_menu.xml',
		'report/yudha_stock_card.xml',
		'report/yudha_stock_card_summary.xml',

		'security/ir.model.access.csv',

	],
	"application": True,
	"installable": True,
    'auto_install': False,
    "images": ["static/description/icon.png"],
}
