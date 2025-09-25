import pandas as pd

# Buat template DataFrame
data = {
    "Nama": [],
    "NIM": []
}

df = pd.DataFrame(data)

# Simpan ke file CSV (bisa juga Excel)
df.to_csv("template.csv", index=False)

print("Template berhasil dibuat: template.csv")
