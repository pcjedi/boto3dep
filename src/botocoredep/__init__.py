import botocore.session


def example():
    """
    >>> import botocore.session
    >>> session = botocore.session.get_session()
    >>> client = session.create_client('ec2')
    >>> print(client.describe_instances())
    """
    return botocore.session
