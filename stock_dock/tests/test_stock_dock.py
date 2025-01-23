from odoo.tests.common import TransactionCase


class TestStockDock(TransactionCase):
    def setUp(self):
        super().setUp()

        self.warehouse = self.env.ref("stock.warehouse0")
        stock_dock_env = self.env["stock.dock"]
        self.stock_dock = stock_dock_env.create(
            {
                "name": "Test",
            }
        )

    def test_00_default_warehouse_id(self):
        # Check if the warehouse_id is set correctly
        self.assertEqual(
            self.stock_dock.warehouse_id,
            self.warehouse,
            "The warehouse should be set to the created warehouse.",
        )

    def test_01_company_id_related_field(self):
        # Check if the company_id is set correctly based on the warehouse
        self.assertEqual(
            self.stock_dock.company_id,
            self.warehouse.company_id,
            "The company should be related to the warehouse's company.",
        )

    def test_02_active_field_default(self):
        # Check if the active field is set to True by default
        self.assertTrue(
            self.stock_dock.active, "The active field should be True by default."
        )
