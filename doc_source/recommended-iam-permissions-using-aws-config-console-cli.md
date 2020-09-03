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
                "iam:PassRole",
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

**Note**  
This policy grants broad permissions\. Before granting full access, consider starting with a minimum set of permissions and granting additional permissions as necessary\. Doing so is better practice than starting with permissions that are too lenient and then trying to tighten them later\.

## Controlling User Permissions for Actions on Multi\-Account Multi\-Region Data Aggregation<a name="resource-level-permission"></a>

You can use resource\-level permissions to control a user's ability to perform specific actions on multi\-account multi\-region data aggregation\. AWS Config multi\-account multi\-region data aggregation APIs support resource level permissions\. With resource level permission can restrict to access/modify the resource data to specific users\.

For example, you want to restrict access to resource data to specific users\.  You can create two aggregators `AccessibleAggregator` and `InAccessibleAggregator`\. Then attach an IAM policy that allows access to the `AccessibleAggregator`\. 

In the first policy, you allow the aggregator actions such as `DescribeConfigurationAggregators` and `DeleteConfigurationAggregator` actions for the config ARN that you specify\. In the following example, the config ARN is `arn:aws:config:ap-northeast-1:AccountID:config-aggregator/config-aggregator-mocpsqhs`\.

```
{
        "Version": "2012-10-17",
        "Statement": [
        {
        "Sid": "ConfigReadOnly",
        "Effect": "Allow",
        "Action": [
            "config:PutConfigurationAggregator",
            "config:DescribePendingAggregationRequests",
            "config:DeletePendingAggregationRequest",
            "config:GetAggregateConfigRuleComplianceSummary",
            "config:DescribeAggregateComplianceByConfigRules",
            "config:GetAggregateComplianceDetailsByConfigRule",
            "config:DescribeConfigurationAggregators",
            "config:DescribeConfigurationAggregatorSourcesStatus",
            "config:DeleteConfigurationAggregator"
        ],
        "Resource": "arn:aws:config:ap-northeast-1:AccountID:config-aggregator/config-aggregator-mocpsqhs"
        }
    ]
}
```

In the second policy, you deny the aggregator actions for the config ARN that you specify\. In the following example, the config ARN is `arn:aws:config:ap-northeast-1:AccountID:config-aggregator/config-aggregator-pokxzldx`\.

```
{
        "Version": "2012-10-17",
        "Statement": [
        {
        "Sid": "ConfigReadOnly",
        "Effect": "Deny",
        "Action": [
            "config:PutConfigurationAggregator",
            "config:DescribePendingAggregationRequests",
            "config:DeletePendingAggregationRequest",
            "config:GetAggregateConfigRuleComplianceSummary",
            "config:DescribeAggregateComplianceByConfigRules",
            "config:GetAggregateComplianceDetailsByConfigRule",
            "config:DescribeConfigurationAggregators",
            "config:DescribeConfigurationAggregatorSourcesStatus",
            "config:DeleteConfigurationAggregator"
        ],
        "Resource": "arn:aws:config:ap-northeast-1:AccountID:config-aggregator/config-aggregator-pokxzldx"
        }
    ]
}
```

If a user of the developer group tries to describe or delete configuration aggregators on the config that you specified in the second policy, that user gets an access denied exception\. 

The following AWS CLI examples show that the user creates two aggregators, `AccessibleAggregator` and `InAccessibleAggregator`\.

```
aws configservice describe-configuration-aggregators
```

The command complete successfully:

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
        }
    ]
}
```

```
{
    "ConfigurationAggregators": [
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

The user then creates an IAM policy that denies access to `InAccessibleAggregator`\.

```
{
        "Version": "2012-10-17",
        "Statement": [
        {
        "Sid": "ConfigReadOnly",
        "Effect": "Deny",
        "Action": [
            "config:PutConfigurationAggregator",
            "config:DescribePendingAggregationRequests",
            "config:DeletePendingAggregationRequest",
            "config:GetAggregateConfigRuleComplianceSummary",
            "config:DescribeAggregateComplianceByConfigRules",
            "config:GetAggregateComplianceDetailsByConfigRule",
            "config:DescribeConfigurationAggregators",
            "config:DescribeConfigurationAggregatorSourcesStatus",
            "config:DeleteConfigurationAggregator"
        ],
        "Resource": "arn:aws:config:ap-northeast-1:AccountID:config-aggregator/config-aggregator-pokxzldx"
        }
    ]
}
```

Next, the user confirms that IAM policy works for restricting access to specific aggregator and rules\.

```
aws configservice get-aggregate-compliance-details-by-config-rule --configuration-aggregator-name InAccessibleAggregator --config-rule-name rule name --account-id AccountID --aws-region AwsRegion
```

The command returns an access denied exception:

```
An error occurred (AccessDeniedException) when calling the GetAggregateComplianceDetailsByConfigRule operation: User: arn:aws:iam::AccountID:user/ is not 
authorized to perform: config:GetAggregateComplianceDetailsByConfigRule on resource: arn:aws:config:AwsRegion-1:AccountID:config-aggregator/config-aggregator-pokxzldx
```

With resource\-level permissions, you can grant or deny access to perform specific actions on multi\-account multi\-region data aggregation\.

## Additional Information<a name="config-permissions-more-info"></a>

 To learn more about creating IAM users, groups, policies, and permissions, see [Creating Your First IAM User and Administrators Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/GSGHowToCreateAdminsGroup.html) and [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/PermissionsAndPolicies.html) in the *IAM User Guide*\. 