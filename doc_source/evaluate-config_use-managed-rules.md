# AWS Config Managed Rules<a name="evaluate-config_use-managed-rules"></a>

AWS Config provides *AWS managed rules*, which are predefined, customizable rules that AWS Config uses to evaluate whether your AWS resources comply with common best practices\. For example, you could use a managed rule to quickly start assessing whether your Amazon Elastic Block Store \(Amazon EBS\) volumes are encrypted or whether specific tags are applied to your resources\. You can set up and activate these rules without writing the code to create an AWS Lambda function, which is required if you want to create custom rules\. The AWS Config console guides you through the process of configuring and activating a managed rule\. You can also use the AWS Command Line Interface or AWS Config API to pass the JSON code that defines your configuration of a managed rule\.

You can customize the behavior of a managed rule to suit your needs\. For example, you can define the rule's scope to constrain which resources trigger an evaluation for the rule, such as EC2 instances or volumes\. You can customize the rule's parameters to define attributes that your resources must have to comply with the rule\. For example, you can customize a parameter to specify that your security group should block incoming traffic to a specific port number\.

## Trigger Types<a name="evaluate-config_use-managed-rules-trigger"></a>

After you add a rule to your account, AWS Config compares your resources to the conditions of the rule\. After this initial evaluation, AWS Config continues to run evaluations each time one is triggered\. The evaluation triggers are defined as part of the rule, and they can include the following types:

**Configuration changes**  
AWS Config runs evaluations for the rule when there is a resource that matches the rule's scope and there is a change in configuration of the resource\. The evaluation runs after AWS Config sends a configuration item change notification\.  
You choose which resources initiate the evaluation by defining the rule's *scope*\. The scope can include the following:  
+ One or more resource types
+ A combination of a resource type and a resource ID
+ A combination of a tag key and value
+ When any recorded resource is created, updated, or deleted
AWS Config runs the evaluation when it detects a change to a resource that matches the rule's scope\. You can use the scope to define which resources initiate evaluations\.

**Periodic**  
AWS Config runs evaluations for the rule at a frequency that you choose; for example, every 24 hours\.

**Hybrid**  
Some rules have both configuration change and periodic triggers\. For these rules, AWS Config evaluates your resources when it detects a configuration change and also at the frequency that you specify\.   


## Evaluation modes<a name="evaluate-config_use-managed-rules-proactive-detective"></a>

There are two evaluation modes for AWS Config rules:

**Proactive**  
Use proactive evaluation to evaluate resources before they have been deployed\. This allows you to evaluate whether a set of resource properties, if used to define an AWS resource, would be COMPLIANT or NON\_COMPLIANT given the set of proactive rules that you have in your account in your Region\.  
For more information, see and [Evaluation modes](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html#aws-config-rules-evaluation-modes)\. For a list of managed rules that support proactive evaluation, see [List of AWS Config Managed Rules by Evaluation Mode](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-evaluation-mode.html)\.  
Proactive rules do not remediate resources that are flagged as NON\_COMPLIANT or prevent them from being deployed\.

**Detective**  
Use detective evaluation to evaluate resources that have already been deployed\. This allows you to evaluate the configuration settings of your existing resources\.

**Topics**
+ [Trigger Types](#evaluate-config_use-managed-rules-trigger)
+ [Evaluation modes](#evaluate-config_use-managed-rules-proactive-detective)
+ [List of AWS Config Managed Rules](managed-rules-by-aws-config.md)
+ [List of AWS Config Managed Rules by Evaluation Mode](managed-rules-by-evaluation-mode.md)
+ [List of AWS Config Managed Rules by Trigger Type](managed-rules-by-trigger-type.md)
+ [List of AWS Config Managed Rules by Region Availability](managing-rules-by-region-availability.md)
+ [Service\-Linked AWS Config Rules](service-linked-awsconfig-rules.md)
+ [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)