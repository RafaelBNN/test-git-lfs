from datetime import datetime

if __name__ == "__main__":
    current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    new_line = f"NE;PE;POCAO;RAFAEL NETO; 00.000.000/0001-00;ESTRADA VICINAL MARIO COVAS;4189;;BAIRRO DE CIMA;18404-517;GLP;{current_datetime};115,99;;R$ / 13 kg;SUPERGASBRAS ENERGIA"
    with open("dados-abertos-precos-glp.csv", "a", encoding="UTF-8") as f:
        f.write("\n" + new_line)
    print(f"Teoricamente adicionei a linha {new_line}")