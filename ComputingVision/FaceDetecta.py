from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from PIL import Image, ImageDraw
import json


def getRectangle(faceDictionary):
    """
    Função para criar um retângulo a partir de uma face identificada pelo Azure Face Detection
    :param faceDictionary:
    :return:
    """
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height

    return ((left, top), (right, bottom))


if __name__ == "__main__":
    #Cria o Client da API
    with open("./azurekeys.json", 'r') as jsonfile:
        azurekeys = json.load(jsonfile)

    KEY = "e737165f314b49c6a28887b85ad310d3" #Coloque aqui sua chave
    ENDPOINT = "https://face-fiap-gallo.cognitiveservices.azure.com/"  #Coloque aqui seu endpoint (Ponto de Extremidade)
    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))


    # Experimente  mudar o arquivo abaixo
    #imagefile = "../datasets/facial/face_varias.jpg"
    imagefile = "../datasets/facial/face_unica.jpg"

    with open(imagefile, 'r+b') as w:
        detected_faces = face_client.face.detect_with_stream(image=w)

    img = Image.open(imagefile)
    draw = ImageDraw.Draw(img)
    for face in detected_faces:
        print("**** Detected face id [{0}] on : {1}".format(face.face_id, face.face_rectangle))
        draw.rectangle(getRectangle(face), outline='red')
    img.show()

    pass