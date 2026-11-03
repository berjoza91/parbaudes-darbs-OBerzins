# ----------------------------------------------------------------------
# A1. Python — WARNING rindu skaits
# ----------------------------------------------------------------------

# Jāsaskaita, cik žurnālā ir WARNING rindu. Izvadās nulle, lai gan tādas rindas failā ir. Atrodi un salabo kļūdu.
#
# Atrodi un salabo. Tad palaid.
# ----------------------------------------------------------------------                                                                                              

skaits = 0
with open("A1_kluda.py", encoding="utf-8") as f:
    for rinda in f:
        if "WARNING" in rinda:
            skaits += 1

print(skaits)