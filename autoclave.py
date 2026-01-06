def main():

    # --- DAFTAR ITEM (INDEX) ---

    TOOLS = [

        "Surgical Stitches",      # 0
        "Surgical Sponge",        # 1
        "Surgical Scalpel",       # 2
        "Surgical Anesthetic",    # 3
        "Surgical Antiseptic",    # 4
        "Surgical Antibiotics",   # 5
        "Surgical Splint",        # 6
        "Surgical Pins",          # 7
        "Surgical Transfusion",   # 8
        "Surgical Clamp",         # 9
        "Surgical Ultrasound",    # 10
        "Surgical Lab Kit",       # 11
        "Surgical Defibrillator"  # 12
    ]

    print("==============================================")

    print("   KALKULATOR AUTOCLAVE                       ")

    print("==============================================")

    #1. SETUP INVENTARIS
    inventory = {nama_tool: 0 for nama_tool in TOOLS}
    modal_awal_total = 0

    #INPUT DATA
    while True:
        print("\n--- MENU INPUT ITEM ---")
        for i, tool in enumerate(TOOLS):
            if tool == "Surgical Stitches":
                continue
            print(f"{i}. {tool}")
        print("\n88. LIHAT ISI GUDANG (CEK INVENTORY)")
        print("99. SELESAI & MULAI HITUNG")

        try:
            pilihan = int(input("\nMasukkan Pilihan (Nomor): "))
            # FITUR CEK INVENTORY
            if pilihan == 88:
                print("\n" + "="*40)
                print("       STATUS INVENTORY SAAT INI       ")
                print("="*40)

                if modal_awal_total == 0:
                    print("(Gudang masih kosong, belum ada item)")
                else:
                    for nama, jumlah in inventory.items():
                        if jumlah > 0:
                            print(f"- {nama:<25} : {jumlah}")
                    print("-" * 40)
                    print(f"TOTAL SEMUA ITEM SAMPAH: {modal_awal_total}")
                print("="*40)
                input("[Tekan Enter untuk kembali ke menu]")
                continue

            # SELESAI INPUT
            if pilihan == 99:
                if modal_awal_total == 0:
                    print("Masukan minimal satu jenis item sampah dulu!")
                    continue
                break

            # LOGIKA INPUT ITEM
            if pilihan < 1 or pilihan >= len(TOOLS):
                print("Nomor item tidak valid!")
                continue

            nama_item_dipilih = TOOLS[pilihan]

            jumlah = int(input(f"Masukkan jumlah '{nama_item_dipilih}': "))

            # Update inventory
            inventory[nama_item_dipilih] += jumlah
            modal_awal_total += jumlah
            print(f"-> Sukses! {jumlah} {nama_item_dipilih} masuk gudang.")

        except ValueError:

            print("Error: Harap masukkan angka bulat.")

    #2. PROSES LOOPING

    print("\n" + "="*50)
    print("MEMULAI PROSES AUTOCLAVE...")
    print("="*50)
    total_stit_terkumpul = 0
    total_masak = 0
    while True:
        item_bisa_dimasak = []
        for tool in TOOLS:
            if tool == "Surgical Stitches": continue
            if inventory[tool] >= 20:
                item_bisa_dimasak.append(tool)

        if not item_bisa_dimasak:
            break
        item_yang_dimasak = item_bisa_dimasak[0]
        jumlah_batch = inventory[item_yang_dimasak] // 20
        jumlah_input_hangus = jumlah_batch * 20
        inventory[item_yang_dimasak] -= jumlah_input_hangus
        for tool_output in TOOLS:
            if tool_output == item_yang_dimasak:
                continue
            jumlah_dapat = jumlah_batch * 1
            if tool_output == "Surgical Stitches":
                total_stit_terkumpul += jumlah_dapat
            else:
                inventory[tool_output] += jumlah_dapat
        total_masak += jumlah_batch

    # 3. HASIL AKHIR

    print("\n" + "="*50)
    print("LAPORAN HASIL AKHIR")
    print("="*50)
    print(f"Total Modal Awal        : {modal_awal_total}")
    print(f"TOTAL STITCHES DIDAPAT  : {total_stit_terkumpul} item")
    print("-" * 50)

    print("Sisa Sampah Mati (Tidak cukup untuk autoclave):")
    for tool in TOOLS:
        if tool != "Surgical Stitches" and inventory[tool] > 0:
            print(f"- {tool:<25} : {inventory[tool]}")

    print("-" * 50)
    print(f"Verifikasi Rumus Cepat (Total Modal / 9):")
    print(f"{modal_awal_total} / 9 = {modal_awal_total/9:.2f}")

if __name__ == "__main__":

    main()
