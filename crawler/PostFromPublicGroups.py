from facebook_scraper import get_posts, get_profile
import browser_cookie3

cj = browser_cookie3.chrome(domain_name='.facebook.com')
# print(cj)

# store posts into csv file
# https://stackoverflow.com/questions/65469973/write-dictionaries-with-different-keys-to-csv-file
# import csv
# with open('posts.csv', 'a') as f:
#     wr = csv.writer(f)
#     posts = get_posts(group=1590338747870221, cookies=cj)
#     for post in posts:
#         wr.writerow(post.values())
# f.close()

# print posts
# for post in get_posts('1590338747870221', pages=1, cj=cj):
#     print(post['text'][:50])

# issues: facebook_scraper.exceptions.LoginRequired: A login (cookies) is required to see this page
# solution: pass browser cookie
# https://stackoverflow.com/questions/68328706/facebook-scraper-exceptions-loginrequired-a-login-cookies-is-required-to-see

import json
# Writing to sample.json
# with open("posts.json", "a") as outfile:
#     posts = get_posts(group=1590338747870221, cookies=cj)
#     i = 0
#     for post in posts:
#         print("post#: ", i)
#         i = i + 1
#         # json_object = json.dumps(post, indent=4)
#         # outfile.write()
# outfile.close()

# get posts from group
# method 2: to write into file
import pickle

# BSA group, 1590338747870221
# posts = get_posts(group=1590338747870221, cookies=cj, options={"comments": True, "reactors": True})
# i = 0
# all_posts = []
# for post in posts:
#     print("post#: ", i)
#     i = i + 1
#     all_posts.append(post)
#
# with open('post_list.pkl', 'wb') as f:
#     pickle.dump(all_posts, f)
# f.close()


#1 BSA group, 1590338747870221 - fetched 200 data
#2 aripata group, 368809433220789 - fetched 200 data
#3 509564056346760 - wtf carbondale - fetched 200 data
#4 918725435132792 - buy nothing carbondale
posts = get_posts(group=509564056346760, cookies=cj, options={"comments": False, "reactors": False})
i = 0
all_posts = []
for post in posts:
    print("post#: ", i)
    i = i + 1
    all_posts.append(post)

with open('wtfcarbondale.pkl', 'wb') as f:
    pickle.dump(all_posts, f)
f.close()

# issue: temporary ban issue
# https://github.com/kevinzg/facebook-scraper/issues/409
# https://github.com/kevinzg/facebook-scraper/issues/385


# dataset
# news data: https://www.kaggle.com/datasets/rishidamarla/facebook-posts-from-abc-bbc-cbs-cnn-20122016

