# eks\-cluster\-oldest\-supported\-version<a name="eks-cluster-oldest-supported-version"></a>

Checks if an Amazon Elastic Kubernetes Service \(EKS\) cluster is running the oldest supported version\. The rule is NON\_COMPLIANT if an EKS cluster is running oldest supported version \(equal to the parameter '`oldestVersionSupported`'\)\. 

**Identifier:** EKS\_CLUSTER\_OLDEST\_SUPPORTED\_VERSION

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Osaka\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

oldestVersionSupportedType: String  
Value of the oldest version of Kubernetes supported on AWS\.

## AWS CloudFormation template<a name="w2aac12c31c27b9d263c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.