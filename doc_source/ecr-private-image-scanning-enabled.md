# ecr\-private\-image\-scanning\-enabled<a name="ecr-private-image-scanning-enabled"></a>

Checks if a private Amazon Elastic Container Registry \(ECR\) repository has image scanning enabled\. The rule is NON\_COMPLIANT if the private ECR repository's scan frequency is not on scan on push or continuous scan\. 

**Identifier:** ECR\_PRIVATE\_IMAGE\_SCANNING\_ENABLED

**Resource Types:** AWS::ECR::Repository

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d239c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.