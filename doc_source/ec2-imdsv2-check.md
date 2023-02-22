# ec2\-imdsv2\-check<a name="ec2-imdsv2-check"></a>

Checks whether your Amazon Elastic Compute Cloud \(Amazon EC2\) instance metadata version is configured with Instance Metadata Service Version 2 \(IMDSv2\)\. The rule is NON\_COMPLIANT if the HttpTokens is set to optional\. 

**Identifier:** EC2\_IMDSV2\_CHECK

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d183c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.