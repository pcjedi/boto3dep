import boto3


def get_s3_client():
    """
    Get an S3 client
    >>> get_s3_client() # doctest: +ELLIPSIS
    <botocore.client.S3 object at 0x...>
    """
    return boto3.client("s3")
