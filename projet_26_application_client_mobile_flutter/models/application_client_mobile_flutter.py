# -*- coding: utf-8 -*-
from odoo import models, fields, api

/* API d\'écoute de notifications push personnalisées */
class MobilePushNotification(models.Model):
    _name = 'mobile.push.notification'
    _description = 'Push Notification Service for Mobile App'

    def send_push_to_user(self, user_id, title, message):
        user = self.env['res.users'].browse(user_id)
        device_tokens = user.partner_id.mobile_device_ids.mapped('token')
        if device_tokens:
            payload = {
                "registration_ids": device_tokens,
                "notification": {
                    "title": title,
                    "body": message,
                    "sound": "default"
                }
            }
            # Envoi vers Google Firebase (FCM)
            requests.post("https://fcm.googleapis.com/fcm/send", json=payload, headers={
                "Authorization": "key=" + self.env['ir.config_parameter'].sudo().get_param('fcm.api_key')
            })
