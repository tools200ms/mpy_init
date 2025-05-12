import os

def list( path:str ):
    try:
        files = os.listdir(path)

        for f in files:
            print(f)
    except Exception as e:
        print(f"Error listing {path}", e)

list('/tmp')
