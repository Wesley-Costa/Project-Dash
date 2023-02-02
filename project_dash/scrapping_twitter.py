import pandas as pd
import snscrape
import snscrape.modules.twitter as sntwitter
from datetime import date, timedelta

def scrapping(date_initial, date_final, names):
    conta = []
    for name in names:
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{name} since:{date_initial} until:{date_final}').get_items()):
            conta.append([tweet.user.url, tweet.date, tweet.user.id, tweet.content, tweet.user.username])
        tweets = pd.DataFrame(
            conta, columns=['URL', 'Datetime', 'Tweet Id', 'Text', 'Username'])
    
    tweets.to_csv(f'../project_dash/storage/dados-scrapping-backup/dados-scrapping-{date_final}.csv')
    return tweets

def main():
    date_final = date.today()
    date_initial = date_final - timedelta(6)

    names = ['jairbolsonaro', 'LulaOficial', 'cirogomes', 'simonetebetbr']
    data_scrapping = scrapping(date_initial, date_final, names)
    
    # data_scrapping.to_csv(f'./dados-scrapping-backup/dados-scrapping-{date_final}.csv')
    return data_scrapping


if __name__ == "__main__":
    main()