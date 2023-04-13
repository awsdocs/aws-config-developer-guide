# autoscaling\-launch\-config\-hop\-limit<a name="autoscaling-launch-config-hop-limit"></a>

Checks the number of network hops that the metadata token can travel\. This rule is NON\_COMPLIANT if the Metadata response hop limit is greater than 1\. 

**Identifier:** AUTOSCALING\_LAUNCH\_CONFIG\_HOP\_LIMIT

**Resource Types:** AWS::AutoScaling::LaunchConfiguration

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), China \(Ningxia\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9c55c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.