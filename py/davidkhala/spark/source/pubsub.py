from dataclasses import dataclass, asdict

from pyspark.sql import SparkSession, DataFrame


@dataclass
class GCPAuthOptions:
    # TODO migrate to https://github.com/davidkhala/gcp-collections
    clientId: str
    clientEmail: str
    privateKey: str
    privateKeyId: str

    def to_dict(self):
        return asdict(self)


class PubSub:
    auth: GCPAuthOptions
    projectId: str
    spark: SparkSession

    def start(self, topicId, subscriptionId) -> DataFrame:
        # Set up the streaming DataFrame to listen to the Pub/Sub topic
        pubsub_df = self.spark.readStream \
            .format("pubsub") \
            .option("subscriptionId", subscriptionId) \
            .option("topicId", topicId) \
            .option("projectId", self.projectId) \
            .options(**self.auth.to_dict()) \
            .load()
        assert pubsub_df.isStreaming == True
        return pubsub_df
