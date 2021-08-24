# autoscaling\-launch\-config\-public\-ip\-disabled<a name="autoscaling-launch-config-public-ip-disabled"></a>

Checks if Amazon EC2 Auto Scaling groups have public IP addresses enabled through Launch Configurations\. This rule is NON\_COMPLIANT if the Launch Configuration for an Auto Scaling group has AssociatePublicIpAddress set to 'true'\. 

**Identifier:** AUTOSCALING\_LAUNCH\_CONFIG\_PUBLIC\_IP\_DISABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Osaka\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w29aac11c33c17b7c35c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.