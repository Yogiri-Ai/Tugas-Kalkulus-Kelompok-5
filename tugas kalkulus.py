import matplotlib.pyplot as plt

def fungsi_biaya_layanan_A(angka):
    """Menghitung biaya layanan A: Rp 100.000 + Rp 500 per GB"""
    return 100000 + 500 * angka

def fungsi_biaya_layanan_B(angka):
    """Menghitung biaya layanan B: Rp 300.000 + Rp 200 per GB"""
    return 300000 + 200 * angka

def hitung_titik_impas():
    """Menghitung titik impas dimana kedua layanan memiliki biaya sama"""
    # C_A(x) = C_B(x)
    # 100000 + 500x = 300000 + 200x
    # 500x - 200x = 300000 - 100000
    # 300x = 200000
    # x = 200000 / 300
    return 200000 / 300

def analisis_perbandingan():
    """Melakukan analisis perbandingan biaya kedua layanan"""
    titik_impas = hitung_titik_impas()
    
    print("=" * 60)
    print("ANALISIS BIAYA LAYANAN CLOUD STORAGE")
    print("=" * 60)
    print(f"Layanan A: Rp 100.000/bulan + Rp 500/GB")
    print(f"Layanan B: Rp 300.000/bulan + Rp 200/GB")
    print("=" * 60)
    
    # Analisis titik impas
    print(f"\nTITIK IMPAS (Break-even Point):")
    print(f"Kedua layanan memiliki biaya sama pada {titik_impas:.2f} GB")
    print(f"Biaya pada titik impas: Rp {fungsi_biaya_layanan_A(titik_impas):,.0f}")
    
    # Analisis area hemat
    print(f"\nREKOMENDASI PEMILIHAN:")
    print(f"• Jika penggunaan < {titik_impas:.2f} GB: Layanan A lebih hemat")
    print(f"• Jika penggunaan > {titik_impas:.2f} GB: Layanan B lebih hemat")
    print(f"• Jika penggunaan = {titik_impas:.2f} GB: Keduanya sama hematnya")
    
    return titik_impas

def input_penggunaan_user():
    """Meminta input dari user untuk analisis spesifik"""
    print("\n" + "=" * 60)
    print("ANALISIS UNTUK PENGGUNAAN SPESIFIK")
    print("=" * 60)
    
    try:
        inputan = float(input("Masukkan estimasi penggunaan storage (GB): "))
        
        biaya_A = fungsi_biaya_layanan_A(inputan)
        biaya_B = fungsi_biaya_layanan_B(inputan)
        
        print(f"\nHasil Analisis untuk {inputan} GB:")
        print(f"Biaya Layanan A: Rp {biaya_A:,.0f}")
        print(f"Biaya Layanan B: Rp {biaya_B:,.0f}")
        
        if biaya_A < biaya_B:
            selisih = biaya_B - biaya_A
            print(f"✓ REKOMENDASI: Pilih Layanan A (lebih hemat Rp {selisih:,.0f})")
        elif biaya_B < biaya_A:
            selisih = biaya_A - biaya_B
            print(f"✓ REKOMENDASI: Pilih Layanan B (lebih hemat Rp {selisih:,.0f})")
        elif biaya_A == biaya_B:
            selisih = biaya_A - biaya_B
            print("Layanan A dan Layanan B sama {selisih:,.0f}")
        else:
            print(f"✓ REKOMENDASI: Kedua layanan sama hematnya")
            
        return inputan
        
    except ValueError:
        print("Error: Masukkan angka yang valid untuk GB")
        return None

