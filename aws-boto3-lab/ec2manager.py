class EC2Manager:
    def __init__(self, client):
        self._client = client
        self._cache = {}

    def list(self):
        if "instances" not in self._cache:
            self._cache["instances"] = self._client.describe_instances()
        return self._cache["instances"]