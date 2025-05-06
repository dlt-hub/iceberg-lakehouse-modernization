# 🚀 Upgrade Your Infrastructure to Iceberg with dlt + Lakekeeper

This repository demonstrates how to modernize your data infrastructure by combining the power of:
* [Apache Iceberg](https://iceberg.apache.org/)
* [dlt](https://dlthub.com/)
* [Lakekeeper](https://docs.lakekeeper.io/) 

Check out the YouTube talk for a quick walkthrough of this modernization: [📺 YouTube: Upgrade Your Infrastructure to Iceberg with dlt + Lakekeeper](https://www.youtube.com/watch?v=fZhghCQq00I)

---

## 🔁 Configuration Files

This repository contains two configuration files:

- **`dlt_warehouse.yml`** – This is the **original configuration** before modernization, representing a traditional Snowflake-based warehouse setup.
- **`dlt.yml`** – This is the **modernized configuration**, using Apache Iceberg as the destination via Lakekeeper.

Refer to each file to see how to transition from a legacy data warehouse pipeline to a modern, open table format with Iceberg.

## ⚙️ Setup Guide

### Quickstart Instructions

1. Install [uv](https://github.com/astral-sh/uv)
```sh
pip install uv
```

2. clone this repo and run the command:
```sh
make dev
```

3. Put your Lakekeeper token to `dlt_portable_data_lake_demo/.dlt/secrets.toml`

```toml
[destination.iceberg_lake.credentials]
credential="your-token"
```

4. Download an archive with data
```sh
make download-gh
```

5. Add the license: 
```toml
[runtime]
license="..."
```
💡 The license is needed when using dlt+ features, sources, or destinations like Iceberg in this demo. Don’t have one yet? Join the [waiting list](https://info.dlthub.com/waiting-list) to request it.

5. Run the pipeline
```sh
uv run dlt pipeline loading_events run
```

6. You can see the data in the Lakekeeper: https://you.hosted.lakekeeper.app/catalog

7. (Optional) Run transformations. 
You need to specify credentials for Snowflake warehouse or change the warehouse type to DuckDB.

```sh
dlt transformation aggregate_issues run
```
Example Snowflake credentials in `secrets.toml`   
```toml
[destination.snowflake.credentials]
database = "dlt_data"
password = "<password>"
username = "loader"
host = "your-host"
warehouse = "COMPUTE_WH"
role = "DLT_LOADER_ROLE"
```
➡️ See the [dlt Snowflake destination docs](https://dlthub.com/docs/dlt-ecosystem/destinations/snowflake) for more.

8. To access to your data, check the [`access.ipynb`](demo/access.ipynb).
