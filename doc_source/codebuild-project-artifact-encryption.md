# codebuild\-project\-artifact\-encryption<a name="codebuild-project-artifact-encryption"></a>

Checks if an AWS CodeBuild project has encryption enabled for all of its artifacts\. The rule is NON\_COMPLIANT if 'encryptionDisabled' is set to 'true' for any primary or secondary \(if present\) artifact configurations\. 

**Identifier:** CODEBUILD\_PROJECT\_ARTIFACT\_ENCRYPTION

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Osaka\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c31c27b9d115c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.