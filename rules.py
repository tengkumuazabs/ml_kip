def evaluate_applicant(row):
    # Dokumen wajib dan labelnya
    required_fields = {
        'KTP': row['KTP'],
        'Akte Lahir': row['Akte Lahir'],
        'Kartu Keluarga': row['Kartu Keluarga'],
        'SKTM (Surat Keterangan Tidak Mampu)': row['SKTM (Surat Keterangan Tidak Mampu)'],
        'Foto Rumah': row['Foto Rumah'],
        'Ijazah/SKL SMA': row['Ijazah/SKL SMA'],
        'Pas Foto 3x4': row['Pas Foto 3x4'],
        'Bukti Penghasilan': row['Bukti Penghasilan'],
        'Rekening Listrik': row['Rekening Listrik'],
        'Screenshot Diterima PTN/PTS': row['Screenshot Diterima PTN/PTS '],
    }

    # Cari dokumen yang tidak lengkap
    missing_docs = [doc for doc, present in required_fields.items() if not present]

    if missing_docs:
        return f"TIDAK LOLOS: Dokumen wajib tidak lengkap: {', '.join(missing_docs)}"

    # Nilai raport + nilai UN
    if ((row['Nilai Raport'] + row['Nilai UN (SHUN)']) / 2) < 80:
        return "TIDAK LOLOS: Nilai di bawah 80."

    # Syarat ekonomi (minimal salah satu)
    ekonomi_ok = (
        row['KKS (Kartu Keluarga Sejahtera)'] or
        row['PKH (Penerima Keluarga Harapan)']
    )

    if not ekonomi_ok:
        return "TIDAK LOLOS: Tidak ada dokumen bantuan sosial yang valid."

    return "LOLOS"
