import boto3
import urllib.request
from datetime import datetime

from urllib.error import URLError

s3 = boto3.client('s3')

def f(event, context):
    # Obtén la fecha actual
    now = datetime.now()
    date_string = now.strftime("%Y-%m-%d")
    
    url = 'https://www.eltiempo.com/'
    
    try:
        # Descargar la página del tiempo
        response = urllib.request.urlopen(url)
        data = response.read()

        # Subir el archivo a S3
        s3.put_object(Body=data, Bucket='zappa-72939e7na', Key=f'{date_string}.html')
        
        return {
            'statusCode': 200,
            'body': f'Archivo {date_string}.html subido exitosamente a S3'
        }
    except URLError as e:
        return {
            'statusCode': 500,
            'body': f'Error al conectarse a la URL: {str(e)}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error al procesar la solicitud: {str(e)}'
        }
    finally:
        pass