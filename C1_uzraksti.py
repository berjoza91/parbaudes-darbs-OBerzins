import sys

LOG_FILE = "log.txt"

if len(sys.argv) < 2:
    print("Lietošana: python script.py <līmenis>")
    sys.exit(0)

level = sys.argv[1]

try:
    with open(LOG_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Atlasa visas rindas ar norādīto līmeni
    filtered_lines = [
        line for line in lines
        if level in line
    ]

    # Izvada atrasto rindu skaitu
    print(f"Līmeņa '{level}' rindu skaits: {len(filtered_lines)}")

    # Saglabā atlasītās rindas failā
    output_file = f"{level}_log.txt"

    with open(output_file, "w", encoding="utf-8") as file:
        file.writelines(filtered_lines)

    print(f"Rindas saglabātas failā: {output_file}")

except FileNotFoundError:
    print(f"Kļūda: fails '{LOG_FILE}' nav atrasts.")
