'''
Author: James Chan
Date: 7/29/18
'''
import requests
import pandas as pd

def get_data(file, dates):
    df = pd.DataFrame(index=dates)
    df_tmp = pd.read_csv(file, index_col='Date',
            parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
    df = df.join(df_tmp).dropna()
    return df


def get_news(keywords, start_date, end_date, news_source):
    '''
    arguments:
        company (list(strings))
        start_date (string)
        end_date (string)
        news_source (list(strings))
    
    returns: 
        pandas.DataFrame
        
    description:
        This method grabs data off of newsapi.org.  Since regular user
        only has 100 queries a day, it's better to just to save data to
        local directory.  The way it is setup now, it grab news from a
        provided date range and with certain companies mentioned.
            1. create dataframe to hold published time, title, body, and company.
            2. determined the total of number of articles in the date range by the publishers
            3. we loop through all the pages to get all the articles.
            4. store article data to dataframe and return it.
    '''
    
    apikey = '23e7e5c41b6443f1bb556ec312275aff' #unique API key per registered user

    #create dataframe so we can append data to it later
    df = pd.DataFrame(columns=['Published', 'Title', 'Body','Company'])
    articles_per_page = 100 # 100 is max number of page displayed per page per API
    for keyword in keywords:
        #determine the total number of articles for the given company and date range
        url = 'https://newsapi.org/v2/everything?language=en&country=us&q={}&from={}&to={}&domains={}&pageSize=0&apiKey={}'\
                .format(keyword, start_date, end_date, news_source, apikey)
        response = requests.get(url)
        news = response.json() 
        num_articles = news['totalResults']
        print(news)
        
        #loop through the pages to get all the articles
        print("total number of articles ", num_articles)
        for page in range(1, int(num_articles/articles_per_page) + 2):
            print('downloading page: ', page)
            url = 'https://newsapi.org/v2/everything?language=en&country=us&q={}&from={}&to={}&domains={}&pageSize={}&page={}&apiKey={}'\
                    .format(keyword, start_date, end_date, news_source, articles_per_page, page, apikey)
            response = requests.get(url)
            news = response.json()
            for article in news['articles']:
                published = article['publishedAt']
                title = article['title']
                body = article['description']
                source = article['source']['name']
                df = df.append({'Published': published, 'Title' : title, 'Body': body, 'Company': keyword, 'Source': source}, ignore_index=True)
    return df