import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_basic_infra.cdk_basic_infra_stack import CdkBasicInfraStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_basic_infra/cdk_basic_infra_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkBasicInfraStack(app, "cdk-basic-infra")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
