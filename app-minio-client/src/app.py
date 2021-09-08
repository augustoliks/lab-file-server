import minio
from os import getenv
from loguru import logger
from time import sleep


IMAGE_PATH = 'file.jpg'
BUCKET_TARGET = 'cliente-carlos-neto'


minio_client = minio.Minio(
    # getenv('MINIO_ADDRESS', 'minio.br.localhost:8090'),
    getenv('MINIO_ADDRESS', '127.0.0.1:9000'),
    access_key=getenv('MINIO_ACCESS_KEY', 'adminadmin'),
    secret_key=getenv('MINIO_SECRET_KEY', 'secretsecret'),
    secure=False
)

logger.info(f'Criando um bucket de testes denominado: {BUCKET_TARGET}')
try:
    minio_client.make_bucket(BUCKET_TARGET)
    logger.success(f'Bucket criado com sucesso: {BUCKET_TARGET}')
except minio.error.S3Error as e:
    if e.code == 'BucketAlreadyOwnedByYou':
        logger.warning(f'bucket ja existente | {BUCKET_TARGET}')
    else:
        raise e
except Exception as e:
    logger.exception(e)
    raise e

logger.info('Listando os buckets presentes no Object-Storage')
try:
    buckets = minio_client.list_buckets()
except Exception as e:
    logger.exception('Nao foi possivel listar os buckets')
    raise e

logger.info('Buckets presentes')
for bucket in buckets:
    logger.info(f'Nome: {bucket.name} | Criado em: {bucket.creation_date}')

count = 0
while True:
    remote_filename = 'image-{}'.format(count)
    logger.info(f'Iniciando upload | Nome Local do Arquivo {IMAGE_PATH} | Nome do Arquivo Remoto {remote_filename}')
    try:
        minio_client.fput_object(BUCKET_TARGET, remote_filename, IMAGE_PATH)
        logger.success(f'Upload feito com sucesso | Bucket {BUCKET_TARGET} | Nome do Arquivo Remoto {remote_filename}')
    except:
        logger.error('Erro no upload do arquivo')
    count += 1
    sleep(3)
