# autoscaling\-launch\-config\-public\-ip\-disabled<a name="autoscaling-launch-config-public-ip-disabled"></a>

Checks if Amazon EC2 Auto Scaling groups have public IP addresses enabled through Launch Configurations\. This rule is NON\_COMPLIANT if the Launch Configuration for an Auto Scaling group has AssociatePublicIpAddress set to 'true'\. 

**Identifier:** AUTOSCALING\_LAUNCH\_CONFIG\_PUBLIC\_IP\_DISABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c31c27b9c45c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.