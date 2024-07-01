from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import math

app = Flask(__name__)

# Konfigurasi MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'spk-topsis'
mysql = MySQL(app)

@app.route("/index")
def index():
    return render_template('index.html')

# Alternatif
@app.route("/alternative")  # Menampilkan Data
def alternative():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM alternative")
    alternative = cur.fetchall()
    cur.close()
    return render_template('alternative.html', data=alternative)

@app.route("/simpanalternative", methods=["GET", "POST"])  # Menyimpan data
def simpanalternative():
    if request.method == 'POST':
        merek = request.form['merek']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO alternative(merek) VALUES (%s)", (merek,))
        mysql.connection.commit()
        cur.close()
        return "<script>alert('Data berhasil ditambahkan'); window.location.href='/alternative';</script>"
    else:
        return "<script>alert('Gagal input'); window.location.href='/alternative';</script>"

@app.route("/delete_alternative/<_id>")  # Menghapus data
def deletealternative(_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM alternative WHERE id = %s", (_id,))
    mysql.connection.commit()
    cur.close()
    return "<script>alert('Data berhasil dihapus'); window.location.href='/alternative';</script>"

@app.route("/edit_alternative/<_id>")  # Mengedit data
def edit_alternative(_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM alternative WHERE id = %s", (_id,))
    alternative = cur.fetchone()
    cur.close()
    return render_template('edit_alternative.html', data=alternative)

@app.route("/editalternative", methods=["POST"])
def editalternative():
    if request.method == 'POST':
        _id = request.form.get('id')
        _merek = request.form.get('merek')
        cur = mysql.connection.cursor()
        cur.execute("UPDATE alternative SET merek=%s WHERE id=%s", (_merek, _id))
        mysql.connection.commit()
        cur.close()
        return "<script>alert('Data berhasil diedit'); window.location.href='/alternative';</script>"
    else:
        return "<script>alert('Gagal input');</script>"

@app.route("/kriteria")
def kriteria():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM kriteria")
    kriteria = cur.fetchall()
    cur.close()
    return render_template('kriteria.html', data=kriteria)

@app.route("/simpankriteria", methods=["GET", "POST"])
def simpankriteria():
    if request.method == 'POST':
        _ram = request.form.get('ram')
        _ssd = request.form.get('ssd')
        _processor = request.form.get('processor')
        _ukuran_layar = request.form.get('ukuran_layar')
        _harga = request.form.get('harga')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO kriteria(ram, ssd, processor, ukuran_layar, harga) VALUES (%s,%s,%s,%s,%s)", (_ram, _ssd, _processor, _ukuran_layar, _harga))
        mysql.connection.commit()
        cur.close()
        return "<script>alert('Data berhasil ditambahkan'); window.location.href='/kriteria';</script>"
    else:
        return "<script>alert('Gagal input'); window.location.href='/kriteria';</script>"

@app.route("/delete_kriteria/<_id>")
def deletekriteria(_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM kriteria WHERE id = %s", (_id,))
    mysql.connection.commit()
    cur.close()
    return "<script>alert('Data berhasil dihapus'); window.location.href='/kriteria';</script>"

@app.route('/penilaian', methods=['GET'])
def penilaian():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM alternative")
    alternatives = cur.fetchall()

    cur.execute("SELECT * FROM penilaian")
    penilaian_data = cur.fetchall()
    cur.close()

    return render_template('penilaian.html', alternatives=alternatives, penilaian_data=penilaian_data)

@app.route('/simpanpenilaian', methods=['POST'])
def simpanpenilaian():
    if request.method == "POST":
        _merek = request.form.get("merek")
        _ram = request.form.get("ram")
        _ssd = request.form.get("ssd")
        _processor = request.form.get("processor")
        _ukuran_layar = request.form.get("ukuran_layar")
        _harga = request.form.get("harga")

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM penilaian WHERE merek = %s", (_merek,))
        existing = cur.fetchone()

        if existing:
            return "<script>alert('Data Merek Sudah dinilai'); window.location.href='/penilaian';</script>"
        else:
            cur.execute("INSERT INTO penilaian (merek, ram, ssd, processor, ukuran_layar, harga) VALUES (%s, %s, %s, %s, %s, %s)",
                        (_merek, _ram, _ssd, _processor, _ukuran_layar, _harga))
            mysql.connection.commit()
            cur.close()
            return "<script>alert('Data berhasil ditambahkan'); window.location.href='/penilaian';</script>"
    else:
        return "<script>alert('Gagal input'); window.location.href='/penilaian';</script>"

@app.route("/delete_penilaian/<_id>")
def deletepenilaian(_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM penilaian WHERE id = %s", (_id,))
    mysql.connection.commit()
    cur.close()
    return "<script>alert('Data berhasil dihapus'); window.location.href='/penilaian';</script>"

@app.route("/edit_penilaian/<_id>")  # Mengedit data
def edit_penilaian(_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM penilaian WHERE id = %s", (_id,))
    penilaian = cur.fetchone()
    cur.close()
    return render_template('edit_penilaian.html', data=penilaian)

@app.route("/editpenilaian", methods=["POST"])
def editpenilaian():
    if request.method == 'POST':
        _id = request.form.get('id')
        _ram = request.form.get("ram")
        _ssd = request.form.get("ssd")
        _processor = request.form.get("processor")
        _ukuran_layar = request.form.get("ukuran_layar")
        _harga = request.form.get("harga")
        cur = mysql.connection.cursor()
        cur.execute("UPDATE penilaian SET ram=%s, ssd=%s, processor=%s, ukuran_layar=%s, harga=%s WHERE id=%s", (_ram, _ssd, _processor, _ukuran_layar, _harga, _id))
        mysql.connection.commit()
        cur.close()
        return "<script>alert('Data berhasil diedit'); window.location.href='/penilaian';</script>"
    else:
        return "<script>alert('Gagal input diedit');</script>"


@app.route('/proses', methods=['GET', 'POST'])
def proses():
    if request.method == 'POST':
        merek = request.form['merek']
        # Proses simpan data di sini

    cur = mysql.connection.cursor()

    # Nilai Matriks
    cur.execute("SELECT id, merek, ram, ssd, processor, ukuran_layar, harga FROM penilaian")
    penilaian = cur.fetchall()
    nilaimatriks = []
    for row in penilaian:
        nilaimatriks.append({
            'no': row[0],
            'merek': row[1],
            'ram': row[2],
            'ssd': row[3],
            'processor': row[4],
            'ukuran_layar': row[5],
            'harga': row[6]
        })
    
    # Penghitungan pembagi untuk masing-masing kriteria
    def calculate_pembagi(kriteria):
        cur.execute(f"SELECT {kriteria} FROM penilaian")
        hasil = sum(pow(float(row[0]), 2) for row in cur)
        return round(pow(hasil, 0.5), 3)

    pembagi1 = calculate_pembagi('ram')
    pembagi2 = calculate_pembagi('ssd')
    pembagi3 = calculate_pembagi('processor')
    pembagi4 = calculate_pembagi('ukuran_layar')
    pembagi5 = calculate_pembagi('harga')

    # Matriks Ternormalisasi
    matriks_ternormalisasi = []
    no = 1
    for row in penilaian:
        matriks_ternormalisasi.append({
            'no': no,
            'merek': row[1],
            'ram': round(float(row[2]) / pembagi1, 3),
            'ssd': round(float(row[3]) / pembagi2, 3),
            'processor': round(float(row[4]) / pembagi3, 3),
            'ukuran_layar': round(float(row[5]) / pembagi4, 3),
            'harga': round(float(row[6]) / pembagi5, 3)
        })
        no += 1
    # Debug print
    print("Matriks ternomalisasi " , matriks_ternormalisasi)
    

    # Penghitungan Bobot Ternormalisasi
    cur.execute("SELECT * FROM kriteria")
    kriteria = cur.fetchone()
    c1, c2, c3, c4, c5 = map(float, kriteria[1:6])

    # Insert Matriks Terbobot
    cur.execute("TRUNCATE TABLE matriks_terbobot")
    for item in matriks_ternormalisasi:
        c1_value = round(item['ram'] * c1, 3)
        c2_value = round(item['ssd'] * c2, 3)
        c3_value = round(item['processor'] * c3, 3)
        c4_value = round(item['ukuran_layar'] * c4, 3)
        c5_value = round(item['harga'] * c5, 3)
        cur.execute(
            "INSERT INTO matriks_terbobot (merek, c1, c2, c3, c4, c5) VALUES (%s, %s, %s, %s, %s, %s)",
            (item['merek'], c1_value, c2_value, c3_value, c4_value, c5_value)
        )
    mysql.connection.commit()

    cur.execute("SELECT * FROM matriks_terbobot")
    matriks_terbobot = cur.fetchall()
    
    # Debug print
    print("matriks terbobot" , matriks_terbobot)

    # Matriks Ideal Positif (Max)
    cur.execute("SELECT MAX(c1), MAX(c2), MAX(c3), MAX(c4), MIN(c5) FROM matriks_terbobot")
    positif = cur.fetchone()

    # Matriks Ideal Negatif (Min)
    cur.execute("SELECT MIN(c1), MIN(c2), MIN(c3), MIN(c4), MAX(c5) FROM matriks_terbobot")
    negatif = cur.fetchone()

    # Debug print
    print("positif", positif)
    print("negatif " ,negatif)

    # Jarak Solusi Ideal Positif (D+)
    jarak_positif = [
        {
            'no': i+1,
            'merek': row[1],
            'd_plus': "{:.3f}".format(math.sqrt(
                sum(pow(float(row[j+2]) - float(positif[j]), 2) for j in range(5))
            ))
        }
        for i, row in enumerate(matriks_terbobot)
    ]
    # Debug print
    print("jarak positif " , jarak_positif)

    # Jarak Solusi Ideal Negatif (D-)
    jarak_negatif = [
        {
            'no': i+1,
            'merek': row[1],
            'd_minus': "{:.3f}".format(math.sqrt(
                sum(pow(float(row[j+2]) - float(negatif[j]), 2) for j in range(5))
            ))
        }
        for i, row in enumerate(matriks_terbobot)
    ]
    # Debug print
    print("jarak Negatif " , jarak_negatif)
    
    # Nilai Preferensi
    cur.execute("TRUNCATE TABLE preferensi")
    for row in matriks_terbobot:
        d_plus = math.sqrt(sum(pow(float(row[j+2]) - float(positif[j]), 2) for j in range(5)))
        d_minus = math.sqrt(sum(pow(float(row[j+2]) - float(negatif[j]), 2) for j in range(5)))
        nilai_preferensi = d_minus / (d_minus + d_plus)
        nilai_preferensi_formatted = "{:.3f}".format(nilai_preferensi)
        cur.execute("INSERT INTO preferensi (merek, nilai_preferensi) VALUES (%s, %s)", (row[1], nilai_preferensi_formatted))

    cur.execute("SELECT * FROM preferensi ORDER BY nilai_preferensi DESC")
    preferensi = cur.fetchall()
    # Debug print
    print("Nilai preferensi " , preferensi)

    return render_template('proses.html', nilaimatriks=nilaimatriks, matriks_ternormalisasi=matriks_ternormalisasi,
                           matriks_terbobot=matriks_terbobot, positif=positif, negatif=negatif,
                           jarak_positif=jarak_positif, jarak_negatif=jarak_negatif, preferensi=preferensi)

if __name__ == '__main__':
    app.run(debug=True)
