# -*- coding: utf-8 -*-
# abelian_surfaces.py

import re

from lmfdb.base import app, r
import flask
from flask import Flask, session, g, render_template, url_for, make_response, request, redirect
from sage.all import *
import tempfile
import os
from pymongo import ASCENDING
from lmfdb.utils import to_dict, parse_range, make_logger, url_character
from lmfdb.abelian_surfaces import abelian_surfaces, abelian_surfaces_logger

###############################################################################
#   Route functions
#   Do not use url_for on these, use url_character defined in lmfdb.utils
###############################################################################

@abelian_surfaces.route("/")
def abelian_surfaces_front_page():

    args = to_dict(request.args)
    info = {}
    info['bread'] = [ ('AbelianSurface','/AbelianSurface') ]

    info['title'] = 'Abelian Surfaces'
    info['something_generated'] = 1+1

    return render_template("browse.html", **info)

@abelian_surfaces.route("/<label>")
def abelian_surfaces_page(label=None):

    args = to_dict(request.args)
    info = {}
    info['bread'] = [ ('AbelianSurface','/AbelianSurface') ]

    info['title'] = 'Abelian Surface %s' %label
    info['name'] = label
    info['something_generated'] = label
    info['properties2'] = [('name',label),('discriminant','1'),('conductor',1)]

    return render_template("surface.html", **info)

