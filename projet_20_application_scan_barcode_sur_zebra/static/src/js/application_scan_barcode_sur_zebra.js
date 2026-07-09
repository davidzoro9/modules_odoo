/* Composant OWL de Scan Barcode Mobile */
import { Component, onMounted } from "@odoo/owl";
export class BarcodeValidator extends Component {
    static template = "barcode.ValidatorTemplate";
    
    setup() {
        onMounted(() => {
            // Écoute de l'événement natif Android envoyé par le scanner Zebra
            window.addEventListener('zebra_scan_received', this.onScanSuccess.bind(this));
        });
    }

    onScanSuccess(event) {
        const barcode = event.detail.barcode;
        const line = this.props.pickingLines.find(l => l.barcode === barcode);
        if (line) {
            this.env.model.incrementLineQty(line.id);
            this.playSuccessBeep();
        } else {
            this.playErrorBeep();
            this.env.services.notification.add("Produit non présent dans cette commande !", {type: 'danger'});
        }
    }
}
