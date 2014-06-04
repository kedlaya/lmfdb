# -*- coding: utf-8 -*-
# hyperelliptic.py

import re

from lmfdb.base import app, r
import flask
from flask import Flask, session, g, render_template, url_for, make_response, request, redirect
from sage.all import *
import tempfile
import os
from pymongo import ASCENDING
from lmfdb.utils import to_dict, parse_range, make_logger, url_character
from lmfdb.hyperelliptic import hyperelliptic, hyperelliptic_logger

###############################################################################
#   Route functions
#   Do not use url_for on these, use url_character defined in lmfdb.utils
###############################################################################

@hyperelliptic.route("/")
def hyperelliptic_front_page():

    args = to_dict(request.args)
    info = {}
    info['bread'] = [ ('HyperellipticCurve','/HyperellipticCurve') ]

    info['title'] = 'Hyperelliptic Curves'
    info['something_generated'] = 1+1

    return render_template("hyperelliptic_front.html", **info)

@hyperelliptic.route("/<label>")
def hyperelliptic_page(label=None):

    args = to_dict(request.args)
    info = {}
    info['bread'] = [ ('HyperellipticCurve','/HyperellipticCurve') ]

    info['title'] = 'Hyperelliptic Curve %s' %label
    info['name'] = label
    info['something_generated'] = label
    info['properties2'] = [('name',label),('discriminant','1')]

    return render_template("hyperelliptic.html", **info)