def buat_grafik(titik_impas, gb_user=None):
    """Membuat grafik perbandingan biaya kedua layanan"""
    # Generate data points
    gb_min = 0
    gb_max = max(1000, titik_impas * 1.5)  # Sesuaikan range grafik
    
    # Buat list titik-titik untuk plotting
    gb_values = []
    for i in range(0, int(gb_max) + 100, 100):  # Step 100 GB
        gb_values.append(i)
    
    # Hitung biaya untuk setiap titik
    biaya_A_values = [fungsi_biaya_layanan_A(x) for x in gb_values]
    biaya_B_values = [fungsi_biaya_layanan_B(x) for x in gb_values]
    
    # Buat plot
    plt.figure(figsize=(12, 8))
    
    # Plot garis biaya
    plt.plot(gb_values, biaya_A_values, 'b-', linewidth=2, label='Layanan A: Rp 100.000 + Rp 500/GB') # " 'b' = blue, '-' = garis " | "linewidh = ketebalan garis"
    plt.plot(gb_values, biaya_B_values, 'r-', linewidth=2, label='Layanan B: Rp 300.000 + Rp 200/GB') # label = nmenampilkan di grafik
    
    # Plot titik impas
    biaya_impas = fungsi_biaya_layanan_A(titik_impas)
    plt.plot(titik_impas, biaya_impas, 'go', markersize=8, label=f'Titik Impas ({titik_impas:.1f} GB)') # "'g' = green, 'o' = lingkaran"
    
    # Plot titik penggunaan user jika ada
    if gb_user is not None:
        biaya_user_A = fungsi_biaya_layanan_A(gb_user)
        biaya_user_B = fungsi_biaya_layanan_B(gb_user)
        plt.plot(gb_user, biaya_user_A, 'bo', markersize=6, label=f'Penggunaan Anda - A ({gb_user} GB)')
        plt.plot(gb_user, biaya_user_B, 'ro', markersize=6, label=f'Penggunaan Anda - B ({gb_user} GB)')
    
    # Area shading untuk menunjukkan area hemat
    gb_area = [x for x in gb_values if x <= gb_max]
    biaya_A_area = [fungsi_biaya_layanan_A(x) for x in gb_area if x <= titik_impas]
    gb_area_A = [x for x in gb_area if x <= titik_impas]
    
    biaya_B_area = [fungsi_biaya_layanan_B(x) for x in gb_area if x >= titik_impas]
    gb_area_B = [x for x in gb_area if x >= titik_impas]
    
    plt.fill_between(gb_area_A, biaya_A_area, alpha=0.2, color='blue', label='Area Hemat Layanan A')
    plt.fill_between(gb_area_B, biaya_B_area, alpha=0.2, color='red', label='Area Hemat Layanan B')
    
    # Konfigurasi grafik
    plt.xlabel('Penggunaan Storage (GB)', fontsize=12)
    plt.ylabel('Biaya Bulanan (Rupiah)', fontsize=12)
    plt.title('Perbandingan Biaya Layanan Cloud Storage', fontsize=14, fontweight='bold')
    
    # Format y-axis dengan separator ribuan
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'Rp {x:,.0f}'))
    
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    
    # Tampilkan grafik
    plt.show()

def main():
    """Program utama"""
    print("PROGRAM ANALISIS LAYANAN CLOUD STORAGE")
    print("=" * 50)
    
    # Analisis umum
    titik_impas = analisis_perbandingan()
    
    # Input dari user
    gb_user = input_penggunaan_user()
    
    # Tampilkan grafik
    print(f"\nMenampilkan grafik perbandingan...")
    buat_grafik(titik_impas, gb_user)
    
    # Tampilkan kesimpulan akhir
    print("\n" + "=" * 60)
    print("KESIMPULAN AKHIR")
    print("=" * 60)
    print("Berdasarkan analisis cost-analysis dan Total Cost of Ownership (TCO):")
    print(f"• Break-even point: {titik_impas:.2f} GB")
    print(f"• Untuk startup dengan penggunaan rendah: Layanan A lebih ekonomis")
    print(f"• Untuk startup dengan penggunaan tinggi: Layanan B lebih ekonomis")
    print(f"• Pertimbangkan juga faktor lain seperti keandalan dan fitur tambahan")

if __name__ == "__main__":
    main()
