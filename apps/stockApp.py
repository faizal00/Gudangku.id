from flask import session,render_template,url_for,redirect,request, flash
from config import collection_stock, collection_out, collection_mitra, collection_in
from datetime import datetime
from bson import ObjectId

def showStockApp():

    if 'username' in session and session['role'] == 'user':
        data_stock = collection_stock.find({'gudang':session['gudang']})
        data_mitra = list(collection_mitra.find())
        return render_template('/user/stock.html',mitra=data_mitra, data = data_stock, username=session['username'],role = session['role'],gudang = session['gudang'])
    return redirect(url_for('index'))

def addStockApp(id):

    if 'username' in session and session['role'] == 'user':
        nama = request.form['nama']
        kategori = request.form['kategori']
        supplier = request.form['supplier']
        satuan = request.form['satuan']
        qty_current = collection_stock.find_one({'_id': ObjectId(id)}).get('qty')
        qty_new = int(request.form['qty'])
        qty_total = qty_current+qty_new
        time = datetime.now().strftime('%d-%m-%Y - %H:%M:%S')
        new_data1 = {
            'qty':qty_total,
            'status':"Out of Stock",
            'edited':session['username'],
            'edited_time':time
        }
        new_data2 = {
            'qty':qty_total,
            'status':"Ready Stock",
            'edited':session['username'],
            'edited_time':time
        }
        if(qty_total==0):
            collection_stock.update_one({'_id': ObjectId(id)}, {'$set': new_data1})
            collection_in.insert_one({'nama': nama, 'kategori': kategori,'qty':qty_new,'satuan':satuan,'supplier':supplier,'gudang':session['gudang'],'edited':session['username'],'edited_time':time})
            return redirect(url_for('showStock'))
        else:
            collection_stock.update_one({'_id': ObjectId(id)}, {'$set': new_data2})
            collection_in.insert_one({'nama': nama, 'kategori': kategori,'qty':qty_new,'satuan':satuan,'supplier':supplier,'gudang':session['gudang'],'edited':session['username'],'edited_time':time})
            return redirect(url_for('showStock'))
    return redirect(url_for('index'))


def dropStockApp(id):
    
    if 'username' in session and session['role'] == 'user':
        nama = request.form['nama']
        kategori = request.form['kategori']
        mitra = request.form['mitra']
        satuan = request.form['satuan']
        qty_current = collection_stock.find_one({'_id': ObjectId(id)}).get('qty')
        qty_new = int(request.form['qty'])
        qty_total = qty_current-qty_new
        time = datetime.now().strftime('%d-%m-%Y - %H:%M:%S')
        new_data1 = {
            'qty':qty_total,
            'status':"Out of Stock",
            'edited':session['username'],
            'edited_time':time
        }
        new_data2 = {
            'qty':qty_total,
            'status':"Ready Stock",
            'edited':session['username'],
            'edited_time':time
        }
        if(qty_current<qty_new):
            flash('Stock tidak mencukupi!', 'error')
            return redirect(url_for('showStock'))
        elif(qty_total==0):
            collection_stock.update_one({'_id': ObjectId(id)}, {'$set': new_data1})
            collection_out.insert_one({'nama': nama, 'kategori': kategori,'qty':qty_new,'satuan':satuan,'mitra' : mitra,'gudang':session['gudang'],'edited':session['username'],'edited_time':time})
            return redirect(url_for('showStock'))
        else:
            collection_stock.update_one({'_id': ObjectId(id)}, {'$set': new_data2})
            collection_out.insert_one({'nama': nama, 'kategori': kategori,'qty':qty_new,'satuan':satuan,'mitra' : mitra,'gudang':session['gudang'],'edited':session['username'],'edited_time':time})
            return redirect(url_for('showStock'))
    return redirect(url_for('index'))

def voidStockApp(id):
        
    if 'username' in session and session['role'] == 'user':
        time = datetime.now().strftime('%d-%m-%Y - %H:%M:%S')
        new_data = {'qty':0,'status':'Out of Stock','edited':session['username'],'edited_time':time}
        collection_stock.update_one({'_id': ObjectId(id)}, {'$set': new_data})
        return redirect(url_for('showStock'))
    return redirect(url_for('index'))

