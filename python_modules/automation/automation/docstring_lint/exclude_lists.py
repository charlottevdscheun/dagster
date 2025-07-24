"""Hardcoded exclude lists for public API validation.

This file contains all the symbols that are known to have @public API inconsistencies.
These lists allow incremental fixing while preventing new issues from being introduced.
"""

# Symbols marked @public but not yet documented in RST files
EXCLUDE_MISSING_RST = {
    # Components system - new functionality being developed
    "dagster.components.definitions.definitions",
    "dagster.components.core.load_defs.build_defs_for_component",
    "dagster.components.core.load_defs.load_from_defs_folder",
    "dagster.components.core.defs_module.DefsFolderComponent",
    "dagster.components.core.context.ComponentDeclLoadContext",
    "dagster.components.core.context.ComponentLoadContext",
    "dagster.components.component.component_loader.component",
    "dagster.components.component.component_loader.component_instance",
    "dagster.components.component.component.ComponentTypeSpec",
    "dagster.components.component.component.Component",
    "dagster.components.resolved.model.Model",
    "dagster.components.resolved.model.Resolver",
    "dagster.components.resolved.context.ResolutionContext",
    "dagster.components.resolved.base.Resolvable",
    "dagster.components.scaffold.scaffold.scaffold_with",
    "dagster.components.scaffold.scaffold.ScaffoldRequest",
    "dagster.components.scaffold.scaffold.Scaffolder",
    "dagster.components.lib.sql_component.sql_component.SqlComponent",
    "dagster.components.core.tree.ComponentTree",
    "dagster._core.errors.user_code_error_boundary",
    # Core internal functionality
    "dagster._core.definitions.definitions_class.create_repository_using_definitions_args",
    # Core storage and compute management - internal functionality
    "dagster._core.storage.compute_log_manager.ForkedPdb",
    "dagster._core.definitions.output.DynamicOutputDefinition",
    "dagster._core.storage.file_manager.FileManager",
    "dagster._core.instance.ref.InstanceRef",
    "dagster._core.storage.event_log.base.AssetRecord",
    "dagster._core.storage.event_log.base.EventLogStorage",
    "dagster._core.storage.schedules.base.ScheduleStorage",
    "dagster._core.storage.runs.base.RunStorage",
    "dagster._core.storage.event_log.sqlite.consolidated_sqlite_event_log.ConsolidatedSqliteEventLogStorage",
    # Component exports at top level
    "dagster.build_defs_for_component",
    "dagster.ComponentTypeSpec",
    "dagster.scaffold_with",
    "dagster.ScaffoldRequest",
    "dagster.Scaffolder",
    "dagster.SqlComponent",
    "dagster_sling.SlingMode",
    # Additional core internal functionality - internal module paths
    "dagster._utils.forked_pdb.ForkedPdb",
    "dagster._serdes.config_class.ConfigurableClassData",
    "dagster._serdes.config_class.ConfigurableClass",
    "dagster._core.launcher.base.RunLauncher",
    "dagster._core.scheduler.scheduler.Scheduler",
    "dagster._core.storage.compute_log_manager.ComputeLogManager",
    "dagster._core.storage.base_storage.DagsterStorage",
    "dagster._core.storage.noop_compute_log_manager.NoOpComputeLogManager",
    "dagster._core.storage.root.LocalArtifactStorage",
    "dagster._core.storage.local_compute_log_manager.LocalComputeLogManager",
    # Storage classes with @public decorators but missing RST documentation
    "dagster._core.storage.event_log.sql_event_log.SqlEventLogStorage",
    "dagster._core.storage.schedules.sql_schedule_storage.SqlScheduleStorage",
    "dagster._core.storage.runs.sql_run_storage.SqlRunStorage",
    "dagster._core.storage.event_log.sqlite.sqlite_event_log.SqliteEventLogStorage",
    "dagster._core.storage.schedules.sqlite.sqlite_schedule_storage.SqliteScheduleStorage",
    "dagster._core.storage.runs.sqlite.sqlite_run_storage.SqliteRunStorage",
    # Library pipes clients
    "dagster_aws.pipes.clients.emr_containers.PipesEMRContainersClient",
    "dagster_aws.pipes.clients.emr.PipesEMRClient",
    "dagster_aws.pipes.clients.emr_serverless.PipesEMRServerlessClient",
    "dagster_gcp.pipes.clients.dataproc_job.PipesDataprocJobClient",
    # Library resources
    "dagster_openai.resources.with_usage_metadata",
    "dagster_openai.resources.OpenAIResource",
    "dagster_sling.SlingMode",
    "dagster_sling.resources.SlingConnectionResource",
    # New public APIs missing RST documentation
    "dagster.build_defs_for_component",
    "dagster.ComponentTypeSpec",
    "dagster.scaffold_with",
    "dagster.ScaffoldRequest",
    "dagster.Scaffolder",
    "dagster.SqlComponent",
    # Library components
    "dagster_snowflake.components.sql_component.component.SnowflakeConnectionComponentBase",
}

# Symbols marked @public but not exported at top-level
EXCLUDE_MISSING_EXPORT = {
    # These are internal symbols that should either be exported or have @public removed
    "dagster._core.definitions.definitions_class.create_repository_using_definitions_args",
    "dagster.components.core.load_defs.build_defs_for_component",
    "dagster.components.core.load_defs.load_from_defs_folder",
    "dagster.components.core.defs_module.DefsFolderComponent",
    "dagster.components.core.context.ComponentDeclLoadContext",
    "dagster.components.core.context.ComponentLoadContext",
    "dagster.components.component.component_loader.component",
    "dagster.components.component.component_loader.component_instance",
    "dagster.components.component.component.ComponentTypeSpec",
    "dagster.components.component.component.Component",
    "dagster.components.resolved.model.Model",
    "dagster.components.resolved.model.Resolver",
    "dagster.components.resolved.context.ResolutionContext",
    "dagster.components.resolved.base.Resolvable",
    "dagster.components.scaffold.scaffold.scaffold_with",
    "dagster.components.scaffold.scaffold.ScaffoldRequest",
    "dagster.components.scaffold.scaffold.Scaffolder",
    "dagster._core.errors.user_code_error_boundary",
}

# List of symbols missing @public decorators
EXCLUDE_MISSING_PUBLIC = {
    "dagster_pipes.encode_env_var",
    "dagster_pipes.decode_env_var",
    "dagstermill.get_context",
    "dagstermill.yield_event",
    "dagstermill.yield_result",
    "dagster_iceberg.config.IcebergCatalogConfig",
    "dagster_iceberg.handler.IcebergBaseTypeHandler",
    "dagster_iceberg.io_manager.base.IcebergIOManager",
    "dagster_airbyte.airbyte_assets",
    "dagster_airlift.DagSelectorFn",
    "dagster_airlift.DagsterEventTransformerFn",
    "dagster_dbt.dbt_assets",
    "dagster_fivetran.ConnectorSelectorFn",
    "dagster_fivetran.fivetran_assets",
    "dagster.PreviewWarning",
    "dagster.BetaWarning",
    "dagster.SupersessionWarning",
    "dagster.file_relative_path",
    "dagster.colored_console_logger",
    "dagster.json_console_logger",
    "dagster.DefaultRunCoordinator",
}

# Modules to exclude from @public scanning
EXCLUDE_MODULES_FROM_PUBLIC_SCAN = set()

# RST files to exclude from symbol extraction
EXCLUDE_RST_FILES = set()
