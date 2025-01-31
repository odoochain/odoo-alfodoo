# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import mock
from odoo.tests import common
from . import models


class BaseTestCmis(common.SavepointCase):

    @classmethod
    def _init_test_model(cls, model_cls):
        model_cls._build_model(cls.env.registry, cls.env.cr)
        cls.env.registry.setup_models(cls.env.cr)
        cls.env.registry.init_models(
            cls.env.cr, [model_cls._name], dict(cls.env.context, update_custom_fields=True)
        )
        return cls.env[model_cls._name]

    @classmethod
    def setUpClass(cls):
        super(BaseTestCmis, cls).setUpClass()
        # mock commit since it"s called in the _auto_init method
        cls.cr.commit = mock.MagicMock()
        cls.cmis_test_model = cls._init_test_model(
            models.CmisTestModel
        )
        cls.cmis_test_model_inherits = cls._init_test_model(
            models.CmisTestModelInherits
        )
        cls.cmis_test_model_related = cls._init_test_model(
            models.CmisTestModelRelated
        )
        cls.cmis_backend = cls.env.ref('cmis.cmis_backend_alfresco')
        cls.cmis_backend.initial_directory_write = '/odoo'

    def setUp(self):
        super(BaseTestCmis, self).setUp()

        # global patch

        def get_unique_folder_name(name, parent):
            return name
        self.patched_get_unique_folder_name = mock.patch.object(
            self.cmis_backend.__class__, 'get_unique_folder_name',
            side_effect=get_unique_folder_name
        )
        self.patched_get_unique_folder_name.start()

    def tearDown(self):
        super(BaseTestCmis, self).tearDown()
        self.patched_get_unique_folder_name.stop()
