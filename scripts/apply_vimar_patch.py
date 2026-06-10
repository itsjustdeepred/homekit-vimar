import sys

file_path = "custom_components/homekit_controller/light.py"
with open(file_path, "r") as f:
    lines = f.readlines()

out = []
replaced = False
for line in lines:
    if "characteristics[CharacteristicsTypes.ON] = True" in line and not replaced:
        indent = line.split("characteristics")[0]
        out.append(indent + "manufacturer = (\n")
        out.append(indent + "    getattr(self.service.accessory, \"manufacturer\", \"\")\n")
        out.append(indent + "    if self.service and self.service.accessory\n")
        out.append(indent + "    else \"\"\n")
        out.append(indent + ")\n\n")
        out.append(indent + "# VIMAR WORKAROUND: Omit ON command if sending other characteristics\n")
        out.append(indent + "if not characteristics or manufacturer != \"Vimar\":\n")
        out.append(indent + "    characteristics[CharacteristicsTypes.ON] = True\n")
        replaced = True
    else:
        out.append(line)

with open(file_path, "w") as f:
    f.writelines(out)

if not replaced:
    print("Errore: Impossibile trovare la riga originale nel file di Home Assistant.")
    sys.exit(1)
