# Catálogo inicial de badges do SGER (Micro-Reconhecimento)
BADGES = {
    1: "Bom trabalho!",
    2: "Ajudou muito!",
    3: "Problema resolvido!",
}

def listar_badges():
    for codigo, nome in BADGES.items():
        print(f"{codigo} - {nome}")

if __name__ == "__main__":
    listar_badges()
