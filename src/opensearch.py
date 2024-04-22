from config import OPENSEARCH_CLUSTER_ENDPOINT, OPENSEARCH_HOST_PORT, \
    OPENSEARCH_USERNAME, OPENSEARCH_PASSWORD, OPENSEARCH_INDEX_NAME
from opensearchpy import OpenSearch


# Starting a connection to the OpenSearch client
client = OpenSearch(
    hosts=[{"host": OPENSEARCH_CLUSTER_ENDPOINT, "port": OPENSEARCH_HOST_PORT}],
    http_compress=True,
    http_auth=(OPENSEARCH_USERNAME, OPENSEARCH_PASSWORD),
    use_ssl=True,
    verify_certs=False,
    ssl_show_warn=False
)


def send_data_to_opensearch(data: dict) -> dict:
    """
    Function responsible for receiving a dictionary that will be sent
    to the OpenSearch index informed in the environment variables.
    :param data: Dictionary that will contain credit monitoring collection data
    :return: Returns OpenSearch's response to sending data.
    """
    response = client.index(index=OPENSEARCH_INDEX_NAME,  body=data)
    return response


__all__ = ["send_data_to_opensearch"]
