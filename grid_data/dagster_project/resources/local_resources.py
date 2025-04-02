from dagster import Definitions, EnvVar, resource
from dagster_dbt import DbtCliResource

@resource
def local_parquet_storage():
    return {"base_path": "data/staged"}

defs = Definitions(
    resources={
        "dbt": DbtCliResource(project_dir="../dbt_project"),
        "parquet_io": local_parquet_storage
    }
)