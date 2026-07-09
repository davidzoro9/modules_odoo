/* Composant OWL de Planification Gantt */
import { Component, xml } from "@odoo/owl";
export class MrpGanttRenderer extends Component {
    static template = xml`
        <div class="mrp-gantt-chart">
            <t t-foreach="props.workCenters" t-as="wc" t-key="wc.id">
                <div class="gantt-row" t-on-drop="(ev) => this._onDropOrder(ev, wc.id)">
                    <span class="wc-name" t-esc="wc.name"/>
                    <div class="tasks-container">
                        <!-- Rendu des blocs Gantt -->
                    </div>
                </div>
            </t>
        </div>`;
        
    _onDropOrder(ev, workCenterId) {
        const orderId = ev.dataTransfer.getData("text/plain");
        this.env.model.updateOrderCenter(orderId, workCenterId);
    }
}
