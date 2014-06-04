# -*- coding: utf-8 -*-
from lmfdb.base import app
from lmfdb.utils import make_logger
from flask import Blueprint

hyperelliptic = Blueprint("hyperelliptic", __name__, template_folder='templates', static_folder="static")
hyperelliptic_logger = make_logger(hyperelliptic)


@hyperelliptic.context_processor
def body_class():
    return {'body_class': 'hyperelliptic'}

import main

app.register_blueprint(hyperelliptic, url_prefix="/HyperellipticCurve")
