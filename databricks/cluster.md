
# Runtime
Runtime for Machine Learning
- based on standard runtime
- contains many popular machine learning libraries: TensorFlow, PyTorch, and XGBoost
- contains Databricks AutoML
- supports distributed deep learning training using Horovod.

# Local SSDs
https://community.databricks.com/t5/data-engineering/what-is-the-local-ssd-used-for-in-databricks/m-p/53575/highlight/true#M29823
> In summary, local SSDs play a crucial role in improving performance by caching data and storing temporary files.

# Compute Policy
- Requires Premium plan

It used to 
- limit a user or group’s compute creation permissions (max cluster count, max cost per cluster)
- Simplify UI to enable more users to create own clusters
- Apply cluster-scoped library installations

Default policies (prebuilt)
## Personal Compute
- available to all users in your workspace
- a single-node compute resource
- minimal configuration option

## Shared Compute
- Allow more compute resources (multi-node)
- Uses the Shared access mode
- Defaults to latest Databricks **Runtime LTS** version
- Can only be used by workspace admins

## Power User Compute
- Similar to **Shared Compute** policy
- Defaults to the latest Databricks **Runtime ML** version (newer than latest LTS)


# Job Compute
