from flask import session,redirect,url_for

def logoutApp():
    session.pop('username', None)
    session.pop('role', None)
    session.pop('gudang', None)
    return redirect(url_for('login'))