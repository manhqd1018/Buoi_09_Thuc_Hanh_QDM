import tkinter as tk
root = tk.Tk()
root.title("Máy tính bỏ túi")
root.geometry("300x400")
root.resizable(False, False)
bieu_thuc = ""
bien_hien_thi = tk.StringVar()
def bam_nut(gia_tri):
    global bieu_thuc
    bieu_thuc += str(gia_tri)
    bien_hien_thi.set(bieu_thuc)
def tinh_ket_qua():
    global bieu_thuc
    try:
        ket_qua = str(eval(bieu_thuc))
        bien_hien_thi.set(ket_qua)
        bieu_thuc = ket_qua
    except Exception:
        bien_hien_thi.set("Lỗi")
        bieu_thuc = ""
def xoa_man_hinh():
    global bieu_thuc
    bieu_thuc = ""
    bien_hien_thi.set("")
man_hinh = tk.Entry(
    root, 
    textvariable=bien_hien_thi, 
    font=("Arial", 20), 
    justify="right", 
    bd=10, 
    relief=tk.FLAT
)
man_hinh.pack(fill="x", padx=10, pady=10)
khu_vuc_nut = tk.Frame(root)
khu_vuc_nut.pack()
danh_sach_nut = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]
for ten, hang, cot in danh_sach_nut:
    if ten == '=':
        btn = tk.Button(
            khu_vuc_nut, 
            text=ten, 
            width=5, 
            height=2, 
            font=("Arial", 14), 
            command=tinh_ket_qua
        )
    elif ten == 'C':
        btn = tk.Button(
            khu_vuc_nut, 
            text=ten, 
            width=5, 
            height=2, 
            font=("Arial", 14), 
            command=xoa_man_hinh
        )
    else:
        btn = tk.Button(
            khu_vuc_nut, 
            text=ten, 
            width=5, 
            height=2, 
            font=("Arial", 14), 
            command=lambda val=ten: bam_nut(val)
        )    
    btn.grid(row=hang, column=cot, padx=5, pady=5)
root.mainloop()