import tkinter as tk
cua_so = tk.Tk()
cua_so.title("Ví dụ Listbox")
cua_so.geometry("300x250")
listbox_mon_hoc = tk.Listbox(cua_so, selectmode="single")
for mon in ["Toán", "Lý", "Hóa", "Văn", "Anh"]:
    listbox_mon_hoc.insert(tk.END, mon)
listbox_mon_hoc.pack(pady=10)
def xem_mon_da_chon():
    lua_chon = listbox_mon_hoc.curselection()
    if lua_chon:
        nhan_ket_qua.config(text=f"Môn đã chọn: {listbox_mon_hoc.get(lua_chon[0])}")
tk.Button(cua_so, text="Xem môn đã chọn", command=xem_mon_da_chon).pack(pady=5)
nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()
cua_so.mainloop()

import tkinter as tk
from tkinter import ttk
cua_so = tk.Tk()
cua_so.title("Ví dụ Combobox")
cua_so.geometry("300x180")
tk.Label(cua_so, text="Chọn thành phố: ").pack(pady=10)
combobox_thanh_pho = ttk.Combobox(cua_so, values=["Hà Nội", "Đà Nẵng", "TPHCM", "Huế"])
combobox_thanh_pho.current(0)
combobox_thanh_pho.pack(pady=5)
def xem_thanh_pho():
    nhan_ket_qua.config(text=f"Bạn chọn: {combobox_thanh_pho.get()}")
tk.Button(cua_so, text="Xác nhận", command=xem_thanh_pho).pack(pady=10)
nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()
cua_so.mainloop()