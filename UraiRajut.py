#soal 3 urai dan rajut
def urai(kata):
    simpen ='' #bikin tempat variable
    for i in range (len(kata)): #untuk i yg ada di range parameter function maka 
        simpen += kata[:i+1] #variable simpan ditambah dengan str[:i+1] di mana yg diambil adalah i+1 index dr blkg ke dpn 
    return simpen #print variable simpen
print(urai('Code'))
print(urai('Python'))
def rajut(kata): 
    hasil = '' #variable kosong dg nama hasil
    sementara = 0 #ini untuk nantinya tau index brp yg nti di tambah ke variable hasil
    step = 2 # ini nanti stepnya yg akan ditambahin karna logicny adalah 0,2,5,9,14,dll (bilangan segitiga)
    for i in range(len(kata)): #for I yg ada di range 0,panjang dr kata maka (jika tidak ada 0,len jg gpp karna perhitungan default python mulai dr 0)  
        if i == sementara: #bikin kondisi jika i itu hasilnya sama dg sementara , maka lanjut co: for i (0). if 0 == 0 maka
            hasil+= kata[i] # parameter kata di index i (co: 0 ) ditambahkan 
            sementara+=step #kemudian var sementara yg 0 ditambah dg step 2 supaya bisa bil segitga
            step+=1 #kemudian step ditambah 1
    return hasil #menampilkan hasil
print(rajut('CCoCodCode')) #mencetak fungsi rajut dengan parameter 'ccocodcode'
print(rajut('PPyPytPythPythoPython'))