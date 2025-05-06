from dlt_plus.project import Project
from dlt_plus.project.entity_factory import EntityFactory
from dlt_plus.project.pipeline_manager import PipelineManager
from dlt_plus_tests.fixtures import auto_test_access_profile as auto_test_access_profile
from dlt_plus_tests.utils import assert_load_info, load_table_counts


def test_events_to_data_lake(dpt_project_config: Project) -> None:
    """Make sure we dispatch the events to tables properly"""
    factory = EntityFactory(dpt_project_config)
    github_events = factory.get_source("events")
    events_to_lake = factory.get_pipeline("events_to_lake")
    info = events_to_lake.run(github_events())
    assert_load_info(info)

    # did I load my test data
    assert load_table_counts(
        events_to_lake, *events_to_lake.default_schema.data_table_names()
    ) == {
        "issues_event": 604,
        "pull_request_event": 514,
        "watch_event": 385,
        "push_event": 6178,
        "public_event": 42,
        "pull_request_review_event": 119,
        "create_event": 1205,
        "issue_comment_event": 298,
        "delete_event": 329,
        "fork_event": 105,
        "release_event": 105,
        "pull_request_review_comment_event": 73,
        "gollum_event": 15,
        "commit_comment_event": 6,
        "member_event": 22,
        "gollum_event__payload__pages": 15,
        "push_event__payload__commits": 8255,
    }
    # you can also assert columns, data types, relations that got inferred


def test_t_layer(dpt_project_config: Project) -> None:
    """Make sure that our generated dbt package creates expected reports in the data warehouse"""
    pipeline_manager = PipelineManager(dpt_project_config)
    info = pipeline_manager.run_pipeline("events_to_lake")
    assert_load_info(info)
    # render and run t-layer, we use test profile so we render in private space
    transformation = pipeline_manager.factory.get_transformation("aggregate_issues")
    # assert "_storage" in transformation.transformation_layer_path
    # do not render new t-layer
    # transformation.render_transformation_layer()
    transformation.run()

    # get the output pipeline
    output_pipeline = transformation.state_output_pipeline
    # get counts of reports tables
    print(
        load_table_counts(
            output_pipeline, *output_pipeline.default_schema.data_table_names()
        )
    )
    assert load_table_counts(
        output_pipeline, *output_pipeline.default_schema.data_table_names()
    ) == {
        "dim_issues_actors": 114,
        "dim_issues_repos": 123,
        "dlt_processed_load_ids": 1,
    }
