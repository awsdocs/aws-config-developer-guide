# eks\-cluster\-logging\-enabled<a name="eks-cluster-logging-enabled"></a>

Checks if an Amazon Elastic Kubernetes Service \(Amazon EKS\) cluster is configured with logging enabled\. The rule is NON\_COMPLIANT if logging for Amazon EKS clusters is not enabled for all log types\. 

**Identifier:** EKS\_CLUSTER\_LOGGING\_ENABLED

**Resource Types:** AWS::EKS::Cluster

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d281c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.