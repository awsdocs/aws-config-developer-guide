# ec2\-imdsv2\-check<a name="ec2-imdsv2-check"></a>

Checks whether your Amazon Elastic Compute Cloud \(Amazon EC2\) instance metadata version is configured with Instance Metadata Service Version 2 \(IMDSv2\)\. The rule is COMPLIANT if the HttpTokens is set to required and is NON\_COMPLIANT if the HttpTokens is set to optional\. 

**Identifier:** EC2\_IMDSV2\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except Europe \(Milan\), Africa \(Cape Town\) Regions

**Parameters:**

None  

## AWS CloudFormation template<a name="w22aac11c29c17d151c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.