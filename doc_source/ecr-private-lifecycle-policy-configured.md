# ecr\-private\-lifecycle\-policy\-configured<a name="ecr-private-lifecycle-policy-configured"></a>

Checks if a private Amazon Elastic Container Registry \(ECR\) repository has at least one lifecycle policy configured\. The rule is NON\_COMPLIANT if no lifecycle policy is configured for the ECR private repository\. 

**Identifier:** ECR\_PRIVATE\_LIFECYCLE\_POLICY\_CONFIGURED

**Resource Types:** AWS::ECR::Repository

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d241c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.