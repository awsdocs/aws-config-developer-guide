# Components of an AWS Config Rule<a name="evaluate-config_components"></a>

AWS Config rules evaluate the configuration settings of your AWS resources\. There are two types of rules: AWS Config Managed Rules and AWS Config Custom Rules\. Managed rules are predefined, customizable rules created by AWS Config\. For a list of managed rules, see [List of AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html)\.

Custom rules are rules that you can create using either Guard or AWS Lambda functions\. Guard \([Guard GitHub Repository](https://github.com/aws-cloudformation/cloudformation-guard)\) is a policy\-as\-code language that allows you to write policies that are enforced by AWS Config Custom Policy rules\. AWS Lambda uses custom code that you upload to evaluate a custom rule\. It is invoked by events that are published to it by an event source, which AWS Config invokes when the custom rule is initiated\.

This page discusses the structure of rule definitions and best practices on how to write rules with Python using the AWS Config Rules Development Kit \(RDK\) and AWS Config Rules Development Kit Library \(RDKlib\)\. For a walkthrough showing how to create AWS Config Custom Policy Rules, see [Creating AWS Config Custom Policy Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_cfn-guard.html)\. For a walkthrough showing how to create AWS Config Custom Lambda Rules, see [Creating AWS Config Custom Lambda Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_lambda-functions.html)\.

**Contents**
+ [Rule definitions](#evaluate-config_components_structure)
+ [Rule metadata](#evaluate-config_components_definitions)
+ [Rule structure](#evaluate-config_components_logic)
  + [Writing rules](#w85aac12c27c17b5)
  + [Rule logic](#evaluate-config_rule-logic)

## Rule definitions<a name="evaluate-config_components_structure"></a>

AWS Config Rule definitions contains the following fields:
+ **identifier**
+ **defaultName**
+ **description**
+ **scope**
+ **sourceDetails**
+ **compulsoryInputParameterDetails**
+ **optionalInputParameterDetails**
+ **labels**

The following JSON example shows the rule definition for the [codedeploy\-ec2\-minimum\-healthy\-hosts\-configured](https://docs.aws.amazon.com/config/latest/developerguide/codedeploy-ec2-minimum-healthy-hosts-configured.html) managed rule\.

```
{
  "identifier": "CODEDEPLOY_EC2_MINIMUM_HEALTHY_HOSTS_CONFIGURED",
  "defaultName": "codedeploy-ec2-minimum-healthy-hosts-configured", 
  "description": "Checks if the deployment group for EC2/On-Premises Compute Platform is configured with a minimum healthy hosts fleet percentage or host count greater than or equal to the input threshold. The rule is NON_COMPLIANT if either is below the threshold.",
  "scope": {
    "resourceTypes": [
      "AWS::CodeDeploy::DeploymentGroup"
    ]
  },
  "sourceDetails": [
    {
      "eventSource": "AWS_CONFIG",
      "messageType": "ConfigurationItemChangeNotification"
    },
    {
      "eventSource": "AWS_CONFIG",
      "messageType": "OversizedConfigurationItemChangeNotification"
    }
  ],
  "compulsoryInputParameterDetails": {},
  "optionalInputParameterDetails": {
    "minimumHealthyHostsFleetPercent": {
      "type": "int",
      "description": "Minimum percentage of healthy hosts fleet during deployment. Default value is set to 66 percent.",
      "defaultValue": "66"
    },
    "minimumHealthyHostsHostCount": {
      "type": "int",
      "description": "Minimum number of healthy hosts in fleet during deployment. Default value is set to 1.",
      "defaultValue": "1"
    }
  },
  "labels": [
    "CodeDeploy"
  ]
}
```

## Rule metadata<a name="evaluate-config_components_definitions"></a>

**identifier**  
The rule identifier functions as the ID for an AWS Config managed rule\. Rule identifiers are written in ALL\_CAPS\_WITH\_UNDERSCORES\. For example, `CODEDEPLOY_EC2_MINIMUM_HEALTHY_HOSTS_CONFIGURED` is the rule identifier and `codedeploy-ec2-minimum-healthy-hosts-configured` is the rule name\. The rule identifier is used to identify a rule when [Creating AWS Config Managed Rules With AWS CloudFormation Templates](https://docs.aws.amazon.com/config/latest/developerguide/aws-config-managed-rules-cloudformation-templates.html) or when calling the [PutConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html) API\.  
For some rules, the rule identifier is different from the rule name\. For example, the rule identifier for `restricted-ssh` is `INCOMING_SSH_DISABLED`\.

**defaultName**  
The defaultName is the name that instances of a rule will get by default\.

**description**  
The rule description provides context for what the rule evaluates\. The AWS Config Console has a limit of 256 characters\. As a best practice, the rule description should be with “Checks if” and include a description of the NON\_COMPLIANT scenario\. Service Names should be written in full beginning with AWS or Amazon when first mentioned in the rule description\. For example, AWS CloudTrail or Amazon CloudWatch instead of CloudTrail or CloudWatch for first use\. Services names can be abbreviated after subsequent reference\. 

**scope**  
The scope determines which resource types the rule targets\. This is required if the rule is change\-triggered or is both change\-triggered and periodic\. It is optional for periodic rules\. For a list of supported resource types, see [Supported Resource Types](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources.html)\.

**sourceDetails**  
The sourceDetails determine the rule's trigger type\. `ConfigurationItemChangeNotification` and `OversizedConfigurationItemChangeNotification` are used for change\-triggered rules\. When AWS Config detects a configuration change for a resource, it sends a configuration item notification\. If the notification exceeds the maximum size allowed by Amazon Simple Notification Service \(Amazon SNS\), the notification includes a brief summary of the configuration item\. You can view the complete notification in the S3 bucket location specified in the s3BucketLocation field\.  
`ScheduleNotification` is used for periodic rules\. If a rule is evaluated both periodically and by configuration changes, all three types of notifications can be used\. For more information, see [Specifying Triggers for AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html)

**compulsoryInputParameterDetails**  
The compulsoryInputParameterDetails are used for parameters that are required for a rule to do its evaluation\. For example, the `access-keys-rotated` managed rule includes `maxAccessKeyAge` as a required parameter\. If a parameter is required, it will not be marked as \(Optional\)\. For each parameter, a type must be specified\. Type can be one of "String", "int", "double", "CSV", "boolean" and "StringMap"\.

**optionalInputParameterDetails**  
The optionalInputParameterDetails are used for parameters that are optional for a rule to do its evaluation\. For example, the `codedeploy-ec2-minimum-healthy-hosts-configured` managed rule includes `minimumHealthyHostsFleetPercent` and `minimumHealthyHostsHostCount` as optional parameters\. For each parameter, a type must be specified\. Type can be one of "String", "int", "double", "CSV", "boolean" and "StringMap"\.

**labels**  
Labels can be used to tag rules\. For example, the `codedeploy-auto-rollback-monitor-enabled`, `codedeploy-ec2-minimum-healthy-hosts-configured`, and `codedeploy-lambda-allatonce-traffic-shift-disabled` managed rules all include the label `CodeDeploy`\.

## Rule structure<a name="evaluate-config_components_logic"></a>

This section contains information on using the AWS Config Rules Development Kit \(RDK\) and AWS Config Rules Development Kit Library \(RDKlib\)\. For more information on the RDK or RDKlib, see the [aws\-config\-rdk ](https://github.com/awslabs/aws-config-rdk) and [aws\-config\-rdklib](https://github.com/awslabs/aws-config-rdklib) GitHub Repositories\.

### Writing rules<a name="w85aac12c27c17b5"></a>

#### Prerequisites<a name="rule-logic-prereqs"></a>

1. Follow the steps in [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/installing.html)\.

1. Follow the steps in [Setting Up AWS Config with the Console](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html) or [Setting Up AWS Config with the AWS CLI](https://docs.aws.amazon.com/config/latest/developerguide/gs-cli.html)\. For information about the AWS Regions where AWS Config is supported, select your Region from the [AWS Regional Services list](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)\.

1. Install the RDK, using the recommended method with pip:

   ```
   pip install rdk
   ```
**Note**  
Before using pip, make sure it is installed on your machine\.

1. Install the RDKLib, using the recommended method with pip:

   ```
   pip install rdklib
   ```
**Note**  
Before using pip, make sure it is installed on your machine\.

#### Change\-triggered rules<a name="rule-logic-change-triggered"></a>

1. To create a rule that is triggered by a change to specified resource type, run the following command:

   ```
   rdk create YOUR_RULE_NAME --runtime python3.6-lib --resource-types AWS::Resource::Type
   ```

   The following example creates a rule that is triggered by a change to the `AWS::IAM::User` resource type:

   ```
   rdk create MFA_ENABLED_RULE --runtime python3.6-lib --resource-types AWS::IAM::User
   ```

   The following are the flags you can use with the `rdk create` command for change\-triggered rules:

   ```
   rdk create RULE_NAME 
       --runtime pythonX.X-lib // Python runtime version
       --input-parameters REQUIRED_PARAMETERS // Parameters that are required for a rule to do its evaluation
       --optional-parameters OPTIONAL_PARAMETERS // Parameters that are optional for a rule to do its evaluation
       --resource-types AWS::Resource::Type // Resource type(s) that the rule targets
   ```
**Note**  
To use the RDKLib, the runtime of the rule must be set to `python3.6-lib`\.

   After running `rdk create`, you should see a new directory with the rule name and 3 files in it:
   + `RULE_NAME.py` \- Python file where the rule logic is stored 
   + `RULE_NAME_test.py` \- Python file where the rule's unit tests is stored
   + `parameters.json` \- JSON file for RDK's deployment settings

1. The next step is writing the rule logic\. You will only need to edit the `RULE_NAME`\.py file\. If you open the `RULE_NAME`\.py file, you will see a template where you can add rule logic\. The following is the template that was generated for MFA\_ENABLED\_RULE:

   ```
   from rdklib import Evaluator, Evaluation, ConfigRule, ComplianceType
                               
   APPLICABLE_RESOURCES = ['AWS::IAM::User']
                               
   class MFA_ENABLED_RULE(ConfigRule):
   
       def evaluate_change(self, event, client_factory, configuration_item, valid_rule_parameters):
           ###############################
           # Add your custom logic here. #
           ###############################                       
                               
           return [Evaluation(ComplianceType.NOT_APPLICABLE)]
                               
       #def evaluate_periodic(self, event, client_factory, valid_rule_parameters):
       #    pass
                               
       def evaluate_parameters(self, rule_parameters):
           valid_rule_parameters = rule_parameters
           return valid_rule_parameters
                                                           
   ################################
   # DO NOT MODIFY ANYTHING BELOW #
   ################################
   def lambda_handler(event, context):
       my_rule = MFA_ENABLED_RULE()
       evaluator = Evaluator(my_rule, APPLICABLE_RESOURCES)
       return evaluator.handle(event, context)
   ```

   The following example is an edited version of the MFA\_ENABLED\_RULE template with the rule logic\. The rule checks if IAM users have multi\-factor authentication \(MFA\) enabled\. The rule is NON\_COMPLIANT if an IAM user does not have MFA not enabled\. For more information on rule logic and the methods provided in the template, see [Rule logic](#evaluate-config_rule-logic)\.

   ```
   from rdklib import ComplianceType, ConfigRule, Evaluation, Evaluator
   
   APPLICABLE_RESOURCES = ["AWS::IAM::User"]
   
   class MFA_ENABLED_RULE(ConfigRule):
           
       def evaluate_change(self, event, client_factory, configuration_item, valid_rule_parameters):
       
           username = configuration_item.get("resourceName")
           
           iam_client = client_factory.build_client("iam")
           
           response = iam_client.list_mfa_devices(UserName=username)
           
           # Scenario:1 IAM user has MFA enabled.
           if response["MFADevices"]:
               return [Evaluation(ComplianceType.COMPLIANT)]
               
           # Scenario:2 IAM user has MFA not enabled.
           annotation = "MFA needs to be enabled for user."
           return [Evaluation(ComplianceType.NON_COMPLIANT, annotation=annotation)]
           
       def evaluate_parameters(self, rule_parameters):
           valid_rule_parameters = rule_parameters
           return valid_rule_parameters
   
   ################################
   # DO NOT MODIFY ANYTHING BELOW #
   ################################
   def lambda_handler(event, context):
       my_rule = MFA_ENABLED_RULE()
       evaluator = Evaluator(my_rule, APPLICABLE_RESOURCES)
       return evaluator.handle(event, context)
   ```

1. The next step is installing the RDKlib layer in AWS with either the AWS Console or AWS CLI\. RDKLib is designed to work as an AWS Lambda Layer\. It allows you to use the library without needing to include it in your deployment package\.
   + To install the RDKlib layer with the AWS Console, do the following steps:

     1. Open the AWS Lambda console at [https://console\.aws\.amazon\.com/lambda/](https://console.aws.amazon.com/lambda/)\.

     1. Select **Create function**\.

     1. On the **Create function** page, select **Browse serverless app repository**, and in the search field, enter **rdklib**\.

     1. Review the function details and then deploy it\. You shouldn't have to make any changes\.

     1. On the left navigation pane, choose the **Layers** page\. Then choose the Lambda layer you just created, and copy the Amazon Resource Name \(ARN\) of the Lambda layer\. You will need the ARN of the Lambda layer when you deploy your rule\.
   + To install the RDKlib layer with the AWS CLI, run the following commands:

     1. Create the change set for the RDKlib\-Layer\.

        ```
        aws serverlessrepo create-cloud-formation-change-set --application-id arn:aws:serverlessrepo:ap-southeast-1:711761543063:applications/rdklib --stack-name RDKlib-Layer
        ```

        It returns the following output:

        ```
        {
            "ApplicationId": "arn:aws:serverlessrepo:ap-southeast-1:711761543063:applications/rdklib",
            "ChangeSetId": "arn:aws:cloudformation:us-east-1:123456789012:changeSet/a3d536322-585e-4ffd-9e2f-552c8b887d6f/ffe7ff5c-ab38-4ab9-b746-9c1617ca95c1",
            "SemanticVersion": "0.1.0",
            "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/serverlessrepo-RDKlib-Layer/365436a0-a58a-11ea-9b04-12ae8fb95b53"
        }
        ```

     1. Execute the change\-set\. You can copy/paste the full change\-set ARN \(ChangeSetId from the output generated in the previous step\) to customize the following command:

        ```
        aws cloudformation execute-change-set --change-set-name NAME_OF_THE_CHANGE_SET
        ```

     1. Return all the associated resources that are part of the deployed stack\.

        ```
        aws cloudformation describe-stack-resources --stack-name serverlessrepo-RDKlib-Layer
        ```

        It returns the following output:

        ```
        {
            "StackResources": [
                {
                    "StackName": "serverlessrepo-RDKlib-Layer",
                    "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/serverlessrepo-RDKlib-Layer/365436a0-a58a-11ea-9b04-12ae8fb95b53",
                    "LogicalResourceId": "RdklibLayercf22317faf",
                    "PhysicalResourceId": "arn:aws:lambda:us-east-1:123456789012:layer:rdklib-layer:1",
                    "ResourceType": "AWS::Lambda::LayerVersion",
                    "Timestamp": "2020-06-03T11:26:30.501Z",
                    "ResourceStatus": "CREATE_COMPLETE",
                    "DriftInformation": {
                        "StackResourceDriftStatus": "NOT_CHECKED"
                    }
                }
            ]
        }
        ```

     1. Copy the ARN of the Lambda layer from the output generated in the previous step\. The ARN of the Lambda layer is the `PhysicalResourceId`\.

        ```
        "PhysicalResourceId": "arn:aws:lambda:us-east-1:123456789012:layer:rdklib-layer:1"
        ```

1. The next step is providing a role for the Lambda function to assume\. By default, Lambda functions attempt to assume the `AWSServiceRoleForConfig` role, which is not allowed\. You need to create a role with the `AWS_ConfigRole` managed policy\. The role must have a trust relationship with AWS Config and all roles under the /rdk/ path should assume the role\. The following is an example trust policy:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Service": "config.amazonaws.com"
         },
         "Action": "sts:AssumeRole"
       },
       {
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::account-ID:root"
         },
         "Action": "sts:AssumeRole",
         "Condition": {
           "StringLike": {
             "aws:PrincipalArn": "arn:aws:iam::account-ID:role/rdk/*"
           }
         }
       }
     ]
   }
   ```

   Using this trust policy, run the following command:

   ```
   aws iam create-role --role-name your-role-name --assume-role-policy-document file://trust-policy.json
   ```

   Now, run the following command to update the input parameter for `ExecutionRoleName` and provide the role name:

   ```
   rdk modify YOUR_RULE_NAME --input-parameters '{"ExecutionRoleName":"your-role-name"}'
   ```

   You can also use `rdk modify` to update the change\-triggered rule details using the following flags:

   ```
   rdk modify RULE_NAME 
       --input-parameters REQUIRED_PARAMETERS // Parameters that are required for a rule to do its evaluation
       --optional-parameters OPTIONAL_PARAMETERS // Parameters that are optional for a rule to do its evaluation
       --resource-types AWS::Resource::Type // Resource type(s) that the rule targets
   ```

1. The final step is deploying your rule\. To deploy your rule, run the following command with the ARN of the Lambda layer from step 3:

   ```
   rdk deploy YOUR_RULE_NAME --rdklib-layer-arn YOUR_RDKLIB_LAYER_ARN
   ```

1. The rule is now deployed\. You can use the AWS Config Console to check if the rule is working as expected\.

#### Periodic rules<a name="rule-logic-periodic"></a>

1. To create a rule that is triggered periodically for a specified resource type, run the following command:

   ```
   rdk create YOUR_RULE_NAME --runtime python3.6-lib --resource-types AWS::Resource::Type --maximum-frequency EXECUTION_FREQUENCY
   ```

   The following example creates a rule that is triggered every 24 hours for the `AWS::IAM::User` resource type:

   ```
   rdk create MFA_ENABLED_RULE --runtime python3.6-lib --resource-types AWS::IAM::User --maximum-frequency TwentyFour_Hours
   ```

   The following are the flags you can use with the `rdk create` command for periodic rules:

   ```
   rdk create RULE_NAME 
       --runtime pythonX.X-lib // Python runtime version
       --input-parameters REQUIRED_PARAMETERS // Parameters that are required for a rule to do its evaluation
       --optional-parameters OPTIONAL_PARAMETERS // Parameters that are optional for a rule to do its evaluation
       --resource-types AWS::Resource::Type // Resource type(s) that the rule targets
       --maximum-frequency EXECUTION_FREQUENCY // How often the rule should be run on a periodic trigger.  One of ['One_Hour','Three_Hours','Six_Hours','Twelve_Hours','TwentyFour_Hours']
   ```
**Note**  
To use the RDKLib, the runtime of the rule must be set to `python3.6-lib`\.

   After running `rdk create`, you should see a new directory with the rule name and 3 files in it:
   + `RULE_NAME.py` \- Python file where the rule logic is stored 
   + `RULE_NAME_test.py` \- Python file where the rule's unit tests is stored
   + `parameters.json` \- JSON file for RDK's deployment settings

1. The next step is writing the rule logic\. You will only need to edit the `RULE_NAME`\.py file\. If you open the `RULE_NAME`\.py file, you will see a template where you can add rule logic\. The following is the template that was generated for MFA\_ENABLED\_RULE:

   ```
   from rdklib import Evaluator, Evaluation, ConfigRule, ComplianceType
                               
   APPLICABLE_RESOURCES = ['AWS::IAM::User']
                               
   class MFA_ENABLED_RULE(ConfigRule):
   
       def evaluate_change(self, event, client_factory, configuration_item, valid_rule_parameters):
           ###############################
           # Add your custom logic here. #
           ###############################                       
                               
           return [Evaluation(ComplianceType.NOT_APPLICABLE)]
                               
       #def evaluate_periodic(self, event, client_factory, valid_rule_parameters):
       #    pass
                               
       def evaluate_parameters(self, rule_parameters):
           valid_rule_parameters = rule_parameters
           return valid_rule_parameters
                                                           
   ################################
   # DO NOT MODIFY ANYTHING BELOW #
   ################################
   def lambda_handler(event, context):
       my_rule = MFA_ENABLED_RULE()
       evaluator = Evaluator(my_rule, APPLICABLE_RESOURCES)
       return evaluator.handle(event, context)
   ```

   The template defaults to change\-triggered rules\. Instead, add your logic to the `evaluate_periodic` method\. The following example is an edited version of the MFA\_ENABLED\_RULE template with the rule logic\. The rule checks if IAM users have multi\-factor authentication \(MFA\) enabled\. The rule is NON\_COMPLIANT if an IAM user does not have MFA not enabled\. For more information on rule logic and the methods provided in the template, see [Rule logic](#evaluate-config_rule-logic)\.

   ```
   from rdklib import ComplianceType, ConfigRule, Evaluation, Evaluator
   
   APPLICABLE_RESOURCES = ["AWS::IAM::User"]
   
   class MFA_ENABLED_RULE(ConfigRule):l
           
       def evaluate_periodic(self, event, client_factory, valid_rule_parameters):
           evaluations = []
           
           iam_client = client_factory.build_client("iam")
           
           paginator = iam_client.get_paginator("list_users")
           response_iterator = paginator.paginate()
           
           for response in response_iterator:
               for user in response["Users"]:
                   username = user["UserName"]
                   response = iam_client.list_mfa_devices(UserName=username)
                   
                   # Scenario:1 IAM user has MFA enabled.
                   if response["MFADevices"]:
                       evaluations.append(Evaluation(ComplianceType.COMPLIANT, username, "AWS::IAM::User"))
                       
                   # Scenario:2 IAM user has MFA not enabled.
                   if not response["MFADevices"]:
                       annotation = "MFA needs to be enabled for user."
                       evaluations.append(
                           Evaluation(ComplianceType.NON_COMPLIANT, username, "AWS::IAM::User", annotation=annotation)
                       )                  
           return evaluations
       
       def evaluate_parameters(self, rule_parameters):
           valid_rule_parameters = rule_parameters
           return valid_rule_parameters
   
   ################################
   # DO NOT MODIFY ANYTHING BELOW #
   ################################
   def lambda_handler(event, context):
       my_rule = MFA_ENABLED_RULE()
       evaluator = Evaluator(my_rule, APPLICABLE_RESOURCES)
       return evaluator.handle(event, context)
   ```

1. The next step is installing the RDKlib layer in AWS with either the AWS Console or AWS CLI\. RDKLib is designed to work as an AWS Lambda Layer\. It allows you to use the library without needing to include it in your deployment package\.
   + To install the RDKlib layer with the AWS Console, do the following steps:

     1. Open the AWS Lambda console at [https://console\.aws\.amazon\.com/lambda/](https://console.aws.amazon.com/lambda/)\.

     1. Select **Create function**\.

     1. On the **Create function** page, select **Browse serverless app repository**, and in the search field, enter **rdklib**\.

     1. Review the function details and then deploy it\. You shouldn't have to make any changes\.

     1. On the left navigation pane, choose the **Layers** page\. Then choose the Lambda layer you just created, and copy the Amazon Resource Name \(ARN\) of the Lambda layer\. You will need the ARN of the Lambda layer when you deploy your rule\.
   + To install the RDKlib layer with the AWS CLI, run the following commands:

     1. Create the change set for the RDKlib\-Layer\.

        ```
        aws serverlessrepo create-cloud-formation-change-set --application-id arn:aws:serverlessrepo:ap-southeast-1:711761543063:applications/rdklib --stack-name RDKlib-Layer
        ```

        It returns the following output:

        ```
        {
            "ApplicationId": "arn:aws:serverlessrepo:ap-southeast-1:711761543063:applications/rdklib",
            "ChangeSetId": "arn:aws:cloudformation:us-east-1:123456789012:changeSet/a3d536322-585e-4ffd-9e2f-552c8b887d6f/ffe7ff5c-ab38-4ab9-b746-9c1617ca95c1",
            "SemanticVersion": "0.1.0",
            "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/serverlessrepo-RDKlib-Layer/365436a0-a58a-11ea-9b04-12ae8fb95b53"
        }
        ```

     1. Execute the change\-set\. You can copy/paste the full change\-set ARN \(ChangeSetId from the output generated in the previous step\) to customize the following command:

        ```
        aws cloudformation execute-change-set --change-set-name NAME_OF_THE_CHANGE_SET
        ```

     1. Return all the associated resources that are part of the deployed stack\.

        ```
        aws cloudformation describe-stack-resources --stack-name serverlessrepo-RDKlib-Layer
        ```

        It returns the following output:

        ```
        {
            "StackResources": [
                {
                    "StackName": "serverlessrepo-RDKlib-Layer",
                    "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/serverlessrepo-RDKlib-Layer/365436a0-a58a-11ea-9b04-12ae8fb95b53",
                    "LogicalResourceId": "RdklibLayercf22317faf",
                    "PhysicalResourceId": "arn:aws:lambda:us-east-1:123456789012:layer:rdklib-layer:1",
                    "ResourceType": "AWS::Lambda::LayerVersion",
                    "Timestamp": "2020-06-03T11:26:30.501Z",
                    "ResourceStatus": "CREATE_COMPLETE",
                    "DriftInformation": {
                        "StackResourceDriftStatus": "NOT_CHECKED"
                    }
                }
            ]
        }
        ```

     1. Copy the ARN of the Lambda layer from the output generated in the previous step\. The ARN of the Lambda layer is the `PhysicalResourceId`\.

        ```
        "PhysicalResourceId": "arn:aws:lambda:us-east-1:123456789012:layer:rdklib-layer:1"
        ```

1. The next step is providing a role for the Lambda function to assume\. By default, Lambda functions attempt to assume the `AWSServiceRoleForConfig` role, which is not allowed\. You need to create a role with the `AWS_ConfigRole` managed policy\. The role must have a trust relationship with AWS Config and all roles under the /rdk/ path should assume the role\. The following is an example trust policy:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Service": "config.amazonaws.com"
         },
         "Action": "sts:AssumeRole"
       },
       {
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::account-ID:root"
         },
         "Action": "sts:AssumeRole",
         "Condition": {
           "StringLike": {
             "aws:PrincipalArn": "arn:aws:iam::account-ID:role/rdk/*"
           }
         }
       }
     ]
   }
   ```

   Using this trust policy, run the following command:

   ```
   aws iam create-role --role-name your-role-name --assume-role-policy-document file://trust-policy.json
   ```

   Now, run the following command to update the input parameter for `ExecutionRoleName` and provide the role name:

   ```
   rdk modify YOUR_RULE_NAME --input-parameters '{"ExecutionRoleName":"your-role-name"}'
   ```

   You can also use `rdk modify` to update the periodic rule details using the following flags:

   ```
   rdk modify RULE_NAME 
       --input-parameters REQUIRED_PARAMETERS // Parameters that are required for a rule to do its evaluation
       --optional-parameters OPTIONAL_PARAMETERS // Parameters that are optional for a rule to do its evaluation
       --resource-types AWS::Resource::Type // Resource type(s) that the rule targets
       --maximum-frequency EXECUTION_FREQUENCY // How often the rule should be run on a periodic trigger.  One of ['One_Hour','Three_Hours','Six_Hours','Twelve_Hours','TwentyFour_Hours']
   ```

1. The final step is deploying your rule\. To deploy your rule, run the following command with the ARN of the Lambda layer from step 3:

   ```
   rdk deploy YOUR_RULE_NAME --rdklib-layer-arn YOUR_RDKLIB_LAYER_ARN
   ```

1. The rule is now deployed\. You can use the AWS Config Console to check if the rule is working as expected\.

### Rule logic<a name="evaluate-config_rule-logic"></a>

The following Python code sample is a template for writing a rule using the RDK and RKDLib\. You should only make changes inside the `evaluate_parameters`, `evaluate_change`, and `evaluate_periodic` methods, or write completely new functions to help with the logic if needed\. For prerequistes to writing rules with the RDK and RDKlib, see [Prerequisites](#rule-logic-prereqs)\.

```
from rdklib import Evaluator, Evaluation, ConfigRule, ComplianceType

APPLICABLE_RESOURCES = ["AWS::Resource::Type"]

# When you create a rule, the class name will be the name you give the rule when you create it instead of ConfigRule
class ConfigRule (ConfigRule):

    def evaluate_parameters(self, rule_parameters):
        return rule_parameters

    def evaluate_change(self, event, client_factory, configuration_item, valid_rule_parameters):
        ###############################
        # Add your custom logic here. #
        ###############################

    def evaluate_periodic(self, event, client_factory, valid_rule_parameters):
        ###############################
        # Add your custom logic here. #
        ###############################
    
################################
# DO NOT MODIFY ANYTHING BELOW #
################################    
def lambda_handler(event, context):
    my_rule = ConfigRule()
    evaluator = Evaluator(my_rule, APPLICABLE_RESOURCES)
    return evaluator.handle(event, context)
```

**APPLICABLE\_RESOURCES**  
`APPLICABLE_RESOURCES` are the resource type\(s\) that the rule targets\. If used, this should be a global variable set to the resource type\(s\) that the rule targets\. For a list of supported resource types, see [Supported Resource Types](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources.html)\.

**evaluate\_parameters**  
**Description**  
This method is used to check if the input parameters for the rule are valid\. The following are best practices:  
+ Check if the correct number of parameters is listed\.
+ Check if the parameter name is correct\.
+ Check if the parameter value is of the correct type\.
+ If the parameter is an integer, check if the parameter is between a reasonable bounds\.
+ If the parameter has a limited number of possible options, check if the parameter is one of those options\.
+ If the parameter is a String, check if it is a reasonable length and trim any space before or after the value\.
+ Check if any case\-sensitivity is handled appropriately\.
+ Limit parameter input when possible\. For example, if you're receiving a comma\-separated list of ARNs, make sure that the only characters allowed are commas and the characters supported by ARNs\.
**Parameters**  
`rule_parameters` is a dictionary of input parameter\(s\) for the rule\.  
**Return syntax**  
If one of the parameters is not valid, you can raise an `InvalidParametersError` error:  

```
from rdklib import InvalidParametersError
raise InvalidParametersError("Error message to display")
```
If the parameters are all valid, the method should return a dictionary:  

```
return valid_rule_parameters
```

**evaluate\_change**  
**Description**  
This method is used for the logic to evaluate a change\-triggered rule\.  
**Parameters**  
`event` is the AWS Lambda event provided by AWS Config\. It is a JSON\-formatted document that contains data for a Lambda function to operate\. For examples, see [Example Events for AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_example-events.html)\.  
`client_factory` is the ClientFactory object to be used for the rule\. The ClientFactory class creates or reuses a boto3 client, which provides low\-level interface to an AWS service\. The boto3 client methods map with an AWS service API, which means that service operations map to client methods of the same name and provide access to the same operation parameters\. For a list of available services, see [Available services](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html) in the Boto3 Docs documentation\.  
The request syntax of `client_factory` is as follows:  

```
response = client_factory.build_client(
    service='string')
```
For example:   

```
iam_client = client_factory.build_client("iam")
```
The boto3 name of the AWS service is required\.
`configuration_item` is dictionary of the full configuration Item, even if oversized\. A configuration item represents a point\-in\-time view of the various attributes of a supported AWS resource\. For information on the contents of `ConfigurationItem`, see [ConfigurationItem](https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationItem.html) in the AWS Config API Reference\.  
`valid_rule_parameters` is the output of the `evaluate_parameters()` method\.  
**Return syntax**  
The method should return one or more of the following:  

```
[Evaluation(ComplianceType.COMPLIANT)]
```

```
[Evaluation(ComplianceType.NON_COMPLIANT)]
```

```
[Evaluation(ComplianceType.NOT_APPLICABLE)]
```
You should use annotations for all non\-compliant evaluations\. For example:  

```
[return [Evaluation(ComplianceType.NON_COMPLIANT, annotation="Explanation for why the rule is NON_COMPLIANT")]]
```

**evaluate\_periodic**  
**Description**  
This method is used to evaluate a periodic rule\.  
**Parameters**  
`event` is the AWS Lambda event provided by AWS Config\. It is a JSON\-formatted document that contains data for a Lambda function to operate\. For examples, see [Example Events for AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_example-events.html)\.  
`client_factory` is the ClientFactory object to be used for the rule\. The ClientFactory class creates or reuses a boto3 client, which provides low\-level interface to an AWS service\. The boto3 client methods map with an AWS service API, which means that service operations map to client methods of the same name and provide access to the same operation parameters\. For a list of available services, see [Available services](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html) in the Boto3 Docs documentation\.  
The request syntax of `client_factory` is as follows:  

```
response = client_factory.build_client(
    service='string')
```
For example:   

```
iam_client = client_factory.build_client("iam")
```
The boto3 name of the AWS service is required\.
`valid_rule_parameters` is the output of the `evaluate_parameters()` method\.  
**Return syntax**  
The method should return one or more of the following:  

```
[Evaluation(ComplianceType.COMPLIANT)]
```

```
[Evaluation(ComplianceType.NON_COMPLIANT)]
```

```
[Evaluation(ComplianceType.NOT_APPLICABLE)]
```
You should use annotations for all non\-compliant evaluations\. For example:  

```
[return [Evaluation(ComplianceType.NON_COMPLIANT, annotation="Explanation for why the rule is NON_COMPLIANT")]]
```

**lambda\_handler**  
**Description**  
You should not need to modify this method\. The lambda handler is used to processes events\. The function runs when AWS Lambda passes the `event` object to the `handler` method\. For more information, see [Lambda function handler in Python](https://docs.aws.amazon.com/lambda/latest/dg/python-handler.htm)\.  
**Parameters**  
`event` is the AWS Lambda event provided by AWS Config\. It is a JSON\-formatted document that contains data for a Lambda function to operate\. For examples, see [Example Events for AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_example-events.html)\.  
`context` is an object is passed to your function by Lambda at runtime\. This object provides methods and properties that provide information and methods that the function can use while it runs\. Note that in newer versions of Lambda, context is no longer used\.