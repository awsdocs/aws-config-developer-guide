# ecr\-private\-tag\-immutability\-enabled<a name="ecr-private-tag-immutability-enabled"></a>

Checks if a private Amazon Elastic Container Registry \(ECR\) repository has tag immutability enabled\. This rule is NON\_COMPLIANT if tag immutability is not enabled for the private ECR repository\. 

**Identifier:** ECR\_PRIVATE\_TAG\_IMMUTABILITY\_ENABLED

**Resource Types:** AWS::ECR::Repository

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d233c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.