'''
Author: James Chan
Description: 
    This file grabs data off of newsapi.org.  Since regular user
    only has 100 queries a day, it's better to just to save data to
    local directory.  The way it is setup now, it grab news from a
    provided date range and with certain companies mentioned.
'''
import requests
import pandas as pd

def news_request(company, start_date, end_date, news_source):
    '''
    arguments:
        company (list(strings))
        start_date (string)
        end_date (string)
        news_source (list(strings))
    
    returns: 
        pandas.DataFrame
        
    description:
        1. create dataframe to hold published time, title, body, and company.
        2. determined the total of number of articles in the date range by the publishers
        3. we loop through all the pages to get all the articles.
        4. store article data to dataframe and return it.
    '''
    
    apikey = '23e7e5c41b6443f1bb556ec312275aff' #unique API key per registered user

    #create dataframe so we can append data to it later
    df = pd.DataFrame(columns=['Published', 'Title', 'Body','Company'])
    articles_per_page = 100 # 100 is max number of page displayed per page per API
    for company in companies:
        #determine the total number of articles for the given company and date range
        url = 'https://newsapi.org/v2/everything?q={}&from={}&to={}&domains={}&pageSize=0&apiKey={}'\
                .format(company, start_date, end_date, news_source, apikey)
        response = requests.get(url)
        news = response.json() 
        num_articles = news['totalResults']
        
        #loop through the pages to get all the articles
        for page in range(1, int(num_articles/articles_per_page) + 2):
            print(company, num_articles, page)
            url = 'https://newsapi.org/v2/everything?q={}&from={}&to={}&domains={}&pageSize={}&page={}&apiKey={}'\
                    .format(company, start_date, end_date, news_source, articles_per_page, page, apikey)
            response = requests.get(url)
            news = response.json()
            for article in news['articles']:
                published = article['publishedAt']
                title = article['title']
                body = article['description']
                df = df.append({'Published': published, 'Title' : title, 'Body': body, 'Company': company}, ignore_index=True)
    return df

if __name__=="__main__":
    companies = ['twitter','netflix','tesla'] #these three stocks move largely base on news
    news_source = 'wsj.com, bloomberg.com, cnbc.com'
    start_date = '2016-01-01'
    end_date = '2017-12-31'
    df = news_request(companies, start_date, end_date, news_source)
    print(df)
    df.to_csv('news_dataset.csv')