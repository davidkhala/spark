from pyspark.sql import SparkSession, DataFrame

from davidkhala.spark.gcp import AuthOptions


class PubSub:
    auth: AuthOptions
    projectId: str
    spark: SparkSession

    def start(self, topicId, subscriptionId) -> DataFrame:
        # Set up the streaming DataFrame to listen to the Pub/Sub topic
        pubsub_df = (self.spark.readStream
                     .option("subscriptionId", subscriptionId)
                     .option("topicId", topicId)
                     .option("projectId", self.projectId)
                     .options(**self.auth.to_dict())
                     .load(format="pubsub"))
        assert pubsub_df.isStreaming == True
        return pubsub_df
