# Copyright 2023 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Stock Release Channel Process End Date",
    "summary": """
        Allows to define an end date (and time) on a release channel and
        propagate it to the concerned pickings""",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "maintainers": ["rousseldenis"],
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/wms",
    "depends": [
        "stock_release_channel",
    ],
    "data": [
        "views/stock_release_channel.xml",
    ],
}
