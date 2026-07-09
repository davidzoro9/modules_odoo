# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LivechatChatbot(models.Model):
    _inherit = 'im_livechat.channel'

    def get_ai_response(self, user_message):
        # Génération d'embeddings et recherche de la FAQ Odoo la plus pertinente
        embedding = self.env['ai.vector.service'].generate_embedding(user_message)
        faq_match = self.env['slide.slide'].search_vector_nearest(embedding, limit=1)
        
        # Envoi à GPT pour reformulation polie
        response = self.env['openai.client'].generate_answer(
            prompt=user_message,
            context=faq_match.html_content
        )
        return response
