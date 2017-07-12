from uuid import uuid4
import boto3
import config


def signed_url(
    file_name=uuid4().hex,
    file_type='jpeg',
    content_type='image/jpeg',
    directory=config.S3_UPLOAD_DIRECTORY,
    bucket=config.S3_BUCKET,
    key=config.S3_KEY,
    secret=config.S3_SECRET,
    expires_in=3600,
    permissions='public-read'
):
    destination_name = '{}/{}.{}'.format(directory, file_name, file_type)
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
