# AWS Config Managed Rules<a name="evaluate-config_use-managed-rules"></a>

AWS Config provides *AWS managed rules*, which are predefined, customizable rules that AWS Config uses to evaluate whether your AWS resources comply with common best practices\. For example, you could use a managed rule to quickly start assessing whether your Amazon Elastic Block Store \(Amazon EBS\) volumes are encrypted or whether specific tags are applied to your resources\. You can set up and activate these rules without writing the code to create an AWS Lambda function, which is required if you want to create custom rules\. The AWS Config console guides you through the process of configuring and activating a managed rule\. You can also use the AWS Command Line Interface or AWS Config API to pass the JSON code that defines your configuration of a managed rule\.

You can customize the behavior of a managed rule to suit your needs\. For example, you can define the rule's scope to constrain which resources trigger an evaluation for the rule, such as EC2 instances or volumes\. You can customize the rule's parameters to define attributes that your resources must have to comply with the rule\. For example, you can customize a parameter to specify that your security group should block incoming traffic to a specific port number\.

After you activate a rule, AWS Config compares your resources to the conditions of the rule\. After this initial evaluation, AWS Config continues to run evaluations each time one is triggered\. The evaluation triggers are defined as part of the rule, and they can include the following types:
+ **Configuration changes** – AWS Config triggers the evaluation when any resource that matches the rule's scope changes in configuration\. The evaluation runs after AWS Config sends a configuration item change notification\.
+ **Periodic** – AWS Config runs evaluations for the rule at a frequency that you choose \(for example, every 24 hours\)\.

The AWS Config console shows which resources comply with the rule and which rules are being followed\. For more information, see [Viewing Configuration Compliance](evaluate-config_view-compliance.md)\.

**Topics**
+ [List of AWS Config Managed Rules](managed-rules-by-aws-config.md)
+ [Working with AWS Config Managed Rules](managing-aws-managed-rules.md)
+ [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)