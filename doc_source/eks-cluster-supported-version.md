# eks\-cluster\-supported\-version<a name="eks-cluster-supported-version"></a>

Checks if an Amazon Elastic Kubernetes Service \(EKS\) cluster is running a supported Kubernetes version\. This rule is NON\_COMPLIANT if an EKS cluster is running an unsupported version \(less than the parameter '`oldestVersionSupported`'\)\. 

**Identifier:** EKS\_CLUSTER\_SUPPORTED\_VERSION

**Resource Types:** AWS::EKS::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

oldestVersionSupportedType: String  
Value of the oldest version of Kubernetes supported on AWS\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d273c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.