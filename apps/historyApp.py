from flask import session,redirect,url_for,render_template
from config import collection_in,collection_out

def showHistoryIn():

    if 'username' in session and session['role'] == 'user':
        data_in = collection_in.find({'gudang':session['gudang']})
        return render_template('/user/logStockIn.html', data = data_in, username=session['username'],role = session['role'], gudang=session['gudang'])
    return redirect(url_for('index'))

def showHistoryOut():
    
    if 'username' in session and session['role'] == 'user':
        data_out = collection_out.find({'gudang':session['gudang']})
        return render_template('/user/logStockOut.html', data = data_out, username=session['username'],role = session['role'],gudang=session['gudang'])
    return redirect(url_for('index'))


def showHistoryAdmin():
    
    if 'username' in session and session['role'] == 'admin':
        data_out = collection_out.find()
        data_in = collection_in.find()
        return render_template('/adm/history.html',dataIn=data_in, dataOut = data_out, username=session['username'],role = session['role'])
    return redirect(url_for('index'))