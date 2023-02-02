import pandas as pd
import numpy as np
import os
import scrapping_twitter
import classificador_dataset

def coletaDeDados(date_initial, date_final, names):
    
    data_scrapping = scrapping_twitter.scrapping(date_initial, date_final, names)
    data_percent_week = pd.DataFrame()
    data_amount_week = pd.DataFrame()

    for name in names:
        account_political = data_scrapping.loc[(data_scrapping['Username'] == name), :]

        # Adicionando 0s e 1s
        classificacao = classificador_dataset.zeros_ones(account_political)
        account_political = account_political.assign(tipo_post = classificacao)
        
        # Ajustes na tabela
        account_political = account_political.reset_index(drop=True)
        # data_br = date_final.strftime('%d/%m/%Y') #Formatando a data final para pt-BR
        
        # Contbilizando o total de posts políticos
        totalPosts = len(account_political)
        totalPostsPoliticos = len(account_political.where(account_political['tipo_post'] == 1).dropna())
        
        # Contabilizando a porcentagem de dados políticos
        porcent_politic = '{:.2f}'.format((totalPostsPoliticos/totalPosts)*100)
        
        # Montando a tabela com as porcentagens por data(semana)
        percentage = np.array([name, porcent_politic])
        data_percent = pd.DataFrame([percentage], columns=['Nome', date_final])
        data_percent_week = pd.concat([data_percent, data_percent_week])

        # Montando a tabela com a quantidade de posts por data(semana)
        amount = np.array([name, totalPosts])
        data_amount = pd.DataFrame([amount], columns=['Nome', date_final])
        data_amount_week = pd.concat([data_amount, data_amount_week])

        percentage = data_percent_week.reset_index(drop=True)
        amount = data_amount_week.reset_index(drop=True)

    # data_scrapping.to_csv('project-dash/project_dash/storage/data_percentage_amount/data_scrapping.csv')
    return [percentage, amount]


def geracaoDados(names, date_initial, date_final):
    path = "../project_dash/storage/data_percentage_amount"
    dir = os.listdir(path)

    if len(dir) == 0:
        # os.mkdir(path
        folder_empty_data = coletaDeDados(date_initial, date_final, names)

        folder_empty_data[0].to_csv(f'../project_dash/storage/data_percentage_amount/percentage_weekly.csv', index=False)
        folder_empty_data[1].to_csv(f'../project_dash/storage/data_percentage_amount/amount_weekly.csv', index=False)
    else:
        data_percent_one = pd.read_csv(f'../project_dash/storage/data_percentage_amount/percentage_weekly.csv', index_col=0)
        data_amount_one = pd.read_csv(f'../project_dash/storage/data_percentage_amount/amount_weekly.csv', index_col=0)

        folder_filed_data = coletaDeDados(date_initial, date_final, names)

        data_percent_two = pd.concat([data_percent_one, folder_filed_data[0].set_index('Nome')], axis=1)
        data_amount_two = pd.concat([data_amount_one, folder_filed_data[1].set_index('Nome')], axis=1)

        data_percent_two.to_csv(f'../project_dash/storage/data_percentage_amount/percentage_weekly.csv')
        data_amount_two.to_csv(f'../project_dash/storage/data_percentage_amount/amount_weekly.csv')

def main(names, date_initial, date_final):
    geracaoDados(names, date_initial, date_final)

# if __name__ == "__main__":
#     main()