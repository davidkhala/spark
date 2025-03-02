from pyspark.sql.connect.session import SparkSession

from davidkhala.spark.session import ServerMore


class Databricks(ServerMore):
    clusterId: str
    spark: SparkSession

    def __init__(self, workspace_instance_name: str, token: str, cluster_id: str):
        from getpass import getuser
        user_id = getuser()  # can be any
        connection_string = f"sc://{workspace_instance_name}:443/;token={token};x-databricks-cluster-id={cluster_id};user_id={user_id}"
        session = SparkSession.builder.remote(connection_string).getOrCreate()
        super().__init__(session)
        self.clusterId = cluster_id
        self.user_id = user_id
