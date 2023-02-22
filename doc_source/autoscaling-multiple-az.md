# autoscaling\-multiple\-az<a name="autoscaling-multiple-az"></a>

Checks if the Auto Scaling group spans multiple Availability Zones\. The rule is NON\_COMPLIANT if the Auto Scaling group does not span multiple Availability Zones\. 

**Identifier:** AUTOSCALING\_MULTIPLE\_AZ

**Resource Types:** AWS::AutoScaling::AutoScalingGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

minAvailabilityZones \(Optional\)Type: int  
Minimum number of expected Availability zones\.

## AWS CloudFormation template<a name="w2aac12c33c15b9c53c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.