#!/usr/bin/env python

import tkinter as tk
from tkinter import ttk
import csv
import sys

def load_csv(csv_file, tree):
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        header = ["Index"] + header 
        tree["columns"] = header
        tree["show"] = "headings"
        for col in header:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")  
        rows = []
        for i, row in enumerate(reader, start=1):
            rows.append([i] + row) 
        total_rows = len(rows)
        if total_rows > 49:
            first_25 = rows[:25]
            last_25 = rows[-25:]
            for row in first_25:
                tree.insert("", tk.END, values=row)
            tree.insert("", tk.END, values=[""]*len(header), tags="separator")
            tree.insert("", tk.END, values=[""]*len(header), tags="separator")
            for row in last_25:
                tree.insert("", tk.END, values=row)
        else:
            for row in rows:
                tree.insert("", tk.END, values=row)
        tree.tag_configure("separator", background="gray")

def main(csv_file):
    root = tk.Tk()
    root.title("CSV Viewer")
    root.configure(bg="#121212")  
    ttk.Style().configure("Treeview", background="#121212", fieldbackground="#121212", foreground="#FFFFFF") 
    tree = ttk.Treeview(root)
    tree.pack(expand=True, fill=tk.BOTH)
    load_csv(csv_file, tree)
    root.attributes("-fullscreen", True)
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python csv_viewer.py <csv_file>")
    else:
        main(sys.argv[1])
