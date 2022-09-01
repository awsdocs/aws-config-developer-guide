# Granting Custom Permissions for AWS Config Users<a name="recommended-iam-permissions-using-aws-config-console-cli"></a>

AWS Config policies grant permissions to users who work with AWS Config\. If you need to grant different permissions to users, you can attach a AWS Config policy to an IAM group or to a user\. You can edit the policy to include or exclude specific permissions\. You can also create your own custom policy\. Policies are JSON documents that define the actions a user is allowed to perform and the resources that the user is allowed to perform those actions on\.

**Contents**
+ [Read\-only access](#read-only-config-permission)
+ [Full access](#full-config-permission)
+ [Controlling User Permissions for Actions on Multi\-Account Multi\-Region Data Aggregation](#resource-level-permission)
+ [Additional Information](#config-permissions-more-info)

## Read\-only access<a name="read-only-config-permission"></a>

The following example shows a AWS managed policy, `AWSConfigUserAccess` that grants read\-only access to AWS Config\.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "config:Get*",
        "config:Describe*",
        "config:Deliver*",
        "config:List*",
        "config:Select*",
        "tag:GetResources",
        "tag:GetTagKeys",
        "cloudtrail:DescribeTrails",
        "cloudtrail:GetTrailStatus",
        "cloudtrail:LookupEvents"
      ],
      "Resource": "*"
    }
  ]
}
```

In the policy statements, the `Effect` element specifies whether the actions are allowed or denied\. The `Action` element lists the specific actions that the user is allowed to perform\. The `Resource` element lists the AWS resources the user is allowed to perform those actions on\. For policies that control access to AWS Config actions, the `Resource` element is always set to `*`, a wildcard that means "all resources\." 

The values in the `Action` element correspond to the APIs that the services support\. The actions are preceded by `config:` to indicate that they refer to AWS Config actions\. You can use the `*` wildcard character in the `Action` element, such as in the following examples:
+ `"Action": ["config:*ConfigurationRecorder"]`

  This allows all AWS Config actions that end with "ConfigurationRecorder" \(`StartConfigurationRecorder`, `StopConfigurationRecorder`\)\.
+ `"Action": ["config:*"]`

  This allows all AWS Config actions, but not actions for other AWS services\.
+ `"Action": ["*"]`

  This allows all AWS actions\. This permission is suitable for a user who acts as an AWS administrator for your account\.

The read\-only policy doesn't grant user permission for the actions such as `StartConfigurationRecorder`, `StopConfigurationRecorder`, and `DeleteConfigurationRecorder`\. Users with this policy are not allowed to start configuration recorder, stop configuration recorder, or delete configuration recorder\. For the list of AWS Config actions, see the [AWS Config API Reference](https://docs.aws.amazon.com/config/latest/APIReference/)\.

## Full access<a name="full-config-permission"></a>

The following example shows a policy that grants full access to AWS Config\. It grants users the permission to perform all AWS Config actions\. It also lets users manage files in Amazon S3 buckets and manage Amazon SNS topics in the account that the user is associated with\.

**Note**  
This policy grants broad permissions\. Before granting full access, consider starting with a minimum set of permissions and granting additional permissions as necessary\. Doing so is better practice than starting with permissions that are too lenient and then trying to tighten them later\.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sns:AddPermission",
                "sns:CreateTopic",
                "sns:DeleteTopic",
                "sns:GetTopicAttributes",
                "sns:ListPlatformApplications",
                "sns:ListTopics",
                "sns:SetTopicAttributes"
            ],
            "Resource": "*"   
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:CreateBucket",
                "s3:GetBucketAcl",
                "s3:GetBucketLocation",
                "s3:GetBucketNotification",
                "s3:GetBucketPolicy",
                "s3:GetBucketRequestPayment",
                "s3:GetBucketVersioning",
                "s3:ListAllMyBuckets",
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads",
                "s3:ListBucketVersions",
                "s3:PutBucketPolicy"
            ],
            "Resource": "arn:aws:s3:::*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:CreateRole",
                "iam:GetRole",
                "iam:GetRolePolicy",
                "iam:ListRolePolicies",
                "iam:ListRoles",
                "iam:PutRolePolicy",
                "iam:AttachRolePolicy",
                "iam:CreatePolicy",
                "iam:CreatePolicyVersion",
                "iam:DeletePolicyVersion",
                "iam:CreateServiceLinkedRole"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": [
                        "config.amazonaws.com",
                        "ssm.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudtrail:DescribeTrails",
                "cloudtrail:GetTrailStatus",
                "cloudtrail:LookupEvents"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "config:*",
                "tag:Get*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeDocument",
                "ssm:GetDocument",
                "ssm:DescribeAutomationExecutions",
                "ssm:GetAutomationExecution",
                "ssm:ListDocuments",
                "ssm:StartAutomationExecution"
            ],
            "Resource": "*"
        }
        
    ]
}
```

