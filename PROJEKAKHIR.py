import tkinter as tk
planet_distances = {
    "Merkurius": 57.9,
    "Venus": 108.2,
    "Bumi": 149.6,
    "Mars": 227.9,
    "Jupiter": 778.3,
    "Saturnus": 1427,
    "Uranus": 2871,
    "Neptunus": 4497.1
}

def hitung_jarak():
    planet1 = pilihan1.get()
    planet2 = pilihan2.get()
    if planet1 == planet2:
        hasil.set("Pilih dua planet yang berbeda.")
    else:
        jarak = abs(planet_distances[planet1] - planet_distances[planet2])
        hasil.set(f"Jarak antara {planet1} dan {planet2} adalah {jarak:.1f} juta km.")


root = tk.Tk()
root.title("Kalkulator Jarak Antar Planet")
root.geometry("400x250")

tk.Label(root, text="Pilih Planet Pertama:").pack(pady=5)
pilihan1 = tk.StringVar(root)
pilihan1.set("Bumi")
tk.OptionMenu(root, pilihan1, *planet_distances.keys()).pack()

tk.Label(root, text="Pilih Planet Kedua:").pack(pady=5)
pilihan2 = tk.StringVar(root)
pilihan2.set("Mars")
tk.OptionMenu(root, pilihan2, *planet_distances.keys()).pack()

tk.Button(root, text="Hitung Jarak", command=hitung_jarak).pack(pady=10)

hasil = tk.StringVar()
tk.Label(root, textvariable=hasil, font=("Helvetica", 12, "bold"), fg="blue").pack(pady=10)

root.mainloop()