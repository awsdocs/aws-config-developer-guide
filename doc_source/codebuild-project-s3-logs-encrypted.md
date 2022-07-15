# codebuild\-project\-s3\-logs\-encrypted<a name="codebuild-project-s3-logs-encrypted"></a>

Checks if a AWS CodeBuild project configured with Amazon S3 Logs has encryption enabled for its logs\. The rule is NON\_COMPLIANT if ‘encryptionDisabled’ is set to ‘true’ in a S3LogsConfig of a CodeBuild project\. 

**Identifier:** CODEBUILD\_PROJECT\_S3\_LOGS\_ENCRYPTED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\) Region

**Parameters:**

exemptedProjects \(Optional\)Type: CSV  
Comma\-separated list of CodeBuild project names that are allowed to output unencrypted logs\.

## AWS CloudFormation template<a name="w79aac11c32c17b9d123c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.