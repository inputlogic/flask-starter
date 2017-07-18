from uuid import uuid4
import boto3
import config


def signed_url(
    file_name=None,
    file_type='jpeg',
    content_type='image/jpeg',
    directory=config.S3_UPLOAD_DIRECTORY,
    bucket=config.S3_BUCKET,
    key=config.S3_KEY,
    secret=config.S3_SECRET,
    expires_in=3600,
    permissions='public-read'
):
    '''Get a signed url for posting a file to s3.

    Defaults to use config values:
        S3_UPLOAD_DIRECTORY
        S3_BUCKET
        S3_KEY
        S3_SECRET

    Returns a dict:
        result = {
            'data': dict
            'url': string
        }

    To upload a file:
        - send a post request to result['data']['url']
        - include the following form data:
            - 'file': the file from the file html input
            - each key/value in result['data']['fields']

    Once uploaded, the file will be at result['url']

    reference:
        https://devcenter.heroku.com/articles/s3-upload-python
    '''
    file_name = uuid4().hex if file_name is None else file_name
    destination_name = '{0}/{1}.{2}'.format(directory, file_name, file_type)
    s3 = boto3.client(
        's3',
        aws_access_key_id=key,
        aws_secret_access_key=secret
    )

    presigned_post = s3.generate_presigned_post(
        Bucket=bucket,
        Key=destination_name,
        Fields={'acl': permissions, 'Content-Type': content_type},
        Conditions=[
            {'acl': permissions},
            {'Content-Type': content_type}
        ],
        ExpiresIn=expires_in
    )

    return {
        'data': presigned_post,
        'url': 'https://{}.s3.amazonaws.com/{}'.format(
            bucket,
            destination_name
        )
    }
