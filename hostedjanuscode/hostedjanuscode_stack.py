from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core
import aws_cdk.aws_route53 as route53
import aws_cdk.aws_cloudfront as cloudfront
import aws_cdk.aws_cloudfront_origins as origins
import os.path
from aws_cdk.aws_s3_assets import Asset as asset

class HostedjanuscodeStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # Network
        # DNS
        hostedjanusZone = route53.PublicHostedZone(self, "HostedZone",
        zone_name="hostedjanus.com"
        )

        # Artifacts
        # Web page s3 Asset
        file_asset = asset(self, 'WebPageAsset',
        path=os.path.join("./webpage")
        )

        # CDN
        # Creates a distribution for a S3 bucket.
        hostedjanus_distribution = cloudfront.Distribution(self, "hostedjanusDist",
            default_behavior=cloudfront.BehaviorOptions(origin=origins.S3Origin(file_asset.bucket))
        )

        route53.CnameRecord(self, "CloudFrontnameRecord", zone=hostedjanusZone,
        record_name="www", domain_name=hostedjanus_distribution.domain_name)

        #Outputs
        #Not working because list is returned
        cdk.CfnOutput(self, "ZoneID", value=hostedjanusZone.hosted_zone_id)
