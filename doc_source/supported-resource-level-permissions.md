# Supported Resource\-Level Permissions for AWS Config Rules APIs Actions<a name="supported-resource-level-permissions"></a>

Resource\-level permissions refers to the ability to specify which resources users are allowed to perform actions on\. AWS Config supports resource\-level permissions for certain AWS Config Rules API actions\. This means that for certain AWS Config Rules actions, you can control when users are allowed to use those actions based on conditions that have to be fulfilled, or specific resources that users are allowed to use\. 

The following table describes the AWS Config Rules API actions that currently support resource\-level permissions, as well as the supported resources \(and their ARNs\) for each action\. When specifying an ARN, you can use the \* wildcard in your paths; for example, when you cannot or do not want to specify exact resource IDs\. 

**Important**  
If an AWS Config Rules API action is not listed in this table, then it does not support resource\-level permissions\. If an AWS Config Rules action does not support resource\-level permissions, you can grant users permissions to use the action, but you have to specify a \* for the resource element of your policy statement\. 


****  

| API Action | Resources | 
| --- | --- | 
| DeleteConfigRule | Config Rule arn:aws:config:*region:accountID*:config\-rule/config\-rule\-*ID* | 
| DeleteEvaluationResults | Config Rule arn:aws:config:*region:accountID*:config\-rule/config\-rule\-*ID* | 
| DescribeComplianceByConfigRule | Config Rule arn:aws:config:*region:accountID*:config\-rule/config\-rule\-*ID* | 
| DescribeConfigRuleEvaluationStatus | Config Rule arn:aws:config:*region:accountID*:config\-rule/config\-rule\-*ID* | 
| DescribeConfigRules | Config Rule arn:aws:config:*region:accountID*:config\-rule/config\-rule\-*ID* | 
| GetComplianceDetailsByConfigRule | Config Rule arn:aws:config:*region:accountID*:config\-rule/config\-rule\-*ID* | 
| PutConfigRule | Config Rule arn:aws:config:*region:accountID*:config\-rule/config\-rule\-*ID* | 
| StartConfigRulesEvaluation | Config Rule arn:aws:config:*region:accountID*:config\-rule/config\-rule\-*ID* | 
| PutRemediationConfigurations | Remediation Configuration arn:aws:config:*region:accountId*:remediation\-configuration/*config rule name/remediation configuration id* | 
| DescribeRemediationConfigurations | Remediation Configuration arn:aws:config:*region:accountId*:remediation\-configuration/*config rule name/remediation configuration id* | 
| DeleteRemediationConfiguration | Remediation Configuration arn:aws:config:*region:accountId*:remediation\-configuration/*config rule name/remediation configuration id* | 
| PutRemediationExceptions | Remediation Configuration arn:aws:config:*region:accountId*:remediation\-configuration/*config rule name/remediation configuration id* | 
| DescribeRemediationExceptions | Remediation Configuration arn:aws:config:*region:accountId*:remediation\-configuration/*config rule name/remediation configuration id* | 
| DeleteRemediationExceptions | Remediation Configuration arn:aws:config:*region:accountId*:remediation\-configuration/*config rule name/remediation configuration id* | 

For example, you want to allow read access and deny write access to specific rules to specific users\.

In the first policy, you allow the AWS Config Rules read actions such as `DescribeConfigRules` and `DescribeConfigRuleEvaluationStatus` on the specified rules\.

```
{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": [
                    "config:DescribeConfigRules",
                    "config:StartConfigRulesEvaluation",
                    "config:DescribeComplianceByConfigRule",
                    "config:DescribeConfigRuleEvaluationStatus",
                    "config:GetComplianceDetailsByConfigRule"
                ],
                "Resource": [
                    "arn:aws:config:region:accountID:config-rule/config-rule-ID",
                    "arn:aws:config:region:accountID:config-rule/config-rule-ID"
                ]
            }
        ]
    }
```

In the second policy, you deny the AWS Config Rules write actions on the specific rule\.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Deny",
            "Action": [
                "config:PutConfigRule",
                "config:DeleteConfigRule",
                "config:DeleteEvaluationResults"
               ],
            "Resource": "arn:aws:config:region:accountID:config-rule/config-rule-ID"
           }
      ]
   }
```

With resource\-level permissions, you can allow read access and deny write access to perform specific actions on AWS Config Rules API actions\. 