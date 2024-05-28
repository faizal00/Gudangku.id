from flask import session, redirect,render_template,url_for,request, flash
from config import collection_mitra
from bson import ObjectId

def showMitraApp():

    if 'username' in session and session['role']=='admin':
        data_mitra = collection_mitra.find()
        return render_template('/adm/mitra.html', mitra = data_mitra, username=session['username'],role = session['role'])
    return redirect(url_for('index'))

def addMitraApp():

    if 'username' in session and session['role']=='admin':
        mitra = request.form['mitra']
        alamat = request.form['alamat']
        if(collection_mitra.find_one({'mitra':mitra})):
            flash('Data Sudah Ada!', 'error')
            return redirect(url_for('showMitra'))
        else:
            collection_mitra.insert_one({'mitra': mitra, 'alamat':alamat})
            return redirect(url_for('showMitra'))
    return redirect(url_for('index'))

def editMitraApp(id):

    if 'username' in session and session['role']=='admin':
        mitra = request.form['mitra']
        alamat = request.form['alamat']
        new_mitra = {'mitra':mitra, 'alamat':alamat}
        collection_mitra.update_one({'_id': ObjectId(id)}, {'$set': new_mitra})
        return redirect(url_for('showMitra'))
    return redirect(url_for('index'))

def hapusMitraApp(id):
    
    if 'username' in session and session['role']=='admin':
        collection_mitra.delete_one({'_id': ObjectId(id)})
        return redirect(url_for('showMitra'))
    return redirect(url_for('index'))