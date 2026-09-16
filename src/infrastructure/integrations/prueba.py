# Interfaces
import tkinter as tk

# Funcionalidad 
import subprocess;
import os;

def code_rustdesk()->str:
    
    PATH_RUSTDESK = "C:\\Program Files\\RustDesk";

    if not os.path.exists(PATH_RUSTDESK):
        return "No tiene rustdesk instalado";

    rustdesk_code = subprocess.run([f"{PATH_RUSTDESK}\\{"rustdesk.exe"}", "--get-id", "|", "more"], check=True, capture_output=True);
    rustdesk_code = rustdesk_code.stdout.decode("utf-8");
    rustdesk_code_clean = rustdesk_code.replace("\n", "")
    print(rustdesk_code_clean)
    return rustdesk_code_clean;

print(code_rustdesk())