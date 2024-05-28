from flask import redirect,request,url_for, session, flash
from datetime import datetime
from config import collection_item,collection_stock
from bson import ObjectId

def addItemApp():
        
    if 'username' in session and session['role'] == 'user':
        nama = request.form['nama']
        kategori = request.form['kategori']
        satuan = request.form['satuan']
        supplier = request.form['supplier']
        time = datetime.now().strftime('%d-%m-%Y - %H:%M:%S')
        if(collection_item.find_one({'nama':nama})):
            flash('Data Sudah Ada!', 'error')
            return redirect(url_for('index'))
        elif(nama == "" or kategori == "" or satuan == "" or supplier==""):
            flash('Data Tidak Boleh Kosong!', 'error')
            return redirect(url_for('index'))
        else:
            collection_item.insert_one({'nama': nama, 'kategori': kategori,'satuan':satuan,'supplier':supplier,'gudang':session['gudang'],'edited':session['username'],'edited_time':time})
            collection_stock.insert_one({'nama': nama, 'kategori': kategori,'qty':0,'satuan':satuan,'status':"-",'supplier':supplier,'gudang':session['gudang'], 'edited':"", 'edited_time':""})
            return redirect(url_for('index'))
    return redirect(url_for('index'))

def editItemApp(id):

    if 'username' in session and session['role'] == 'user':
        item = collection_item.find_one({'_id': ObjectId(id)})
        item_name = item.get('nama')

        nama = request.form['nama']
        kategori = request.form['kategori']
        satuan = request.form['satuan']
        supplier = request.form['supplier']
        time = datetime.now().strftime('%d-%m-%Y - %H:%M:%S')
        new_data1 = {'nama': nama, 'kategori': kategori,'satuan':satuan,'supplier':supplier,'edited':session['username'],'edited_time':time}
        new_data2 = {'nama': nama, 'kategori': kategori,'satuan':satuan,'supplier':supplier}

        if(nama == "" or kategori == "" or satuan == "" or supplier==""):
            flash('Data Tidak Boleh Kosong!', 'error')
            return redirect(url_for('index'))
        else:
            collection_item.update_one({'_id': ObjectId(id)}, {'$set': new_data1})
            collection_stock.update_one({'nama':item_name}, {'$set': new_data2})
            return redirect(url_for('index'))
    return redirect(url_for('index'))

def hapusItemApp(id):
    
    if 'username' in session and session['role'] == 'user':
        item = collection_item.find_one({'_id': ObjectId(id)})
        item_name = item.get('nama')

        collection_stock.delete_one({'nama':item_name})
        collection_item.delete_one({'_id': ObjectId(id)})
        return redirect(url_for('index'))
    return redirect(url_for('index'))