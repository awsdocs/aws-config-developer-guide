# ecs\-no\-environment\-secrets<a name="ecs-no-environment-secrets"></a>

Checks if secrets are passed as container environment variables\. The rule is NON\_COMPLIANT if 1 or more environment variable key matches a key listed in the '`secretKeys`' parameter \(excluding environmental variables from other locations such as Amazon S3\)\. 

**Identifier:** ECS\_NO\_ENVIRONMENT\_SECRETS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Osaka\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

secretKeysType: CSV  
Comma\-separated list of key names to search for in the environment variables of container definitions within Task Definitions\. Extra spaces will be removed\.

## AWS CloudFormation template<a name="w2aac12c31c27b9d237c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.