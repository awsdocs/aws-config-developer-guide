# codebuild\-project\-artifact\-encryption<a name="codebuild-project-artifact-encryption"></a>

Checks if an AWS CodeBuild project has encryption enabled for all of its artifacts\. The rule is NON\_COMPLIANT if ‘encryptionDisabled’ is set to ‘true’ for any primary or secondary \(if present\) artifact configurations\. 

**Identifier:** CODEBUILD\_PROJECT\_ARTIFACT\_ENCRYPTION

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w85aac12c32c17b9d115c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.