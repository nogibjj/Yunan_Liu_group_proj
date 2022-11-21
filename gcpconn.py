from google.cloud import bigquery
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file(
'/app/fresh-span-361719-e4e6a5688c1e.json')

project_id = 'fresh-span-361719'
client = bigquery.Client(credentials= credentials,project=project_id)

def topFivePosts():
    query_job = client.query("""
    SELECT distinct pl.id, pl.creation_date, pa.score
    FROM `bigquery-public-data.stackoverflow.post_links` pl
    LEFT JOIN `bigquery-public-data.stackoverflow.posts_answers` pa
    on pl.id = pa.id
    order by score desc
    limit 5""")

    results = query_job.result()
    # printout = results
    # count = 0
    # for row in printout:
    #     print(row)
    #     count += 1
    #     if count == 5:
    #         break
    
    return results.to_dataframe()

topFivePosts()
