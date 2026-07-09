/* Intégration JS du formulaire Stripe dans Odoo Web */
odoo.define('ecommerce_stripe.payment_element', function (require) {
    "use strict";
    var publicWidget = require('web.public.widget');

    publicWidget.registry.StripeElement = publicWidget.Widget.extend({
        selector: '#stripe-payment-form',
        start: function () {
            this.stripe = Stripe(this.el.dataset.publishableKey);
            this.elements = this.stripe.elements({clientSecret: this.el.dataset.clientSecret});
            this.paymentElement = this.elements.create("payment");
            this.paymentElement.mount("#payment-element");
        }
    });
});
