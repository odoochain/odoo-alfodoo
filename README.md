
<!-- /!\ Non OCA Context : Set here the badge of your runbot / runboat instance. -->
[![Pre-commit Status](https://github.com/acsone/alfodoo/actions/workflows/pre-commit.yml/badge.svg?branch=14.0)](https://github.com/acsone/alfodoo/actions/workflows/pre-commit.yml?query=branch%3A14.0)
[![Build Status](https://github.com/acsone/alfodoo/actions/workflows/test.yml/badge.svg?branch=14.0)](https://github.com/acsone/alfodoo/actions/workflows/test.yml?query=branch%3A14.0)
[![codecov](https://codecov.io/gh/acsone/alfodoo/branch/14.0/graph/badge.svg)](https://codecov.io/gh/acsone/alfodoo)
<!-- /!\ Non OCA Context : Set here the badge of your translation instance. -->

<!-- /!\ do not modify above this line -->

# Alfodoo

Alfodoo is a set of addons to seamlessly integrate an external Document
Management System with Odoo.

Alfresco Enterprise Content Management System (from version 4.2) is supported.

The code is structured in two parts:

- pure CMIS 1.1 compliant modules (cmis_field, cmis_web)
- Alfresco specific extension modules (cmis_alf, cmis_web_alf).

It is therefore possible in principle to easily integrate Other CMIS compliants
content management systems such as Nuxeo, Documentum, etc. This has not been tested yet.

Documentation and installation instructions can be found at https://alfodoo.org.

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[cmis_alf](cmis_alf/) | 14.0.1.0.1 |  | Alfresco extension for the CMIS Connector
[cmis_field](cmis_field/) | 14.0.1.0.1 |  | Specialized field to work with a CMIS server
[cmis_report_write](cmis_report_write/) | 14.0.1.0.1 |  | Cmis Report Write
[cmis_web](cmis_web/) | 14.0.1.0.1 |  | CMIS Web browser widget
[cmis_web_alf](cmis_web_alf/) | 14.0.1.0.1 |  | Extensions to the Alfodoo web widgets for Alfresco
[cmis_web_bus](cmis_web_bus/) | 14.0.1.0.1 |  | Cmis Web Bus
[cmis_web_proxy](cmis_web_proxy/) | 14.0.1.0.1 |  | Odoo as proxy server for your cmis requests.
[cmis_web_proxy_alf](cmis_web_proxy_alf/) | 14.0.1.0.1 |  | Alfodoo CMIS Web Proxy for Alfresco
[cmis_web_report_write](cmis_web_report_write/) | 14.0.1.0.1 |  | Cmis Web Report Write
[cmis_web_report_write_alf](cmis_web_report_write_alf/) | 14.0.1.0.1 |  | Cmis Web Report Write Alf

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to ACSONE
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
<!-- /!\ Non OCA Context : Set here the full description of your organization. -->
