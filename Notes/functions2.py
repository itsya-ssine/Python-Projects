import customtkinter as ctk

notes = []
totals = []
notes_filieres = []
float_notes = [[0 for _ in range(6)] for _ in range(4)]

def grid(root):
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)
    root.grid_rowconfigure(5, weight=1)
    root.grid_rowconfigure(6, weight=1)
    root.grid_rowconfigure(7, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

def create_label(txt, root, r):
    ctk.CTkLabel(
        root,
        text = txt,
        width = 90,
        font = ("Montserrat", 14, 'bold')
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
            placeholder_text=0)
        entry.grid(row=i+1, column=1, padx=10, pady=5)
        T.append(entry)
    notes.append(T)

def total_label(root):
    total = ctk.CTkLabel(
        root,
        text = "Moyenne : 0.00",
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

def create_filiere(root, txt, c):
    ctk.CTkLabel(
        root,
        text = txt,
        width = 100,
        text_color = "#3a7ebf",
        font = ("Alegreya Sans SC Black", 20, "bold")
    ).grid(row=0, column=c, padx=10, pady=10)

def create_note(root):
    for i in range(6):
        note = ctk.CTkLabel(
            root,
            text = "0.00",
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

def valid_note(note):
    try:
        float(note)
    except ValueError:
        return False
        
    if not 0 <= float(note) <= 20 :
        return False
        
    return True

def virefy_entries():
    flag = True
    for i, l in enumerate(notes):
        for j, note in enumerate(l):
            n = note.get()
            if n != '' and not valid_note(n):
                note.configure(fg_color = "red")
                flag = False
            else:
                note.configure(fg_color = "white")
                if n != '':
                    float_notes[i][j] = float(n)
    return flag

def moy(i):
    return sum(float_notes[i]) / 6

def ok_button():
    if not virefy_entries():
        return

    for i in range(4):
        totals[i].configure(text = f"Moyenne : {moy(i):.2f}")

    # GI:
    GI = sum([float_notes[i][0] for i in range(4)]) * 5
    GI += sum([float_notes[i][1] for i in range(4)]) * 5
    GI += sum([float_notes[i][2] for i in range(4)])
    GI += sum([float_notes[i][3] for i in range(4)])
    GI += sum([float_notes[i][4] for i in range(3)]) * 7
    GI += sum([float_notes[i][5] for i in range(4)]) * 2
    GI += float_notes[3][4]
    GI /= 78

    notes_filieres[0].configure(text = f"{GI:.2f}")

    # IID
    IID = sum([float_notes[i][0] for i in range(4)]) * 7
    IID += sum([float_notes[i][1] for i in range(4)]) * 7
    IID += sum([float_notes[i][2] for i in range(4)])
    IID += sum([float_notes[i][3] for i in range(3)])
    IID += sum([float_notes[i][4] for i in range(3)]) * 7
    IID += sum([float_notes[i][5] for i in range(4)]) * 2
    IID += (float_notes[3][4] + float_notes[3][3])
    IID /= 96

    notes_filieres[1].configure(text = f"{IID:.2f}")

    # IRIC
    IRIC = sum([float_notes[i][0] for i in range(4)]) * 2
    IRIC += sum([float_notes[i][1] for i in range(3)]) * 2
    IRIC += sum([float_notes[i][2] for i in range(4)])
    # IRIC += sum([float_notes[i][3] for i in range(4)])
    IRIC += sum([float_notes[i][4] for i in range(3)]) * 3
    IRIC += sum([float_notes[i][5] for i in range(1, 4)])
    IRIC += (float_notes[3][4] + (float_notes[1][3]*3) + float_notes[3][0])
    IRIC += ((float_notes[3][1]+float_notes[3][2])*2 + float_notes[3][3])
    IRIC /= 45

    notes_filieres[2].configure(text = f"{IRIC:.2f}")

    # MGSI
    MGSI = sum([float_notes[i][0] for i in range(4)]) * 2
    MGSI += sum([float_notes[i][1] for i in range(4)]) * 5
    MGSI += sum([float_notes[i][2] for i in range(4)])
    MGSI += sum([float_notes[i][3] for i in range(4)])
    MGSI += sum([float_notes[i][4] for i in range(3)]) * 3
    MGSI += sum([float_notes[i][5] for i in range(4)]) * 2
    MGSI += float_notes[3][4]
    MGSI /= 45

    notes_filieres[3].configure(text = f"{MGSI:.2f}")

    # GE
    GE = sum([float_notes[i][0] for i in range(4)]) / 4
    GE += sum([float_notes[i][1] for i in range(4)]) / 4
    GE += sum([float_notes[i][2] for i in range(4)]) / 5
    GE += sum([float_notes[i][3] for i in range(4)]) / 4
    GE += sum([float_notes[i][4] for i in range(3)]) / 3 * 3
    GE += sum([float_notes[i][5] for i in range(4)]) / 4 * 2
    GE += float_notes[3][4] / 5
    GE /= 21

    notes_filieres[4].configure(text = f"{GE:.2f}")

    # GP
    GP = sum([float_notes[i][0] for i in range(4)]) / 4
    GP += sum([float_notes[i][1] for i in range(4)]) / 4
    GP += sum([float_notes[i][2] for i in range(4)]) / 5
    GP += sum([float_notes[i][3] for i in range(4)]) / 4
    GP += sum([float_notes[i][4] for i in range(3)]) / 3 * 3
    GP += sum([float_notes[i][5] for i in range(4)]) / 4 * 2
    GP += float_notes[3][4] / 5
    GP /= 21

    notes_filieres[4].configure(text = f"{GP:.2f}")