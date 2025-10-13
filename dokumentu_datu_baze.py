import sqlite3
import os
import subprocess
from tkinter import Tk, Label, Button, Listbox, filedialog, END, messagebox

# --- Подключение к базе ---
conn = sqlite3.connect("documents.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS documents_blob (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    filedata BLOB
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS documents_path (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    filepath TEXT
)
""")
conn.commit()

# --- Список временных файлов для очистки ---
temp_files = []

# --- Функции для работы с базой ---
def save_word_as_blob(path):
    filename = os.path.basename(path)
    with open(path, 'rb') as f:
        data = f.read()
    cursor.execute("INSERT INTO documents_blob (filename, filedata) VALUES (?, ?)", (filename, data))
    conn.commit()
    messagebox.showinfo("Успех", f"Файл '{filename}' сохранён в базе как BLOB.")
    refresh_file_list()


def save_word_as_path(path):
    filename = os.path.basename(path)
    cursor.execute("INSERT INTO documents_path (filename, filepath) VALUES (?, ?)", (filename, os.path.abspath(path)))
    conn.commit()
    messagebox.showinfo("Успех", f"Путь к файлу '{filename}' сохранён в базе.")
    refresh_file_list()


def restore_file():
    selected = file_list.curselection()
    if not selected:
        messagebox.showwarning("Внимание", "Выберите файл из списка")
        return
    idx = selected[0]
    doc_id = file_ids[idx]
    if doc_id is None:
        messagebox.showwarning("Внимание", "Выбран файл, который хранится только как путь")
        return

    cursor.execute("SELECT filename, filedata FROM documents_blob WHERE id = ?", (doc_id,))
    row = cursor.fetchone()
    if row:
        filename = row[0]
        save_path = filedialog.asksaveasfilename(defaultextension=".docx", initialfile=filename)
        if save_path:
            with open(save_path, 'wb') as f:
                f.write(row[1])
            messagebox.showinfo("Успех", f"Файл восстановлен как '{save_path}'")
    else:
        messagebox.showerror("Ошибка", "Файл не найден в базе BLOB")


def open_file(event):
    """Открывает файл двойным кликом"""
    idx = file_list.curselection()
    if not idx:
        return
    idx = idx[0]
    doc_id = file_ids[idx]
    label = file_list.get(idx)
    
    if label.startswith("[BLOB]"):
        # Для BLOB создаём временный файл и открываем
        cursor.execute("SELECT filename, filedata FROM documents_blob WHERE id = ?", (doc_id,))
        row = cursor.fetchone()
        if row:
            filename, data = row
            tmp_path = os.path.join(os.getcwd(), f"tmp_{filename}")
            with open(tmp_path, 'wb') as f:
                f.write(data)
            temp_files.append(tmp_path)  # сохраняем для удаления при выходе
            open_with_default_program(tmp_path)
        else:
            messagebox.showerror("Ошибка", "Файл не найден в базе BLOB")
    elif label.startswith("[PATH]"):
        # Для PATH открываем по пути
        cursor.execute("SELECT filepath FROM documents_path WHERE id = ?", (doc_id,))
        row = cursor.fetchone()
        if row and os.path.exists(row[0]):
            open_with_default_program(row[0])
        else:
            messagebox.showerror("Ошибка", "Файл не найден по указанному пути")


def open_with_default_program(path):
    """Кроссплатформенное открытие файла"""
    try:
        if os.name == 'nt':  # Windows
            os.startfile(path)
        elif os.name == 'posix':  # Mac / Linux
            subprocess.call(('xdg-open', path))
        else:
            messagebox.showinfo("Info", f"Откройте файл вручную: {path}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось открыть файл: {e}")


def delete_file():
    """Удаляет выбранный файл из базы"""
    selected = file_list.curselection()
    if not selected:
        messagebox.showwarning("Внимание", "Выберите файл из списка")
        return
    idx = selected[0]
    doc_id = file_ids[idx]
    label = file_list.get(idx)
    
    if messagebox.askyesno("Подтверждение", f"Удалить {label}?"):
        if label.startswith("[BLOB]"):
            cursor.execute("DELETE FROM documents_blob WHERE id = ?", (doc_id,))
        elif label.startswith("[PATH]"):
            cursor.execute("DELETE FROM documents_path WHERE id = ?", (doc_id,))
        conn.commit()
        messagebox.showinfo("Удалено", f"{label} удалён из базы.")
        refresh_file_list()


def refresh_file_list():
    file_list.delete(0, END)
    global file_ids
    file_ids = []

    cursor.execute("SELECT id, filename FROM documents_blob")
    for row in cursor.fetchall():
        file_list.insert(END, f"[BLOB] {row[1]}")
        file_ids.append(row[0])

    cursor.execute("SELECT id, filename FROM documents_path")
    for row in cursor.fetchall():
        file_list.insert(END, f"[PATH] {row[1]}")
        file_ids.append(row[0])


def add_file_blob():
    path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
    if path:
        save_word_as_blob(path)


def add_file_path():
    path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
    if path:
        save_word_as_path(path)


def cleanup_temp_files():
    """Удаляет все временные файлы BLOB при выходе"""
    for f in temp_files:
        try:
            if os.path.exists(f):
                os.remove(f)
        except Exception as e:
            print(f"Не удалось удалить временный файл {f}: {e}")


# --- GUI ---
root = Tk()
root.title("Word Database Manager")

Label(root, text="Список документов:").pack()

file_list = Listbox(root, width=50)
file_list.pack(padx=10, pady=5)
file_list.bind("<Double-Button-1>", open_file)  # двойной клик

Button(root, text="Добавить файл в BLOB", command=add_file_blob).pack(fill='x', padx=10, pady=2)
Button(root, text="Добавить файл как путь", command=add_file_path).pack(fill='x', padx=10, pady=2)
Button(root, text="Восстановить выбранный файл (только BLOB)", command=restore_file).pack(fill='x', padx=10, pady=2)
Button(root, text="Удалить выбранный файл", command=delete_file).pack(fill='x', padx=10, pady=2)

refresh_file_list()

# --- Обработка закрытия окна ---
def on_closing():
    cleanup_temp_files()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
