{
	"name": "TaxFree for Odoo by GlobalBlue",
	"category": "Sales",
	"version": "16.0.1.0.0",
	"author": "ProcessControl",
	"license": "OPL-1",
	"website": "",
	"depends": [
		'sale',
		'point_of_sale'
	],
	"qweb": [
		'static/src/xml/ReceiptScreen/ReceiptScreen.xml',
		'static/src/xml/PaymentScreen/PaymentScreen.xml',
	],
	"data": [
		'views/res_config_settings.xml',
		'views/pos_order.xml',
		'wizard/pos_payment.xml',
	],
	"assets": {
		"point_of_sale.assets": [
			"global_blue_tax_free/static/src/js/ReceiptScreen/ReceiptScreen.js",
			"global_blue_tax_free/static/src/xml/**/*.xml",
		],
	},
	"application": True,
    'installable': True,
    'auto_install': False,
}