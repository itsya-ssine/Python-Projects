# import customtkinter as ctk
from functions2 import *

def main():
    root = ctk.CTk()
    root.title("Developped by @__itsnaoki__")
    ctk.set_appearance_mode("light")

    frame = ctk.CTkFrame(root, corner_radius=36)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    frame.grid_rowconfigure(0, weight=1)
    # frame.grid_rowconfigure(1, weight=1)
    frame.grid_rowconfigure(2, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)
    frame.grid_columnconfigure(3, weight=1)

    # S1 -----------------------------------------------------
    semestre(frame, 0, "S1",
        " Analyse 1 :", " Algebre 1 :",
        " Meca 1 :", " Phys 1 :",
        " Info 1 :", " LC 1 :"
    )

    # S2 -----------------------------------------------------
    semestre(frame, 1, "S2",
        " Analyse 2 :", " Algebre 2 :",
        " Chimie :", " Phys 2 :",
        " Info 2 :", " LC 2 :"
    )

    # S3 -----------------------------------------------------
    semestre(frame, 2, "S3",
        " Analyse 3 :", " Algebre 3 :",
        " Meca 2 :", " Electro 1 :",
        " Info 3 :", " LC 3 :"
    )

    # S4 -----------------------------------------------------
    semestre(frame, 3, "S4",
        " Analyse 4 :"," Math App :",
        " Phys 3 :"," Electro 2 :",
        " Phys 4 :"," LC 4 :"
    )

    # Button OK ----------------------------------------------
    ctk.CTkButton(
        frame,
        text = "CALCULER",
        corner_radius = 26,
        height = 52,
        cursor = "hand2",
        font = ("Blackpast", 24),
        command = ok_button
    ).grid(row=1, column=0, columnspan=4, pady=5, padx=10, sticky="nsew")
    # --------------------------------------------------------

    # Notes --------------------------------------------------
    notes_frame = ctk.CTkFrame(frame, corner_radius=26)
    notes_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    notes_frame.grid_rowconfigure(0, weight=1)
    notes_frame.grid_rowconfigure(1, weight=1)
    notes_frame.grid_columnconfigure(0, weight=1)
    notes_frame.grid_columnconfigure(1, weight=1)
    notes_frame.grid_columnconfigure(2, weight=1)
    notes_frame.grid_columnconfigure(3, weight=1)
    notes_frame.grid_columnconfigure(4, weight=1)
    notes_frame.grid_columnconfigure(5, weight=1)

    create_filiere(notes_frame, "GI", 0)
    create_filiere(notes_frame, "IID", 1)
    create_filiere(notes_frame, "IRIC", 2)
    create_filiere(notes_frame, "MGSI", 3)
    create_filiere(notes_frame, "GE", 4)
    create_filiere(notes_frame, "GP", 5)

    create_note(notes_frame)
    # --------------------------------------------------------

    root.mainloop()

if __name__ == "__main__":
    main()