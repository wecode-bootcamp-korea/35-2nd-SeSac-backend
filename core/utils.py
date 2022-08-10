from urllib.parse import unquote

class ImageUploader:
    def __init__(self, client):
        self.client = client

    def upload(self, file):
        self.client.upload_fileobj(
                    file, 
                    "freshus",
                    unquote(file.name),
                    ExtraArgs={
                        "ContentType": file.content_type
                    }
                )
        
        return "https://freshus.s3.ap-northeast-2.amazonaws.com/%s" %(file.name)

    def delete(self, file_name):
        return self.client.delete_object(Bucket='freshus', Key=file_name)


class ImageHandler:
    def __init__(self, client):
        self.client = client

    def save(self, file):
        return self.client.upload(file)

    def delete(self, file_name):
        return self.client.delete(file_name)