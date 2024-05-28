from flask import request, redirect, url_for, flash,session
import bcrypt
from config import collection_user
from bson import ObjectId

def addUserApp():

    if 'username' in session and session['role'] == 'admin':
        username = request.form['username']
        password = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
        role = request.form['role']
        gudang = request.form['gudang']
        if(collection_user.find_one({'username':username})):
            flash('Data Sudah Ada!', 'error')
            return redirect(url_for('index'))
        elif(role=="admin" and gudang==""):
            collection_user.insert_one({'username': username, 'password': password,'role':role, 'gudang':gudang})
            return redirect(url_for('index'))
        elif(username == "" or password == "" or role == "" or gudang == ""):
            flash('Data Tidak Boleh Kosong!', 'error')
            return redirect(url_for('index'))
        else:
            collection_user.insert_one({'username': username, 'password': password,'role':role, 'gudang':gudang})
            return redirect(url_for('index'))
    return redirect(url_for('index'))

def hapusUserApp(id):
    
    if 'username' in session and session['role'] == 'admin':
        if(session['role']=='admin' and collection_user.find_one({'_id': ObjectId(id)})['role']=='admin'):
            flash('Tidak dapat menghapus!', 'error')
            return redirect(url_for('index'))
        else:
            collection_user.delete_one({'_id': ObjectId(id)})
            return redirect(url_for('index'))
    return redirect(url_for('index'))