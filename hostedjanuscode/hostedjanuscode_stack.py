from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core
import aws_cdk.aws_route53 as route53

class HostedjanuscodeStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # Network
        # DNS
        hostedjanusZone = route53.PublicHostedZone(self, "HostedZone",
        zone_name="hostedjanus.com"
        )


        #Outputs
        #Not working because list is returned
        cdk.CfnOutput(self, "ZoneID", value=hostedjanusZone.hosted_zone_id)
