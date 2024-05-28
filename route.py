from flask import Flask
from apps import loginApp, stockApp, userApp, kategoriApp, supplierApp, mitraApp, itemApp,mainApp,logoutApp, historyApp, gudangApp

app = Flask(__name__)
app.secret_key = 'admin'

#main route
@app.route('/',methods=['GET', 'POST'])
def index():
    return mainApp.indexApp()
    
#login route
@app.route('/login', methods=['GET', 'POST'])
def login():
  return loginApp.loginApp()

#user route
@app.route('/adduser',methods=['GET', 'POST'])
def addUser():
    return userApp.addUserApp()

@app.route('/deleteUser/<string:id>', methods=['POST'])
def hapusUser(id):
    return userApp.hapusUserApp(id)

#gudang route
@app.route('/showgudang')
def showGudang():
    return gudangApp.showGudangApp()

@app.route('/addgudang',methods=['GET', 'POST'])
def addGudang():
    return gudangApp.addGudangApp()

@app.route('/editgudang/<string:id>', methods=['POST'])
def editGudang(id):
    return gudangApp.editGudangApp(id)

@app.route('/deletegudang/<string:id>', methods=['POST'])
def hapusGudang(id):
    return gudangApp.hapusGudangApp(id)

#kategori route
@app.route('/showkategori')
def showKategori():
    return kategoriApp.showKategoriApp()

@app.route('/addkategori',methods=['GET', 'POST'])
def addKategori():
    return kategoriApp.addKategoriApp()

@app.route('/editKat/<string:id>', methods=['POST'])
def editKategori(id):
    return kategoriApp.editKategoriApp(id)

@app.route('/deleteKat/<string:id>', methods=['POST'])
def hapusKategori(id):
    return kategoriApp.hapusKategoriApp(id)

#supplier route
@app.route('/showsupplier')
def showSupplier():
    return supplierApp.showSupplierApp()

@app.route('/addsupplier',methods=['GET', 'POST'])
def addSupplier():
    return supplierApp.addSupplierApp()

@app.route('/editSup/<string:id>', methods=['POST'])
def editSupplier(id):
    return supplierApp.editSupplierApp(id)

@app.route('/deleteSup/<string:id>', methods=['POST'])
def hapusSupplier(id):
    return supplierApp.hapusSupplierApp(id)

#mitra route
@app.route('/showmitra')
def showMitra():
    return mitraApp.showMitraApp()

@app.route('/addmitra',methods=['GET', 'POST'])
def addMitra():
    return mitraApp.addMitraApp()

@app.route('/editMit/<string:id>', methods=['POST'])
def editMitra(id):
    return mitraApp.editMitraApp(id)

@app.route('/deleteMit/<string:id>', methods=['POST'])
def hapusMitra(id):
    return mitraApp.hapusMitraApp(id)

#item route
@app.route('/additem',methods=['GET', 'POST'])
def addItem():
    return itemApp.addItemApp()

@app.route('/edititem/<string:id>', methods=['POST'])
def editItem(id):
    return itemApp.editItemApp(id)

@app.route('/deleteitem/<string:id>', methods=['POST'])
def hapusItem(id):
    return itemApp.hapusItemApp(id)

#stock route
@app.route('/showstock')
def showStock():
    return stockApp.showStockApp()

@app.route('/addstock/<string:id>', methods=['POST'])
def addStock(id):
    return stockApp.addStockApp(id)

@app.route('/dropstock/<string:id>', methods=['POST'])
def dropStock(id):
    return stockApp.dropStockApp(id)

@app.route('/voidstock/<string:id>', methods=['POST'])
def voidStock(id):
    return stockApp.voidStockApp(id)

#history route
@app.route('/showin')
def showStockIn():
    return historyApp.showHistoryIn()

@app.route('/showout')
def showStockOut():
    return historyApp.showHistoryOut()

@app.route('/historyadmin')
def historyAdmin():
    return historyApp.showHistoryAdmin()

#logout route
@app.route('/logout')
def logout():
    return logoutApp.logoutApp()


