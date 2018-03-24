#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 08:54
# @Author  : GUO Ziyao
"""
Homepage
"""
from flask import Blueprint
from flask import render_template

bp = Blueprint('index', __name__)


@bp.route('/')
def hello_world():
    return render_template('welcome.html')


@bp.app_errorhandler(404)
def not_found(ex):
    return render_template('404.html'), 404
