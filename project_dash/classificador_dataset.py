import numpy as np
import random

def zeros_ones(contaPolitico):
    qtd_zeros = len(contaPolitico)-(len(contaPolitico)//2)
    qtd_ones = len(contaPolitico)//2
    classificacao = np.array([*np.ones(qtd_ones), *np.zeros(qtd_zeros)])
    classificacao = classificacao.astype(int)
    random.shuffle(classificacao)

    return classificacao