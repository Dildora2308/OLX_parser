# import requests

# from bs4 import BeautifulSoup  

# for i in range(1, 4):

#     url = f'https://www.olx.uz/transport/legkovye-avtomobili/?gad_source=1&gclid=Cj0KCQjwq_G1BhCSARIsACc7NxqgAijbxHlGyv8j4mdVr1nbASiLljAI8ICnRSPLWW3irQ6xnZfvrHAaArVEEALw_wcB&utm_campaign=brand-motors-cars-%5Bru%5D-search-tis-uzbekistan-np-ads-%5Bd-m%5D&utm_content=146785691985&utm_id=19885032940&utm_medium=cpc&utm_source=google/page/1/2/3/'

# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'lxml')

# top_cars = soup.find_all('div', class_='css-1dyfc0k')
                         
# for i in top_cars:
#     top_3 = i.find('h6')
# #     price = i.find('h5')

# print(top_3.text)

# # <div data-testid="adCard-featured" class="css-1dyfc0k" height="24" font-size="12" font-weight="bold" letter-spacing="0.8" color="background-global-primary">ТОП</div>







# # import requests

# # def download_image(url, save_as):
# #     response = requests.get(url)
# #     with open(save_as, 'wb') as file:
# #         file.write(response.content)

# # image_url = '''https://www.olx.uz/transport/legkovye-avtomobili/?gad_source=1&gclid=Cj0KCQjwq_G1BhCSARIsACc7NxqgAijbxHlGyv8j4mdVr1nbASiLljAI8ICnRSPLWW3irQ6xnZfvrHAaArVEEALw_wcB&utm_campaign=brand-motors-cars-%5Bru%5D-search-tis-uzbekistan-np-ads-%5Bd-m%5D&utm_content=146785691985&utm_id=19885032940&utm_medium=cpc&utm_source=google'''
# # save_as = 'image.jpg'

# # download_image(image_url, save_as)



# import shutil



