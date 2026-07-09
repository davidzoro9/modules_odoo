# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MigrationOdooV14AV17Enterprise(models.Model):
    _name = 'portfolio.migration.odoo.v14.a.v17.enterprise'
    _description = "Migration Odoo v14 à v17 Enterprise"

    # Exemple de script d\'adaptation de schéma SQL de transition
    def pre_migration_sql_cleanup(cr):
        # Suppression des index inutilisés et correction des contraintes obsolètes
        cr.execute("""
            ALTER TABLE sale_order_line DROP CONSTRAINT IF EXISTS sale_order_line_qty_check;
            CREATE INDEX IF NOT EXISTS idx_sale_order_date_order ON sale_order(date_order);
        """)
        # Nettoyage des anciennes entrées du registre d\'attachements système
        cr.execute("DELETE FROM ir_attachment WHERE res_model = 'mail.message' AND create_date < NOW() - INTERVAL '3 years';")
