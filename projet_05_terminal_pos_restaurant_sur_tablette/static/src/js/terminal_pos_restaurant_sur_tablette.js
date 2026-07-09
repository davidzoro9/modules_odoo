import { Component, useState } from "@odoo/owl";
export class RestaurantOrderPad extends Component {
    static template = "pos_restaurant.OrderPad";
    
    setup() {
        this.state = useState({
            activeTable: null,
            currentOrder: [],
        });
    }

    async sendToKitchen() {
        if (this.state.currentOrder.length === 0) return;
        await this.env.pos.sendOrderLinesToKitchen(
            this.state.activeTable,
            this.state.currentOrder
        );
        this.state.currentOrder = [];
        this.render();
    }
}
