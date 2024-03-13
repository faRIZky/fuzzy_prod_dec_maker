from tkinter import *
from tkinter import ttk
import math

root = Tk()

root.title("FUZZY :^")

def myClick():
    def fuzPermintaan(permintaan, temp):
        match permintaan:
            # Naik
            case 'turun':
                if (temp <= permintaan_min):
                    return 1
                elif (temp >= permintaan_max):
                    return 0
                else:
                    # Turun (\)
                    return (permintaan_max - temp) / (permintaan_max - permintaan_min)
            # Turun
            case 'naik':
                if (temp <= permintaan_min):
                    return 0
                elif (temp >= permintaan_max):
                    return 1
                else:
                    # Naik (/)
                    return (temp - permintaan_min) / (permintaan_max - permintaan_min)

    def fuzPersediaan(persediaan, temp):
        match persediaan:
            # Sedikit
            case 'sedikit':
                if temp <= persediaan_min:
                    return 1
                elif temp >= persediaan_max:
                    return 0
                else:
                    # Turun (\)
                    return (persediaan_max - temp) / (persediaan_max - persediaan_min)
            # Banyak
            case 'banyak':
                if temp <= persediaan_min:
                    return 0
                elif temp >= persediaan_max:
                    return 1
                else:
                    # Naik (/)
                    return (temp - persediaan_min) / (persediaan_max - persediaan_min)

    def alphaProduksi(permintaan, persediaan):
        return min(permintaan, persediaan)

    def fuzProduksi(kuantitas, alpha):
        match kuantitas:
            # Berkurang
            case 'berkurang':
                zBerkurang = produksi_max - alpha * (produksi_max - produksi_min)
                return zBerkurang

            # Bertambah
            case 'bertambah':
                z_bertambah = alpha * (produksi_max - produksi_min) + produksi_min
                return z_bertambah

    def defuzz(alpha1, z1, alpha2, z2, alpha3, z3, alpha4, z4):
        numerator = ((alpha1 * z1) + (alpha2 * z2) + (alpha3 * z3) + (alpha4 * z4))
        denominator = alpha1 + alpha2 + alpha3 + alpha4

        defuzz_value = numerator / denominator

        return defuzz_value

    permintaan = int(kasus_permintaan_input.get())
    permintaan_min = int(permintaan_input_min.get())
    permintaan_max = int(permintaan_input_max.get())

    persediaan = int(kasus_persediaan_input.get())
    persediaan_min = int(persediaan_input_min.get())
    persediaan_max = int(persediaan_input_max.get())

    produksi_min = int(produksi_input_min.get())
    produksi_max = int(produksi_input_max.get())

    var_fuz_naik = fuzPermintaan('naik', permintaan)
    var_fuz_turun = fuzPermintaan('turun', permintaan)

    var_fuz_banyak = fuzPersediaan('banyak', persediaan)
    var_fuz_sedikit = fuzPersediaan('sedikit', persediaan)

    print("Nilai var_fuz_naik:", str(var_fuz_naik))
    print("Nilai var_fuz_turun:", str(var_fuz_turun))
    print("Nilai var_fuz_banyak:", str(var_fuz_banyak))
    print("Nilai var_fuz_sedikit:", str(var_fuz_sedikit))
    print()

    # Rule 1
    alpha1 = alphaProduksi(var_fuz_turun, var_fuz_banyak)
    z1 = fuzProduksi('berkurang', alpha1)

    print(f"Rule 1 \nNilai alpha : {alpha1} \nnilai z1: {z1}")
    print()

    # Rule 2
    alpha2 = alphaProduksi(var_fuz_naik, var_fuz_sedikit)
    z2 = fuzProduksi('bertambah', alpha2)

    print(f"Rule 2\nNilai alpha: {alpha2}\nnilai z2: {z2}")
    print()

    # Rule 3
    alpha3 = alphaProduksi(var_fuz_naik, var_fuz_banyak)
    z3 = fuzProduksi('bertambah', alpha3)

    print(f"Rule 3\nNilai alpha: {alpha3}\nnilai z3: {z3}")
    print()

    # Rule 4
    alpha4 = alphaProduksi(var_fuz_turun, var_fuz_sedikit)
    z4 = fuzProduksi('berkurang', alpha4)

    print(f"Rule 4\nNilai alpha: {alpha4}\nnilai z4: {z4}")
    print()

    defuzzification = math.ceil(defuzz(alpha1, z1, alpha2, z2, alpha3, z3, alpha4, z4))
    print(f"Maka produksi nya adalah {defuzzification} units")

    # Add your logic here
    result_label.config(text=f"Maka produksi nya adalah {defuzzification} units")

# Permintaan
permintaan_label = Label(root, text="Permintaan per hari:")
permintaan_label.grid(row=0, column=0)

permintaan_input_min = Entry(root, width=35, borderwidth=5)
permintaan_input_min.grid(row=1, column=0, columnspan=2, padx=(10, 5), pady=10)

permintaan_label_sampai = Label(root, text=" sampai ")
permintaan_label_sampai.grid(row=1, column=2)

permintaan_input_max = Entry(root, width=35, borderwidth=5)
permintaan_input_max.grid(row=1, column=3, columnspan=3, padx=10, pady=10)

# Persediaan
persediaan_label = Label(root, text="Persediaan per hari:")
persediaan_label.grid(row=2, column=0)

persediaan_input_min = Entry(root, width=35, borderwidth=5)
persediaan_input_min.grid(row=3, column=0, columnspan=2, padx=(10, 5), pady=10)

persediaan_label_sampai = Label(root, text=" sampai ")
persediaan_label_sampai.grid(row=3, column=2)

persediaan_input_max = Entry(root, width=35, borderwidth=5)
persediaan_input_max.grid(row=3, column=3, columnspan=3, padx=10, pady=10)

# Produksi
produksi_label = Label(root, text="Produksi per hari:")
produksi_label.grid(row=4, column=0)

produksi_input_min = Entry(root, width=35, borderwidth=5)
produksi_input_min.grid(row=5, column=0, columnspan=2, padx=(10, 5), pady=10)

produksi_label_sampai = Label(root, text=" sampai ")
produksi_label_sampai.grid(row=5, column=2)

produksi_input_max = Entry(root, width=35, borderwidth=5)
produksi_input_max.grid(row=5, column=3, columnspan=3, padx=10, pady=10)

# Separator
separator = ttk.Separator(root, orient='horizontal')
separator.grid(row=6, columnspan=6, sticky='ew', pady=10)

# Kasus
kasus_label = Label(root, text="Berapa banyak units yang harus diproduksi, jika...")
kasus_label.grid(row=7, columnspan=6, pady=5)

# Kasus Permintaan
kasus_permintaan_label = Label(root, text="Permintaan saat ini :")
kasus_permintaan_label.grid(row=8, column=0, columnspan=2, padx=(10, 5), pady=10)

kasus_permintaan_input = Entry(root, width=35, borderwidth=5)
kasus_permintaan_input.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Kasus Persediaan
kasus_persediaan_label = Label(root, text="Persediaan saat ini :")
kasus_persediaan_label.grid(row=8, column=3, columnspan=10, padx=10, pady=10)

kasus_persediaan_input = Entry(root, width=35, borderwidth=5)
kasus_persediaan_input.grid(row=9, column=3, columnspan=10, padx=10, pady=10)

# Button
myButton = Button(root, text="Submit", command=myClick)
myButton.grid(row=10, column=0, columnspan=6, padx=10, pady=10)

# Result
result_label = Label(root, text="Result: ")
result_label.grid(row=12, column=0, columnspan=6, padx= 10)

root.mainloop()
