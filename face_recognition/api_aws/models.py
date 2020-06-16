from django.db import models
from django.contrib.auth.models import User

import boto3

import cv2
# Create your models here.

if __name__ == "__main__":

  pass

class Face(models.Model):
  face_manager = models.Manager()
  name = models.CharField(max_length=50)
  similarity = models.FloatField(max_length=30)
  faceId = models.CharField(max_length=50)
  width = models.FloatField(max_length=30)
  height = models.FloatField(max_length=30)
  left = models.FloatField(max_length=30)
  top = models.FloatField(max_length=30)
  imageId = models.CharField(max_length=50)

  @classmethod
  def create(cls, name, similarity, faceId, width, height, left, top, imageId):
    face = cls(name = name, similarity = similarity, faceId=faceId, width=width,
                height=height, left=left, top=top, imageId=imageId)
    return face
  if __name__ == "__main__":

    pass
  
  @classmethod
  def recognize(cls):
    collectionId='desafio_javier'
    threshold = 70
    maxFaces=2
    client=boto3.client('rekognition')
    vidcap = cv2.VideoCapture('./static/video/video-1.mp4')
    def getFrame(sec):
      vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
      hasFrames,image = vidcap.read()
      if hasFrames:
          cv2.imwrite("./static/frames/image.jpg", image)     # save frame as JPG file
          fileName="./static/frames/image.jpg"
          with open(fileName, 'rb') as image:
            response=client.search_faces_by_image(CollectionId=collectionId,
                                        Image={'Bytes':image.read()},
                                        FaceMatchThreshold=threshold,
                                        MaxFaces=maxFaces)
            match=response['FaceMatches'][0]
            print('Name: ' + match['Face']['ExternalImageId'])
            print('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
            
            name = match['Face']['ExternalImageId']
            similarity = match['Similarity']
            faceId = match['Face']['FaceId']
            bounding_box = match['Face']['BoundingBox']
            width = bounding_box['Width']
            height = bounding_box['Height']
            left = bounding_box['Left']
            top = bounding_box['Top']
            imageId = match['Face']['ImageId']
        
            face = Face()
            print(name, similarity, faceId, width, height, left, top, imageId)
            face.create(name, similarity, faceId, width, height, left, top, imageId)
            face.name = name
            face.similarity = similarity
            face.faceId = faceId
            face.width = width
            face.height = height
            face.left = left
            face.top = top
            face.imageId = imageId
            face.save()
            print("Salvo no PostgreSQL")
          
      return hasFrames
    sec = 0
    frameRate = 5 #//it will capture image in each 0.5 second
    count=0
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)


