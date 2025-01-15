import boto3
import dateutil

# from six import PY3, string_types


def get_s3_client():
    """
    Get an S3 client
    >>> get_s3_client() # doctest: +ELLIPSIS
    <botocore.client.S3 object at 0x...>
    """
    return boto3.client("s3")


def parse_date(date_str):
    """
    Parse a date string
    >>> parse_date("2018-01-01")
    datetime.datetime(2018, 1, 1, 0, 0)
    """
    return dateutil.parser.parse(date_str)
