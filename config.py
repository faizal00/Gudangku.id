from pymongo import MongoClient

try:
    URI = MongoClient('mongodb+srv://faizalrmdn01:Faizal00-@cluster0.kdgybhh.mongodb.net/')
    db = URI['db_project']
    collection_user = db['users']
    collection_gudang = db['gudang']
    collection_item = db['items']
    collection_stock = db['stock']
    collection_out = db['stock_out']
    collection_in = db['stock_in']
    collection_kategori = db['kategori']
    collection_supplier = db['supplier']
    collection_mitra = db['mitra']
    print("Koneksi Berhasil")
except Exception as e:
    print("Koneksi Gagal!")