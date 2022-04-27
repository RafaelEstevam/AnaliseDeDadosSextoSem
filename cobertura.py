abrangencia = [
    {"cidade": 'APARECIDA', "regiao": 'VALE DO PARAIBA', "codigo": 61492},
    {"cidade": 'CAÇAPAVA', "regiao": 'VALE DO PARAIBA', "codigo": 62715},
    {"cidade": 'CACHOEIRA PAULISTA', "regiao": 'VALE DO PARAIBA', "codigo": 62731},
    {"cidade": 'CANAS', "regiao": 'VALE DO PARAIBA', "codigo": 62103},
    {"cidade": 'CUNHA', "regiao": 'VALE DO PARAIBA', "codigo": 63738},
    {"cidade": 'GUARATINGUETÁ', "regiao": 'VALE DO PARAIBA', "codigo": 64696},
    {"cidade": 'IGARATÁ', "regiao": 'VALE DO PARAIBA', "codigo": 65056},
    {"cidade": 'JACAREÍ', "regiao": 'VALE DO PARAIBA', "codigo": 65897},
    {"cidade": 'JAMBEIRO', "regiao": 'VALE DO PARAIBA', "codigo": 65994},
    {"cidade": 'LAGOINHA', "regiao": 'VALE DO PARAIBA', "codigo": 66273},
    {"cidade": 'LORENA', "regiao": 'VALE DO PARAIBA', "codigo": 66451},
    {"cidade": 'NATIVIDADE DA SERRA', "regiao": 'VALE DO PARAIBA', "codigo": 67474},
    {"cidade": 'PARAIBUNA', "regiao": 'VALE DO PARAIBA', "codigo": 68136},
    {"cidade": 'PINDAMONHANGABA', "regiao": 'VALE DO PARAIBA', "codigo": 68616},
    {"cidade": 'PIQUETE', "regiao": 'VALE DO PARAIBA', "codigo": 68713},
    {"cidade": 'POTIM', "regiao": 'VALE DO PARAIBA', "codigo": 61565},
    {"cidade": 'REDENÇÃO DA SERRA', "regiao": 'VALE DO PARAIBA', "codigo": 69477},
    {"cidade": 'ROSEIRA', "regiao": 'VALE DO PARAIBA', "codigo": 69876},
    {"cidade": 'SANTA BRANCA', "regiao": 'VALE DO PARAIBA', "codigo": 70211},
    {"cidade": 'SÃO JOSÉ DOS CAMPOS', "regiao": 'VALE DO PARAIBA', "codigo": 70998},
    {"cidade": 'SÃO LUÍS DO PARAITINGA', "regiao": 'VALE DO PARAIBA', "codigo": 71013},
    {"cidade": 'TAUBATÉ', "regiao": 'VALE DO PARAIBA', "codigo": 71838},
    {"cidade": 'TREMEMBÉ', "regiao": 'VALE DO PARAIBA', "codigo": 71978},

    {"cidade": 'ARAPEÍ', "regiao": 'VALE HISTÓRICO', "codigo": 61646},
    {"cidade": 'AREIAS', "regiao": 'VALE HISTÓRICO', "codigo": 61697},
    {"cidade": 'BANANAL', "regiao": 'VALE HISTÓRICO', "codigo": 61972},
    {"cidade": 'CRUZEIRO', "regiao": 'VALE HISTÓRICO', "codigo": 63690},
    {"cidade": 'LAVRINHAS', "regiao": 'VALE HISTÓRICO', "codigo": 66338},
    {"cidade": 'QUELUZ', "regiao": 'VALE HISTÓRICO', "codigo": 69396},
    {"cidade": 'SÃO JOSÉ DO BARREIRO', "regiao": 'VALE HISTÓRICO', "codigo": 70939},
    {"cidade": 'SILVEIRAS', "regiao": 'VALE HISTÓRICO', "codigo": 71412},

    {"cidade": 'CARAGUATATUBA', "regiao": 'LITORAL NORTE', "codigo": 63118},
    {"cidade": 'ILHABELA', "regiao": 'LITORAL NORTE', "codigo": 65099},
    {"cidade": 'SÃO SEBASTIÃO', "regiao": 'LITORAL NORTE', "codigo": 71153},
    {"cidade": 'UBATUBA', "regiao": 'LITORAL NORTE', "codigo": 72095},

    {"cidade": 'CAMPOS DO JORDÃO', "regiao": 'SERRA DA MANTIQUEIRA', "codigo": 62952},
    {"cidade": 'MONTEIRO LOBATO', "regiao": 'SERRA DA MANTIQUEIRA', "codigo": 67350},
    {"cidade": 'SANTO ANTÔNIO DO PINHAL', "regiao": 'SERRA DA MANTIQUEIRA', "codigo": 70653},
    {"cidade": 'SÃO BENTO DO SAPUCAÍ', "regiao": 'SERRA DA MANTIQUEIRA', "codigo": 70734},

    {"cidade": 'ATIBAIA', "regiao": 'REGIÃO BRAGANTINA', "codigo": 61816},
    {"cidade": 'BOM JESUS DOS PERDÕES', "regiao": 'REGIÃO BRAGANTINA', "codigo": 62413},
    {"cidade": 'BRAGANÇA PAULISTA', "regiao": 'REGIÃO BRAGANTINA', "codigo": 62510},
    {"cidade": 'JOANÓPOLIS', "regiao": 'REGIÃO BRAGANTINA', "codigo": 66117},
    {"cidade": 'NAZARÉ PAULISTA', "regiao": 'REGIÃO BRAGANTINA', "codigo": 67490},
    {"cidade": 'PIRACAIA', "regiao": 'REGIÃO BRAGANTINA', "codigo": 68730},
    {"cidade": 'VARGEM', "regiao": 'REGIÃO BRAGANTINA', "codigo": 61549}
]

count = 0
query = ""

for abr_code in abrangencia:
    query += 'CD_MUNICIPIO == ' + str(abr_code["codigo"])
    count += 1
    if count < len(abrangencia):
        query += 'or '