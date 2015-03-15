# -*- coding: utf-8 -*-
__author__ = 'alacret'

from openerp import models,fields


class Course(models.Model):
    """
    Clase de un modelo para pruebas en el curso
    """
    _name = "openacademy.course"
    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")

