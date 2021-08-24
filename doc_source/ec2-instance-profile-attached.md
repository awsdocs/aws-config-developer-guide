# ec2\-instance\-profile\-attached<a name="ec2-instance-profile-attached"></a>

Checks if an Amazon Elastic Compute Cloud \(Amazon EC2\) instance has an Identity and Access Management \(IAM\) profile attached to it\. This rule is NON\_COMPLIANT if no IAM profile is attached to the Amazon EC2 instance\. 

**Identifier:** EC2\_INSTANCE\_PROFILE\_ATTACHED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Osaka\) Region

**Parameters:**

IamInstanceProfileArnList \(Optional\)Type: CSV  
Comma\-separated list of IAM profile Amazon Resource Names \(ARNs\) that can be attached to Amazon EC2 instances\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d143c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.