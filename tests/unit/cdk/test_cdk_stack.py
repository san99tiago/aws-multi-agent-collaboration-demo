# Built-in imports
import os

# External imports
import aws_cdk as core
import aws_cdk.assertions as assertions

# Own imports
from cdk.stacks.cdk_multi_agent_collab_stack import MultiAgentStack

app: core.App = core.App()
stack: MultiAgentStack = MultiAgentStack(
    scope=app,
    construct_id="santi-multi-agent-collab-test",
    main_resources_name="santi-multi-agent-collab",
    app_config={
        "deployment_environment": "test",
        "log_level": "DEBUG",
        "agents_data_table_name": "aws-multi-agent-collab-test2",
        "enable_rag": True,
    },
)
template: assertions.Template = assertions.Template.from_stack(stack)


def test_app_synthesize_ok():
    app.synth()


def test_dynamodb_table_created():
    match = template.find_resources(
        type="AWS::DynamoDB::Table",
    )
    assert len(match) == 1


def test_lambda_function_created():
    match = template.find_resources(
        type="AWS::Lambda::Function",
    )
    assert len(match) >= 2
