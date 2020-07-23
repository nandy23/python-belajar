import requests
for i in range(1,201):
    if i < 10 :
        req = requests.get(link, stream=True)
        req.raise_for_status()
        with open(str(i)+'.jpg', 'wb') as fd:
            for chunk in req.iter_content(chunk_size=50000):
                print('Received a Chunk 1')
                fd.write(chunk)
    elif i < 100 :
        req = requests.get(link, stream=True)
        req.raise_for_status()
        with open(str(i)+'.jpg', 'wb') as fd:
            for chunk in req.iter_content(chunk_size=50000):
                print('Received a Chunk 2')
                fd.write(chunk)
    else :
        req = requests.get(link, stream=True)
        req.raise_for_status()
        with open(str(i)+'.jpg', 'wb') as fd:
            for chunk in req.iter_content(chunk_size=50000):
                print('Received a Chunk 3')
                fd.write(chunk)
