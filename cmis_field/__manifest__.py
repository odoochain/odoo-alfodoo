# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Alfodoo CMIS Field',
    'version': "14.0.1.0.1",
    'summary': 'Specialized field to work with a CMIS server',
    'category': 'Document Management',
    'author': "ACSONE SA/NV ",
    'website': 'https://alfodoo.org',
    'license': 'AGPL-3',
    'depends': [
        'cmis'
    ],
    'data': [
        'views/cmis_backend_view.xml'
    ],
    'installable': True,
    'images': [
        'static/description/main_icon.png',
    ],
}
