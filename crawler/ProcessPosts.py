# import pickle
#
# with open('post_list.pkl', 'rb') as f:
#     posts = pickle.load(f)
# print(len(posts))
#
# i = 0
# for post in posts:
#     print("post#: ", i)
#     i = i + 1
#     print(post['text'])
#     print(post['images_lowquality'])
#     print(post['images_lowquality_description'])
#     print(post['likes'])
#     print(post['comments'])
#     print(post['shares'])
#     print(post['post_url'])
#     print(post['links'])
#     print(post['user_id'])
#     print(post['username'])
#     print(post['user_url'])
#     print(post['video'])
#     # print(post['video_thumbnail'])
# f.close()

# CREATE TABLE post_data (
#     id int,
#     post text,
#     poster text,
#     imageUrls text,
#     videoUrls text
# );