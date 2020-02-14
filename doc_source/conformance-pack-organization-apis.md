# Managing Conformance Packs Across all Accounts in Your Organization<a name="conformance-pack-organization-apis"></a>

Use AWS Config to manage conformance packs across all AWS accounts within an organization\. You can do the following:
+ Centrally deploy, update, and delete conformance packs across member accounts in an organization in AWS Organizations\.
+ Deploy a common set of AWS Config rules and remediation actions across all accounts and specify accounts where AWS Config rules and remediation actions should not be created\.
+ Use the APIs from the master account in AWS Organizations to enforce governance by ensuring that the underlying AWS Config rules and remediation actions are not modifiable by your organization’s member accounts\.

**Permissions for cross account bucket access**

Each member account must have permission to access to the master account bucket\. The member account service\-linked role must have permissions to access the Amazon S3 bucket and the master account must allow all the member accounts to use this bucket\. We recommend having limited permissions to the Amazon S3 bucket policy\. To limit access, you can use `PrincipalOrgID` and `PrincipalArn` conditions in the Amazon S3 policy\.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                 "s3:GetObject",
                 "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::awsconfigconformscustomer_bucket_name/*",
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalOrgID": "customer_org_id"
                },
                "ArnLike": {
                    "aws:PrincipalArn": "arn:aws:iam::*:role/aws-service-role/config-conforms.amazonaws.com/AWSServiceRoleForConfigConforms"
                }
            }
        },
        {
            "Sid": "AllowGetBucketAcl",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetBucketAcl",
            "Resource": "arn:aws:s3:::awsconfigconformscustomer_bucket_name",
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalOrgID": "customer_org_id"
                },
                "ArnLike": {
                    "aws:PrincipalArn": "arn:aws:iam::*:role/aws-service-role/config-conforms.amazonaws.com/AWSServiceRoleForConfigConforms"
                }
            }
        }
    ]
}
```

Ensure AWS Config recording is on before you use the following APIs to manage conformance pack rules across all AWS accounts within an organization:
+ [DeleteOrganizationConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteOrganizationConformancePack.html)
+ [DescribeOrganizationConformancePacks](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConformancePacks.html)
+ [DescribeOrganizationConformancePackStatuses](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConformancePackStatuses.html)
+ [GetOrganizationConformancePackDetailedStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_GetOrganizationConformancePackDetailedStatus.html)
+ [PutOrganizationConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html)