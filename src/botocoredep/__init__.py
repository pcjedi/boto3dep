import botocore


def example():
    """
    >>> import botocore.session
    >>> session = botocore.session.get_session()
    >>> client = session.create_client('ec2')
    >>> print(client.describe_instances())
    Traceback (most recent call last):
      ...
    botocore.exceptions.NoRegionError: You must specify a region.
    """
    return botocore
