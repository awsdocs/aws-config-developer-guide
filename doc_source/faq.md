# Frequently Asked Questions<a name="faq"></a>

## Indirect Relationships in AWS Config<a name="config-recording"></a>

**Topics**
+ [What is resource relationship?](#faq-1)
+ [What is a direct and an indirect relationship with respect to a resource?](#faq-2)
+ [Which indirect relationships does AWS Config support?](#faq-3)
+ [How are the configuration items created due to direct and indirect relationship?](#faq-4)
+ [What are the configuration items generated due to indirect relationships?](#faq-5)
+ [How do I retrieve configuration data related to indirect relationships?](#faq-6)

### What is resource relationship?<a name="faq-1"></a>

In AWS, resources refer to entities that are manageable, such as an Amazon Elastic Compute Cloud \(Amazon EC2\) instance, an AWS CloudFormation stack, or an Amazon S3 bucket\. AWS Config is a service that tracks and monitors resources by creating configuration items \(CIs\) whenever a change to a recorded resource type is detected\. For instance, when AWS Config is set up to track Amazon EC2 instances, it creates a configuration item every time an instance is created, updated, or deleted\. Each configuration item created by AWS Config has several fields, including `accountId`, `arn` \(Amazon Resource Name\), `awsRegion`, `configuration`, `tags`, and `relationships`\. The relationships field of a CI enables AWS Config to display how resources are linked to one another\. For instance, a relationship may indicate that an Amazon EBS volume with ID `vol-123ab45d` is attached to an Amazon EC2 instance with ID `i-a1b2c3d4`, which is associated with security group `sg-ef678hk`\.

### What is a direct and an indirect relationship with respect to a resource?<a name="faq-2"></a>

AWS Config derives the relationships for most resource types from the configuration field, which are called "direct" relationships\. A direct relationship is a one\-way connection \(A→B\) between a resource \(A\) and another resource \(B\), typically obtained from the describe API response of resource \(A\)\. In the past, for some resource types that AWS Config initially supported, it also captured relationships from the configurations of other resources, creating "indirect" relationships that are bidirectional \(B→A\)\. For example, the relationship between an Amazon EC2 instance and its security group is direct because the security groups are included in the describe API response for the Amazon EC2 instance\. On the other hand, the relationship between a security group and an Amazon EC2 instance is indirect because describing a security group does not return any information about the instances it is associated with\. As a result, when a resource configuration change is detected, AWS Config not only creates a CI for that resource, but also generates CIs for any related resources, including those with indirect relationships\. For example, when AWS Config detects changes in an Amazon EC2 instance, it creates a CI for the instance and a CI for the security group that is associated with the instance\.

### Which indirect relationships does AWS Config support?<a name="faq-3"></a>

The following indirect resource relationships are supported in AWS Config\.


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/faq.html)

### How are the configuration items created due to direct and indirect relationship?<a name="faq-4"></a>

For a direct relationship between resources \(A→B\), any configuration change to the resource B will initiate a configuration item \(CI\) for the resource A as well\. Similarly, for an indirect relationship \(B→A\), when there is a configuration change to resource A a new CI will be generated for resource B\. For example, Amazon EC2 instance to security group is a direct relationship so any configuration change to a security group would generate a CI for the security group as well as a CI for the EC2 instance\. Similarly, security group to Amazon EC2 instance is an indirect relationship so any configuration change to an EC2 instance would generate a CI for the Amazon EC2 instance as well as a CI for the security group\.

### What are the configuration items generated due to indirect relationships?<a name="faq-5"></a>

Below are the additional configuration items \(CIs\) generated due to indirect resource relationships\.


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/faq.html)

### How do I retrieve configuration data related to indirect relationships?<a name="faq-6"></a>

You can run Structured Query Language \(SQL\) queries in AWS Config Advanced Queries to retrieve configuration data related to indirect resource relationships\. For example, if you want to retrieve the list of Amazon EC2 instances related to a security group, use the following query:

```
SELECT
    resourceId,
    resourceType
    WHERE
    resourceType ='AWS::EC2::Instance' 
    AND
    relationships.resourceId = 'sg-234213'
```