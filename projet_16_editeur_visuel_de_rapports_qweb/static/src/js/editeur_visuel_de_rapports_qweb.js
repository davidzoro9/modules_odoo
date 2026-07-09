<!-- Surcharge du moteur de rendu QWeb pour intégration de styles dynamiques -->
<template id="custom_invoice_layout" inherit_id="web.external_layout_standard">
    <xpath expr="//div[@class='header']" position="replace">
        <div class="header" t-att-style="'color: ' + (o.company_id.primary_pdf_color or '#000000') + ';'">
            <div class="row">
                <div class="col-6">
                    <img t-if="o.company_id.logo" t-att-src="image_data_uri(o.company_id.logo)" style="max-height: 45px;" alt="Logo"/>
                </div>
                <div class="col-6 text-right">
                    <h3 t-field="o.company_id.name"/>
                </div>
            </div>
        </div>
    </xpath>
</template>
