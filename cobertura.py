abrangencia = [
    {"cidade": 'APARECIDA', "nome": "Aparecida", "regiao": 'VALE DO PARAIBA', "codigo": 61492},
    {"cidade": 'CAÇAPAVA', "nome": "Caçapava", "regiao": 'VALE DO PARAIBA', "codigo": 62715},
    {"cidade": 'CACHOEIRA PAULISTA',"nome": "Cachoeira Paulista", "regiao": 'VALE DO PARAIBA', "codigo": 62731},
    {"cidade": 'CANAS',"nome": "Canas", "regiao": 'VALE DO PARAIBA', "codigo": 62103},
    {"cidade": 'CUNHA',"nome": "Cunha", "regiao": 'VALE DO PARAIBA', "codigo": 63738},
    {"cidade": 'GUARATINGUETÁ',"nome": "Guaratingetá", "regiao": 'VALE DO PARAIBA', "codigo": 64696},
    {"cidade": 'IGARATÁ', "nome": "Igaratá", "regiao": 'VALE DO PARAIBA', "codigo": 65056},
    {"cidade": 'JACAREÍ', "nome": "Jacareí", "regiao": 'VALE DO PARAIBA', "codigo": 65897},
    {"cidade": 'JAMBEIRO', "nome": "Jambeiro", "regiao": 'VALE DO PARAIBA', "codigo": 65994},
    {"cidade": 'LAGOINHA', "nome": "Lagoinha", "regiao": 'VALE DO PARAIBA', "codigo": 66273},
    {"cidade": 'LORENA', "nome": "Lorena", "regiao": 'VALE DO PARAIBA', "codigo": 66451},
    {"cidade": 'NATIVIDADE DA SERRA',"nome": "Natividade da Serra", "regiao": 'VALE DO PARAIBA', "codigo": 67474},
    {"cidade": 'PARAIBUNA', "nome": "Paraibuna", "regiao": 'VALE DO PARAIBA', "codigo": 68136},
    {"cidade": 'PINDAMONHANGABA', "nome": "Pindamonhangaba", "regiao": 'VALE DO PARAIBA', "codigo": 68616},
    {"cidade": 'PIQUETE', "nome": "Piquete", "regiao": 'VALE DO PARAIBA', "codigo": 68713},
    {"cidade": 'POTIM',"nome": "Potim", "regiao": 'VALE DO PARAIBA', "codigo": 61565},
    {"cidade": 'REDENÇÃO DA SERRA',"nome": "Redenção da Serra", "regiao": 'VALE DO PARAIBA', "codigo": 69477},
    {"cidade": 'ROSEIRA',"nome": "Roseira", "regiao": 'VALE DO PARAIBA', "codigo": 69876},
    {"cidade": 'SANTA BRANCA',"nome": "Santa Branca", "regiao": 'VALE DO PARAIBA', "codigo": 70211},
    {"cidade": 'SÃO JOSÉ DOS CAMPOS',"nome": "São José dos Campos", "regiao": 'VALE DO PARAIBA', "codigo": 70998},
    {"cidade": 'SÃO LUÍS DO PARAITINGA',"nome": "São Luís do Paraitinga", "regiao": 'VALE DO PARAIBA', "codigo": 71013},
    {"cidade": 'TAUBATÉ', "nome": "Taubaté", "regiao": 'VALE DO PARAIBA', "codigo": 71838},
    {"cidade": 'TREMEMBÉ',"nome": "Tremembé", "regiao": 'VALE DO PARAIBA', "codigo": 71978},

    {"cidade": 'ARAPEÍ',"nome": "Arapeí", "regiao": 'VALE HISTÓRICO', "codigo": 61646},
    {"cidade": 'AREIAS',"nome": "Areias", "regiao": 'VALE HISTÓRICO', "codigo": 61697},
    {"cidade": 'BANANAL',"nome": "Bananal", "regiao": 'VALE HISTÓRICO', "codigo": 61972},
    {"cidade": 'CRUZEIRO',"nome": "Cruzeiro", "regiao": 'VALE HISTÓRICO', "codigo": 63690},
    {"cidade": 'LAVRINHAS',"nome": "Lavrinhas", "regiao": 'VALE HISTÓRICO', "codigo": 66338},
    {"cidade": 'QUELUZ',"nome": "Queluz", "regiao": 'VALE HISTÓRICO', "codigo": 69396},
    {"cidade": 'SÃO JOSÉ DO BARREIRO',"nome": "São José do Barreiro", "regiao": 'VALE HISTÓRICO', "codigo": 70939},
    {"cidade": 'SILVEIRAS',"nome": "Silveiras", "regiao": 'VALE HISTÓRICO', "codigo": 71412},

    {"cidade": 'CARAGUATATUBA',"nome": "Caraguatatuba", "regiao": 'LITORAL NORTE', "codigo": 63118},
    {"cidade": 'ILHABELA',"nome": "Ilhabela", "regiao": 'LITORAL NORTE', "codigo": 65099},
    {"cidade": 'SÃO SEBASTIÃO',"nome": "São Sebastião", "regiao": 'LITORAL NORTE', "codigo": 71153},
    {"cidade": 'UBATUBA',"nome": "Ubatuba", "regiao": 'LITORAL NORTE', "codigo": 72095},

    {"cidade": 'CAMPOS DO JORDÃO',"nome": "Campos do Jordão", "regiao": 'SERRA DA MANTIQUEIRA', "codigo": 62952},
    {"cidade": 'MONTEIRO LOBATO',"nome": "Monteiro Lobato", "regiao": 'SERRA DA MANTIQUEIRA', "codigo": 67350},
    {"cidade": 'SANTO ANTÔNIO DO PINHAL',"nome": "Santo Antônio do Pinhal", "regiao": 'SERRA DA MANTIQUEIRA', "codigo": 70653},
    {"cidade": 'SÃO BENTO DO SAPUCAÍ',"nome": "São Bento do Sapucaí", "regiao": 'SERRA DA MANTIQUEIRA', "codigo": 70734},

    {"cidade": 'ATIBAIA',"nome": "Atibaia", "regiao": 'REGIÃO BRAGANTINA', "codigo": 61816},
    {"cidade": 'BOM JESUS DOS PERDÕES',"nome": "Bom Jesus dos Perdões", "regiao": 'REGIÃO BRAGANTINA', "codigo": 62413},
    {"cidade": 'BRAGANÇA PAULISTA',"nome": "Bragança Paulista", "regiao": 'REGIÃO BRAGANTINA', "codigo": 62510},
    {"cidade": 'JOANÓPOLIS',"nome": "Joanópolis", "regiao": 'REGIÃO BRAGANTINA', "codigo": 66117},
    {"cidade": 'NAZARÉ PAULISTA',"nome": "Nazaré Paulista", "regiao": 'REGIÃO BRAGANTINA', "codigo": 67490},
    {"cidade": 'PIRACAIA',"nome": "Piracaia", "regiao": 'REGIÃO BRAGANTINA', "codigo": 68730},
    {"cidade": 'VARGEM',"nome": "Vargem", "regiao": 'REGIÃO BRAGANTINA', "codigo": 61549}
]

count = 0
query = ""

for abr_code in abrangencia:
    query += 'CD_MUNICIPIO == ' + str(abr_code["codigo"])
    count += 1
    if count < len(abrangencia):
        query += 'or '