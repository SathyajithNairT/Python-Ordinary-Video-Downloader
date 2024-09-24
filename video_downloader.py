import requests

chunk_size = 500

url = ''

video_name = ''

save_path = f'path_the_video_should_be_saved_to\\{video_name}'

r = requests.get(url, stream = True)

print('Download Starting.....')

with open(save_path, 'wb') as f:
    for chunk in r.iter_content(chunk_size= chunk_size):
        f.write(chunk)

print('Download Successful!')