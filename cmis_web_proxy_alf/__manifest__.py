# Copyright 2016 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Alfodoo CMIS Web Proxy for Alfresco",
    "category": "Document Management",
    "version": "14.0.1.0.1",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV",
    "website": "https://alfodoo.org",
    "depends": ["cmis_web_proxy"],
    "data": ["views/cmis_backend.xml", "views/cmis_web_proxy_alf.xml"],
    "demo": [],
    "pre_init_hook": "pre_init_hook",
    "images": ["static/description/main_icon.png"],
    "installable": True,
}
