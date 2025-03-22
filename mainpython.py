import pandas as pd


data = {
    'Product': ['BASE BOX 78X188X30', 'BASE PARA CAMA CASAL BEGE', 'BLANC TOALHA DE BANHO 68X140', 'CAÇAROLA AMETISTA CRAQUEDA (PRETO E VERMELHO)', 'CORTINA C/ ARGOLA', 'CORTINA DE JANELA', 'GUARDA ROUPA 3 PCS CANADA C/ ESPELHO CASTANHO', 'GUARDA ROUPA PARMA 6 PTS C/ESPELHO CASTANHO', 'GUARDA ROUPAS PARIS 3 PTS C/ESPELHO SPECIAL-CASTAN', 'JOGO DE MESA PLAST LATINA SORTIDA', 'KIT COLCHA CASAL MARINHO', 'KIT COLCHA KING LISA', 'KIT COLCHA QUEEN', 'KIT COLCHA SOLT. INANTIL', 'LENCOL CASAL 3 PCS', 'LENCOL DE MALHA KING', 'LENCOL QUEEN MALHA', 'MAGNUS TOALHA DE BANHO', 'MANTA MICROFIBRA ALTOMAX CASAL', 'PEROLA POLAR BEGE (COLCHÃO) 138X188X20', 'PEROLA POLAR CINZA (COLCHÃO) 88X188X17', 'PEROLA POLAR PREMIUM BEGE (COLCHÃO) 158X188X26', 'RISOTEIRA TV CRAQUEADA', 'SANDUICHEIRA', 'TABULEIRO AL. BATIDO 28X36', 'TACHO N40', 'TAPETE 1.40X2.00', 'TAPETE P/PISO PEARL 50X80 AVELUDADO', 'TRAVESSEIRO', 'VENTILADOR'],
    'Current Price': [250, 500, 35, 35, 193, 190, 270, 600, 630, 150, 85, 100, 110, 75, 50, 60, 60, 32, 50, 750, 420, 1500, 40, 82, 35, 85, 95, 25, 50, 180],
    'Demand Score': [30, 30, 40, 40, 50, 50, 90, 90, 90, 50, 100, 100, 100, 100, 80, 80, 80, 60, 50, 80, 80, 80, 40, 30, 40, 40, 70, 70, 50, 70], 
    'Competitor Price': [240, 479, 40, 35, 190, 180, 300, 550, 600, 200, 80, 95, 95, 80, 60, 70, 70, 40, 60, 750, 450, 1600, 42, 90, 40, 90, 80, 30, 65, 200]
    
}

df = pd.DataFrame(data)

def adjust_price(row):
    demand_adjustment = (row['Demand Score'] / 100) * 10 
    new_price = row['Current Price'] + (row['Current Price'] * demand_adjustment / 100)
    
    if new_price > row['Competitor Price']:
        new_price = row['Competitor Price'] * 0.95  
    
    return round(new_price, 2)


df.index = range(1, len(df) + 1)


df['Adjusted Price'] = df.apply(adjust_price, axis=1)

print(df)