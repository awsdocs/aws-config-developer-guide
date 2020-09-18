# desired\-instance\-type<a name="desired-instance-type"></a>

Checks whether your EC2 instances are of the specified instance types\.

For a list of supported Amazon EC2 instance types, see [Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide for Linux Instances*\.

**Identifier:** DESIRED\_INSTANCE\_TYPE

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions

**Parameters:**

 instanceType   
 Comma\-separated list of EC2 instance types \(for example, "t2\.small, m4\.large, i2\.xlarge"\)\.

## AWS CloudFormation template<a name="w22aac11c29c17c89c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.