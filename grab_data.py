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
    apikey = '23e7e5c41b6443f1bb556ec312275aff'
    
    #determine the total number of results in the request parameter
    url = 'https://newsapi.org/v2/everything?q={}&from={}&to={}&domains={}&pageSize=0&apiKey={}'\
            .format(company, start_date, end_date, news_source, apikey)
    response = requests.get(url)
    news = response.json() 
    total_result = news['totalResults']
    
    #create a dataframe to hold article and time it was published
    df = pd.DataFrame(columns=['Published', 'Body'])
    print(df)
    '''
    once we have determined the total of number of articles, we loop through all the pages 
    to get everything since each page has a max allowable articles displayed
    '''
#    page_size = 100 # 100 is max number of page displayed per page per API
#    for page in range(1, total_result/page_size + 2):
#        url = 'https://newsapi.org/v2/everything?q={}&from={}&to={}&domains={}&pageSize={}&page={}apiKey={}'\
#                .format(company, start_date, end_date, news_source, page_size, page, apikey)
#        response = requests.get(url)
#        news = response.json()
#        
if __name__=="__main__":
    companies = ['twitter','amd','tesla'] #these three stocks move largely base on news
    news_source = 'wsj.com, bloomberg.com, cnbc.com'
    start_date = '2016-01-01'
    end_date = '2017-12-31'
    #news_request(companies, start_date, end_date, news_source)
    df = pd.DataFrame(columns=['Published', 'Body'])
    published = '1234'
    body = 'a35hw4bea'
    df = df.append({'Published': published, 'Body': body}, ignore_index=True)
    print(df)