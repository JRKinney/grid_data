from dagster_dbt import dbt_assets, DbtCliResource
from dagster import AssetExecutionContext

@dbt_assets(manifest_path="../dbt_project/target/manifest.json")
def ercot_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()