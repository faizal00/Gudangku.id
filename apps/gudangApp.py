from flask import session, redirect,render_template,url_for,request, flash
from config import collection_gudang
from bson import ObjectId

def showGudangApp():

    if 'username' in session and session['role']=='admin':
        data_gudang = collection_gudang.find()
        return render_template('/adm/gudang.html', gudang = data_gudang, username=session['username'],role = session['role'])
    return redirect(url_for('index'))

def addGudangApp():

    if 'username' in session and session['role']=='admin':
        gudang = request.form['gudang']
        alamat = request.form['alamat']
        if(collection_gudang.find_one({'gudang':gudang})):
            flash('Data Sudah Ada!', 'error')
            return redirect(url_for('showGudang'))
        else:
            collection_gudang.insert_one({'gudang': gudang, 'alamat':alamat})
            return redirect(url_for('showGudang'))
    return redirect(url_for('index'))

def editGudangApp(id):

    if 'username' in session and session['role']=='admin':
        gudang = request.form['gudang']
        alamat = request.form['alamat']
        new_gudang = {'gudang':gudang, 'alamat':alamat}
        collection_gudang.update_one({'_id': ObjectId(id)}, {'$set': new_gudang})
        return redirect(url_for('showGudang'))
    return redirect(url_for('index'))

def hapusGudangApp(id):
    
    if 'username' in session and session['role']=='admin':
        collection_gudang.delete_one({'_id': ObjectId(id)})
        return redirect(url_for('showGudang'))
    return redirect(url_for('index'))