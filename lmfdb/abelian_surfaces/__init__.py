# -*- coding: utf-8 -*-
from lmfdb.base import app
from lmfdb.utils import make_logger
from flask import Blueprint

abelian_surfaces = Blueprint("abelian_surfaces", __name__, template_folder='templates', static_folder="static")
abelian_surfaces_logger = make_logger(abelian_surfaces)


@abelian_surfaces.context_processor
def body_class():
    return {'body_class': 'abelian_surfaces'}

import main

app.register_blueprint(abelian_surfaces, url_prefix="/AbelianSurface")
