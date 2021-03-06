# -*- coding: utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from socketserver import ThreadingMixIn

import os
from models import *

# configuration
DEBUG = True
SECRET_KEY = '&Us\xb9\xa0\xef\xc9\xe8H\xfc\x10\xe2\xfd9\xffR\x8c\xa2\xb65\x18\xd9\xf7?'
USERNAME = 'admin'
PASSWORD = '123456'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def show_entries():
    entries = Entries.select()
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    entry = Entries(title=request.form['title'],text=request.form['text'])
    entry.save()
    flash('新的留言发布成功！')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = '用户名错误！'
        elif request.form['password'] != app.config['PASSWORD']:
            error = '密码错误！'
        else:
            session['logged_in'] = True
            flash('处于登录状态！')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('你已经退出系统！')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run()