## Controlling User Permissions for Actions on Multi\-Account Multi\-Region Data Aggregation<a name="resource-level-permission"></a>

You can use resource\-level permissions to control a user's ability to perform specific actions on multi\-account multi\-region data aggregation\. The following AWS Config `Aggregator` APIs support resource level permissions:
+ [BatchGetAggregateResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_BatchGetAggregateResourceConfig.html)
+ [DeleteConfigurationAggregator](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConfigurationAggregator.html)
+ [DescribeAggregateComplianceByConfigRules](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeAggregateComplianceByConfigRules.html)
+ [DescribeAggregateComplianceByConformancePacks](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeAggregateComplianceByConformancePacks.html)
+ [DescribeConfigurationAggregatorSourcesStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationAggregatorSourcesStatus.html)
+ [GetAggregateComplianceDetailsByConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_GetAggregateComplianceDetailsByConfigRule.html)
+ [GetAggregateConfigRuleComplianceSummary](https://docs.aws.amazon.com/config/latest/APIReference/API_GetAggregateConfigRuleComplianceSummary.html)
+ [GetAggregateConformancePackComplianceSummary](https://docs.aws.amazon.com/config/latest/APIReference/API_GetAggregateConformancePackComplianceSummary.html)
+ [GetAggregateDiscoveredResourceCounts](https://docs.aws.amazon.com/config/latest/APIReference/API_GetAggregateDiscoveredResourceCounts.html)
+ [GetAggregateResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_GetAggregateResourceConfig.html)
+ [ListAggregateDiscoveredResources](https://docs.aws.amazon.com/config/latest/APIReference/API_ListAggregateDiscoveredResources.html)
+ [PutConfigurationAggregator](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationAggregator.html)
+ [SelectAggregateResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_SelectAggregateResourceConfig.html)

For example, you can restrict access to resource data from specific users by creating two aggregators `AccessibleAggregator` and `InAccessibleAggregator` and attaching an IAM policy that allows access to `AccessibleAggregator` but denies access to `InAccessibleAggregator`\.

**IAM Policy for AccessibleAggregator**

In this policy, you allow access to the supported aggregator actions for the AWS Config Amazon Resource Name \(ARN\) that you specify\. In this example, the AWS Config ARN is `arn:aws:config:ap-northeast-1:AccountID:config-aggregator/config-aggregator-mocpsqhs`\.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ConfigAllow",
            "Effect": "Allow",
            "Action": [
                "config:BatchGetAggregateResourceConfig",
                "config:DeleteConfigurationAggregator",
                "config:DescribeAggregateComplianceByConfigRules",
                "config:DescribeAggregateComplianceByConformancePacks",
                "config:DescribeConfigurationAggregatorSourcesStatus",
                "config:GetAggregateComplianceDetailsByConfigRule",
                "config:GetAggregateConfigRuleComplianceSummary",
                "config:GetAggregateConformancePackComplianceSummary",
                "config:GetAggregateDiscoveredResourceCounts",
                "config:GetAggregateResourceConfig",
                "config:ListAggregateDiscoveredResources",
                "config:PutConfigurationAggregator",
                "config:SelectAggregateResourceConfig"
            ],
            "Resource": "arn:aws:config:ap-northeast-1:AccountID:config-aggregator/config-aggregator-mocpsqhs"
        }
    ]
}
```

**IAM Policy for InAccessibleAggregator**

In this policy, you deny access to the supported aggregator actions for the AWS Config ARN that you specify\. In this example, the AWS Config ARN is `arn:aws:config:ap-northeast-1:AccountID:config-aggregator/config-aggregator-pokxzldx`\.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ConfigDeny",
            "Effect": "Deny",
            "Action": [
                "config:BatchGetAggregateResourceConfig",
                "config:DeleteConfigurationAggregator",
                "config:DescribeAggregateComplianceByConfigRules",
                "config:DescribeAggregateComplianceByConformancePacks",
                "config:DescribeConfigurationAggregatorSourcesStatus",
                "config:GetAggregateComplianceDetailsByConfigRule",
                "config:GetAggregateConfigRuleComplianceSummary",
                "config:GetAggregateConformancePackComplianceSummary",
                "config:GetAggregateDiscoveredResourceCounts",
                "config:GetAggregateResourceConfig",
                "config:ListAggregateDiscoveredResources",
                "config:PutConfigurationAggregator",
                "config:SelectAggregateResourceConfig"
            ],
            "Resource": "arn:aws:config:ap-northeast-1:AccountID:config-aggregator/config-aggregator-pokxzldx"
        }
    ]
}
```

If a user of the developer group tries to perform any of these actions on the AWS Config ARN that you specified, that user will get an access denied exception\.

**Checking User Access Permissions**

To show the aggregators that you have created, run the following AWS CLI command:

```
aws configservice describe-configuration-aggregators
```

When command has successfully completed, you will be able to see the details for all the aggregators associated with your account\. In this example, those are `AccessibleAggregator` and `InAccessibleAggregator`:

```
{
    "ConfigurationAggregators": [
        {
            "ConfigurationAggregatorArn": "arn:aws:config:ap-northeast-1:AccountID:config-aggregator/config-aggregator-mocpsqhs",
            "CreationTime": 1517942461.442,
            "ConfigurationAggregatorName": "AccessibleAggregator",
            "AccountAggregationSources": [
                {
                    "AllAwsRegions": true,
                    "AccountIds": [
                        "AccountID1",
                        "AccountID2",
                        "AccountID3"
                    ]
                }
            ],
            "LastUpdatedTime": 1517942461.455
        },
        {
            "ConfigurationAggregatorArn": "arn:aws:config:ap-northeast-1:AccountID:config-aggregator/config-aggregator-pokxzldx",
            "CreationTime": 1517942461.442,
            "ConfigurationAggregatorName": "InAccessibleAggregator",
            "AccountAggregationSources": [
                {
                    "AllAwsRegions": true,
                    "AccountIds": [
                        "AccountID1",
                        "AccountID2",
                        "AccountID3"
                    ]
                }
            ],
            "LastUpdatedTime": 1517942461.455
        }
    ]
}
```

**Note**  
For `account-aggregation-sources` enter a comma\-separated list of AWS account IDs for which you want to aggregate data\. Wrap the account IDs in square brackets, and be sure to escape quotation marks \(for example, `"[{\"AccountIds\": [\"AccountID1\",\"AccountID2\",\"AccountID3\"],\"AllAwsRegions\": true}]"`\)\.

Attach the following IAM policy to deny access to `InAccessibleAggregator`, or the aggregator to which you want to deny access\.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ConfigDeny",
            "Effect": "Deny",
            "Action": [
                "config:BatchGetAggregateResourceConfig",
                "config:DeleteConfigurationAggregator",
                "config:DescribeAggregateComplianceByConfigRules",
                "config:DescribeAggregateComplianceByConformancePacks",
                "config:DescribeConfigurationAggregatorSourcesStatus",
                "config:GetAggregateComplianceDetailsByConfigRule",
                "config:GetAggregateConfigRuleComplianceSummary",
                "config:GetAggregateConformancePackComplianceSummary",
                "config:GetAggregateDiscoveredResourceCounts",
                "config:GetAggregateResourceConfig",
                "config:ListAggregateDiscoveredResources",
                "config:PutConfigurationAggregator",
                "config:SelectAggregateResourceConfig"
            ],
            "Resource": "arn:aws:config:ap-northeast-1:AccountID:config-aggregator/config-aggregator-pokxzldx"
        }
    ]
}
```

Next, you can confirm that the IAM policy works for restricting access to rules for a specific aggregator:

```
aws configservice get-aggregate-compliance-details-by-config-rule --configuration-aggregator-name InAccessibleAggregator --config-rule-name rule name --account-id AccountID --aws-region AwsRegion
```

The command should return an access denied exception:

```
An error occurred (AccessDeniedException) when calling the GetAggregateComplianceDetailsByConfigRule operation: User: arn:aws:iam::AccountID:user/ is not 
authorized to perform: config:GetAggregateComplianceDetailsByConfigRule on resource: arn:aws:config:AwsRegion-1:AccountID:config-aggregator/config-aggregator-pokxzldx
```

## Additional Information<a name="config-permissions-more-info"></a>

 To learn more about creating IAM users, groups, policies, and permissions, see [Creating Your First IAM User and Administrators Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/GSGHowToCreateAdminsGroup.html) and [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/PermissionsAndPolicies.html) in the *IAM User Guide*\. 