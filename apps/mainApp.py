from flask import  render_template, redirect, url_for, session
from config import collection_user,collection_item,collection_kategori, collection_supplier, collection_gudang

def indexApp():
    
    if 'username' in session and session['role'] == 'admin':
        data_user = list(collection_user.find())
        data_gudang = list(collection_gudang.find())
        return render_template('/adm/index.html',data=data_user,gudang = data_gudang, username=session['username'],role = session['role'])
    elif 'username' in session and session['role'] == 'user':
        user = collection_user.find_one({'username': session['username']})
        session['gudang']= user['gudang']
        data_item = list(collection_item.find({'gudang':session['gudang']}))
        data_kategori = list(collection_kategori.find())
        data_supplier = list(collection_supplier.find())
        return render_template('/user/index.html',supplier = data_supplier,kategori = data_kategori,data=data_item, username=session['username'],role = session['role'], gudang=session['gudang'])
    return redirect(url_for('login'))