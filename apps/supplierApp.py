from flask import redirect, render_template, session,url_for, request, flash
from config import collection_supplier
from bson import ObjectId

def showSupplierApp():

    if 'username' in session and session['role'] == 'admin':
        data_supplier = collection_supplier.find()
        return render_template('/adm/supplier.html', supplier = data_supplier, username=session['username'],role = session['role'])
    return redirect(url_for('index'))

def addSupplierApp():

    if 'username' in session and session['role'] == 'admin':
        supplier = request.form['supplier']
        alamat = request.form['alamat']
        if(collection_supplier.find_one({'supplier':supplier})):
            flash('Data Sudah Ada!', 'error')
            return redirect(url_for('showSupplier'))
        else:
            collection_supplier.insert_one({'supplier': supplier,'alamat':alamat})
            return redirect(url_for('showSupplier'))
    return redirect(url_for('index'))

def editSupplierApp(id):
    
    if 'username' in session and session['role'] == 'admin':
        supplier = request.form['supplier']
        alamat = request.form['alamat']
        new_supplier = {'supplier':supplier,'alamat':alamat}
        collection_supplier.update_one({'_id': ObjectId(id)}, {'$set': new_supplier})
        return redirect(url_for('showSupplier'))
    return redirect(url_for('index'))

def hapusSupplierApp(id):
    
    if 'username' in session and session['role'] == 'admin':
        collection_supplier.delete_one({'_id': ObjectId(id)})
        return redirect(url_for('showSupplier'))
    return redirect(url_for('index'))