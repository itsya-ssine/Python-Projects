import customtkinter as ctk

notes = []
totals = []
notes_filieres = []

def grid(root):
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)
    root.grid_rowconfigure(5, weight=1)
    root.grid_rowconfigure(6, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

def create_label(txt, root, r):
    ctk.CTkLabel(
        root,
        text = txt,
        width = 90,
        font = ("Montserrat", 12, 'bold')
    ).grid(row=r, column=0, padx=10, pady=5)

def create_entry(root):
    T = []
    for i in range(6):
        entry = ctk.CTkEntry(
            root,
            border_width=0,
            width=150,
            height=35,
            corner_radius=16,
            placeholder_text=00)
        entry.grid(row=i+1, column=1, padx=10, pady=5)
        T.append(entry)
    notes.append(T)

def total_label(root):
    total = ctk.CTkLabel(
        root,
        text = "Moyenne : 00.00",
        font = ("Montserrat Bold", 16, 'bold'))
    total.grid(row=7, column=0, columnspan=2, pady=5, padx=10)
    totals.append(total)

def create_title(root, txt):
    ctk.CTkLabel(
        root,
        text = txt,
        text_color = "#3a7ebf",
        font = ("Alegreya Sans SC Black", 35, "bold")
    ).grid(row=0, column=0, columnspan=2, pady=5)

def create_filiere(root, txt, r, c):
    ctk.CTkLabel(
        root,
        text = txt,
        width = 100,
        text_color = "#3a7ebf",
        font = ("Alegreya Sans SC Black", 20, "bold")
    ).grid(row=r, column=c, padx=10, pady=10)

def create_note(root):
    for i in range(6):
        note = ctk.CTkLabel(
            root,
            text = "00.00",
            width = 100,
            font = ("Blackpast", 20, "bold"))
        note.grid(row=1, column=i, padx=10, pady=10)

        notes_filieres.append(note)

def semestre(frame, c, Si, M1, M2, M3, M4, M5, M6):
    S = ctk.CTkFrame(frame, corner_radius=26)
    S.grid(row=0, column=c, padx=10, pady=10, sticky="nsew")
    grid(S)

    create_title(S, Si)

    create_label(M1, S, 1)
    create_label(M2, S, 2)
    create_label(M3, S, 3)
    create_label(M4, S, 4)
    create_label(M5, S, 5)
    create_label(M6, S, 6)

    create_entry(S)

    total_label(S)

def valid_notes(notes):
    for i in range(len(notes)):
        try:
            float(notes[i])
        except ValueError:
            return False
        
        if not 0 <= float(notes[i]) <= 20 :
            return False
        
    return True

def moy(notes):
    return sum([float(notes[i]) for i in range(6)]) / 6

def ok_button():
    is_valid = True
    float_notes = []

    for i in range(4):
        s = [notes[i][j].get() for j in range(6)]
        if valid_notes(s):
            totals[i].configure(text = f"Moyenne : {moy(s):.2f}")
            float_notes.append(s)
        else:
            is_valid = False
    
    if is_valid:
        anls = sum([float(float_notes[i][0]) for i in range(4)]) / 4
        alg = sum([float(float_notes[i][1]) for i in range(4)]) / 4
        meca = sum([float(float_notes[i][2]) for i in range(4)]) / 4
        pc = sum([float(float_notes[i][3]) for i in range(4)] + [float(float_notes[3][4])]) / 5
        info = sum([float(float_notes[i][4]) for i in range(3)]) / 3
        lc = sum([float(float_notes[i][5]) for i in range(4)]) / 4

        GI = (info*7 + (anls + alg)*5 + lc*2 + meca + pc) / 21
        notes_filieres[0].configure(text = f"{GI:.2f}")

        IID = (info*7 + (anls + alg)*5 + lc*2 + meca + pc) / 21
        notes_filieres[1].configure(text = f"{IID:.2f}")

        IRIC = (info*7 + (anls + alg)*5 + lc*2 + meca + pc) / 21
        notes_filieres[2].configure(text = f"{IRIC:.2f}")

        MGSI = (info*7 + (anls + alg)*5 + lc*2 + meca + pc) / 21
        notes_filieres[3].configure(text = f"{MGSI:.2f}")

        GE = (info*7 + (anls + alg)*5 + lc*2 + meca + pc) / 21
        notes_filieres[4].configure(text = f"{GE:.2f}")

        GP = (info*7 + (anls + alg)*5 + lc*2 + meca + pc) / 21
        notes_filieres[5].configure(text = f"{GP:.2f}")
