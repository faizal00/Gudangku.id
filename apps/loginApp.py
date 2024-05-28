from flask import Flask, render_template, request, redirect, url_for, session,flash
import bcrypt
from config import collection_user

def loginApp():
    
    if request.method == 'POST':
        login_user = collection_user.find_one({'username': request.form['username']})
        if login_user and bcrypt.checkpw(request.form['password'].encode('utf-8'), login_user['password']):
            session['username'] = request.form['username']
            session['role'] = login_user['role']
            return redirect(url_for('index'))
        flash('Username atau Password Tidak Valid!', 'error')
        return redirect(url_for('login'))
    return render_template('login.html')