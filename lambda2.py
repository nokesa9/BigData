import urllib.request
import boto3
from datetime import datetime

def lambda_handler(event, context):
    try:
        # Obtener la fecha actual en el formato yyy-mm-dd
        fecha_actual = datetime.now().strftime('%Y-%m-%d')

        # URL de la página principal del tiempo
        url = 'https://www.tiempo.com/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 OPR/45.0.2552.898'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read()

        # Guardar el archivo en memoria con el nombre yyy-mm-dd.html
        file_name = f'{fecha_actual}.html'
        s3 = boto3.client('s3')
        s3.put_object(Bucket='horas', Key=file_name, Body=html)

        return {
            'statusCode': 200,
            'body': f'Archivo {file_name} subido exitosamente a S3.'
        }
    except Exception as e:
        print(f'Error: {e}')
        return {
            'statusCode': 500,
            'body': f'Error:{e}'
}