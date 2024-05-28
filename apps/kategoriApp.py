from flask import session, redirect,render_template,url_for,request,flash
from config import collection_kategori
from bson import ObjectId

def showKategoriApp():

    if 'username' in session and session['role'] == 'admin':
        data_kategori = collection_kategori.find()
        return render_template('/adm/kategori.html', kategori = data_kategori, username=session['username'],role = session['role'])
    return redirect(url_for('index'))

def addKategoriApp():

    if 'username' in session and session['role'] == 'admin':
        kategori = request.form['kategori']
        if(collection_kategori.find_one({'kategori':kategori})):
            flash('Data Sudah Ada!', 'error')
            return redirect(url_for('showKategori'))
        else:
            collection_kategori.insert_one({'kategori': kategori})
            return redirect(url_for('showKategori'))
    return redirect(url_for('index'))

def editKategoriApp(id):

    if 'username' in session and session['role'] == 'admin':
        kategori = request.form['kategori']
        new_kategori = {'kategori':kategori}
        if(collection_kategori.find_one({'kategori':kategori})):
            flash('Data Sudah Ada!', 'error')
            return redirect(url_for('showKategori'))
        else:
            collection_kategori.update_one({'_id': ObjectId(id)}, {'$set': new_kategori})
            return redirect(url_for('showKategori'))
    return redirect(url_for('index'))

def hapusKategoriApp(id):
    
    if 'username' in session and session['role'] == 'admin':
        collection_kategori.delete_one({'_id': ObjectId(id)})
        return redirect(url_for('showKategori'))
    return redirect(url_for('index'))