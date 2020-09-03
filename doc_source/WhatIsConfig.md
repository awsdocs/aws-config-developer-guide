# What Is AWS Config?<a name="WhatIsConfig"></a>

AWS Config provides a detailed view of the configuration of AWS resources in your AWS account\. This includes how the resources are related to one another and how they were configured in the past so that you can see how the configurations and relationships change over time\. 

An AWS *resource* is an entity you can work with in AWS, such as an Amazon Elastic Compute Cloud \(EC2\) instance, an Amazon Elastic Block Store \(EBS\) volume, a security group, or an Amazon Virtual Private Cloud \(VPC\)\. For a complete list of AWS resources supported by AWS Config, see [Supported Resource Types](resource-config-reference.md)\.

With AWS Config, you can do the following:
+ Evaluate your AWS resource configurations for desired settings\.
+ Get a snapshot of the current configurations of the supported resources that are associated with your AWS account\.
+ Retrieve configurations of one or more resources that exist in your account\.
+ Retrieve historical configurations of one or more resources\.
+ Receive a notification whenever a resource is created, modified, or deleted\.
+ View relationships between resources\. For example, you might want to find all resources that use a particular security group\.

## Ways to Use AWS Config<a name="common-scenarios"></a>

When you run your applications on AWS, you usually use AWS resources, which you must create and manage collectively\. As the demand for your application keeps growing, so does your need to keep track of your AWS resources\. AWS Config is designed to help you oversee your application resources in the following scenarios: 

### Resource Administration<a name="scenarios-resource-administration"></a>

To exercise better governance over your resource configurations and to detect resource misconfigurations, you need fine\-grained visibility into what resources exist and how these resources are configured at any time\. You can use AWS Config to notify you whenever resources are created, modified, or deleted without having to monitor these changes by polling the calls made to each resource\.

You can use AWS Config rules to evaluate the configuration settings of your AWS resources\. When AWS Config detects that a resource violates the conditions in one of your rules, AWS Config flags the resource as noncompliant and sends a notification\. AWS Config continuously evaluates your resources as they are created, changed, or deleted\.

### Auditing and Compliance<a name="scenarios-auditing-and-compliance"></a>

You might be working with data that requires frequent audits to ensure compliance with internal policies and best practices\. To demonstrate compliance, you need access to the historical configurations of your resources\. This information is provided by AWS Config\.

### Managing and Troubleshooting Configuration Changes<a name="scenarios-managing-and-troubleshooting-configuration-changes"></a>

When you use multiple AWS resources that depend on one another, a change in the configuration of one resource might have unintended consequences on related resources\. With AWS Config, you can view how the resource you intend to modify is related to other resources and assess the impact of your change\. 

You can also use the historical configurations of your resources provided by AWS Config to troubleshoot issues and to access the last known good configuration of a problem resource\.

### Security Analysis<a name="w22aab5c10c10"></a>

To analyze potential security weaknesses, you need detailed historical information about your AWS resource configurations, such as the AWS Identity and Access Management \(IAM\) permissions that are granted to your users, or the Amazon EC2 security group rules that control access to your resources\.

You can use AWS Config to view the IAM policy that was assigned to an IAM user, group, or role at any time in which AWS Config was recording\. This information can help you determine the permissions that belonged to a user at a specific time: for example, you can view whether the user `John Doe` had permission to modify Amazon VPC settings on Jan 1, 2015\.

You can also use AWS Config to view the configuration of your EC2 security groups, including the port rules that were open at a specific time\. This information can help you determine whether a security group blocked incoming TCP traffic to a specific port\.