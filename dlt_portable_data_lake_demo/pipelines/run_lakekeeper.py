# import os
# import dlt
# import dlt_plus
# from dlt_plus.destinations.impl.iceberg.factory import iceberg
# import dlt_plus.project
# import pyiceberg.io


# # , filesystem={"bucket_url": "s3://demo/"}
# iceberg_dest = iceberg(
#     "rest",
#     credentials={
#         "uri": "http://localhost:8181/catalog",
#         "warehouse": "lakekeeper_demo",
#     },
#     table_root_layout="s3://dlt-ci-test-bucket/dlt_plus_demo/lakekeeper_demo/{dataset_name}/{table_name}",
#     # credentials={"uri": "https://lakekeeper-f6mi9.ondigitalocean.app/catalog", "warehouse": "dlt-ci-warehouse"},
#     # table_root_layout="s3://dlt-ci-test-bucket/lakekeeper-warehouse-1/dlt_plus_demo/lakekeeper_demo/{dataset_name}/{table_name}"
# )

# # iceberg_dest = iceberg("rest", credentials={"uri": "http://localhost:8181/catalog", "warehouse": "dlt_ci"})

# pipeline = dlt.pipeline("aleph_loader", destination=iceberg_dest, dataset_name="aleph8")
# pipeline.sync_destination()
# print(pipeline.run([1, 2, 3], table_name="natural2"))
# print(pipeline.dataset().natural2.df())


# # corresponding to bauplan

# # @dlt.transformation
# # def model():
# #     ...

# # # will create NAMESPACE and switch to branch 'branch_name' (from main branch)
# # pipeline = dlt.pipeline("bauplan_api", dataset_name=NAMESPACE, destination=iceberg("rest", branch=branch_name))
# # # will execute model
# # pipeline.run(model)
