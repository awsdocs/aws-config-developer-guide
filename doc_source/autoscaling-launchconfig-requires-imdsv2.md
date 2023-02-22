# autoscaling\-launchconfig\-requires\-imdsv2<a name="autoscaling-launchconfig-requires-imdsv2"></a>

Checks whether only IMDSv2 is enabled\. This rule is NON\_COMPLIANT if the Metadata version is not included in the launch configuration or if both Metadata V1 and V2 are enabled\. 

**Identifier:** AUTOSCALING\_LAUNCHCONFIG\_REQUIRES\_IMDSV2

**Resource Types:** AWS::AutoScaling::LaunchConfiguration

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9c45c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.