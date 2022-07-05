# Creating AWS Config Custom Policy Rules<a name="evaluate-config_develop-rules_cfn-guard"></a>

You can create AWS Config Custom Policy rules from the AWS Management Console, AWS CLI, or AWS Config API\. For more information on how to write rules with Guard, see [Writing Guard rules](https://docs.aws.amazon.com/cfn-guard/latest/ug/writing-rules.html) in the AWS CloudFormation Guard User Guide\. For more information on the schemas of supported resource types that AWS Config can evalute, see [resource\-types](https://github.com/awslabs/aws-config-resource-schema/tree/master/config/properties/resource-types) in the AWS Config Resource Schema GitHub Repository\.

## Creating AWS Config Custom Policy Rules \(Console\)<a name="create-cfn-guard-rule-console"></a>

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. In the AWS Management Console menu, verify that the Region selector is set to an AWS Region that supports AWS Config rules\. For the list of supported Regions, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/awsconfig.html) in the *Amazon Web Services General Reference*\. 

1. In the left navigation, choose **Rules**\. 

1. On the **Rules** page, choose **Add rule**\. 

1. On the **Specify rule type** page, choose **Create custom rule using Guard**\.

1. On the **Configure rule** page, create your rule by completing the following steps:

   1. For **Rule name**, type a unique name for the rule\.

   1. For **Description**, type a description for the rule\.

   1. For **Guard runtime version**, choose the runtime system for your AWS Config Custom Policy rule\.

   1. For **Rule Content**, you can populate it with the Guard Custom policy for your rule\. For more information about the structure and features for Guard Custom policies, see the [AWS CloudFormation Guard 2\.0's Modes of Operation](https://github.com/aws-cloudformation/cloudformation-guard/tree/main/guard) in the Guard GitHub Repository\.

      The following example shows the policy definition for an AWS Config Custom Policy rule version of the AWS Config Managed rule [dynamodb\-pitr\-enabled](dynamodb-pitr-enabled.md)

      ```
      # This rule checks if point in time recovery (PITR) is enabled on active Amazon DynamoDB tables
      let status = ['ACTIVE']
      
      rule tableisactive when
          resourceType == "AWS::DynamoDB::Table" {
          configuration.tableStatus == %status
      }
      
      rule checkcompliance when
          resourceType == "AWS::DynamoDB::Table"
          tableisactive {
              let pitr = supplementaryConfiguration.ContinuousBackupsDescription.pointInTimeRecoveryDescription.pointInTimeRecoveryStatus
              %pitr == "ENABLED"
      }
      ```

   1. For **Trigger**, AWS Config Custom Policy rules are initiated by **Configuration changes**\. This option will be pre\-selected\.

      Specify one of the following options for **Scope of changes**:
      +  **Resources** – When a resource that matches the specified resource type, or the type plus identifier, is created, changed, or deleted\.
      +  **Tags** – When a resource with the specified tag is created, changed, or deleted\.
      +  **All changes** – When a resource recorded by AWS Config is created, changed, or deleted\.

   1. If your rule includes parameters, in the **Rule parameters** section you can customize the values for the provided keys\. A parameter is an attribute that your resources must have before they are considered COMPLIANT with the rule\.

1. After you finish editing your rule, choose **Next**\. On the **Review and create** page, you can review all your editing choices before adding the rule to your AWS account\.

1. When you finish reviewing your rules, choose **Add rule**\.

## Creating AWS Config Custom Policy Rules \(AWS CLI\)<a name="create-cfn-guard-rule-cli"></a>

Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/put-config-rule.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/put-config-rule.html) command\.

The `Owner` field should be `CUSTOM_POLICY`\. The following additional fields are required for AWS Config Custom Policy rules:
+ `Runtime`: The runtime system for your AWS Config Custom Policy rules\.
+ `PolicyText`: The policy definition containing the logic for your AWS Config Custom Policy rules\.
+ `EnableDebugLogDelivery`: The Boolean expression for enabling debug logging for your AWS Config Custom Policy rule\. The default value is `false`\.

## Creating AWS Config Custom Policy Rules \(API\)<a name="create-cfn-guard-rule-api"></a>

Use the [PutConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html) action\.

The `Owner` field should be `CUSTOM_POLICY`\. The following additional fields are required for AWS Config Custom Policy rules:
+ `Runtime`: The runtime system for your AWS Config Custom Policy rules\.
+ `PolicyText`: The policy that defines the logic for your AWS Config Custom Policy rules\.
+ `EnableDebugLogDelivery`: The Boolean expression for enabling debug logging for your AWS Config Custom Policy rule\. The default value is `false`\.