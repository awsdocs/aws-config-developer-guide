# ec2\-instance\-profile\-attached<a name="ec2-instance-profile-attached"></a>

Checks if an Amazon Elastic Compute Cloud \(Amazon EC2\) instance has an Identity and Access Management \(IAM\) profile attached to it\. This rule is NON\_COMPLIANT if no IAM profile is attached to the Amazon EC2 instance\. 

**Identifier:** EC2\_INSTANCE\_PROFILE\_ATTACHED

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

IamInstanceProfileArnList \(Optional\)Type: CSV  
Comma\-separated list of IAM profile Amazon Resource Names \(ARNs\) that can be attached to Amazon EC2 instances\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d203c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.