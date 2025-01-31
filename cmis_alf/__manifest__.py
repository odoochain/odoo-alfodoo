# © 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'CMIS for Alfresco',
    'version': '14.0.1.0.1',
    'summary': 'Alfresco extension for the CMIS Connector',
    'category': 'Document Management',
    'author': "ACSONE SA/NV",
    'website': 'https://alfodoo.org',
    'license': 'AGPL-3',
    'depends': [
        'cmis',
    ],
    'data': [
        'views/cmis_backend_view.xml',
    ],
    'images': [
        'static/description/main_icon.png',
    ],
    'external_dependencies': {
        'python': ['requests'],
    },
    'installable': True,
    'auto_install': False,
}
