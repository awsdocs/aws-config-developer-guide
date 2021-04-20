# codepipeline\-deployment\-count\-check<a name="codepipeline-deployment-count-check"></a>

Checks whether the first deployment stage of the AWS Codepipeline performs more than one deployment\. Optionally checks if each of the subsequent remaining stages deploy to more than the specified number of deployments \(`deploymentLimit`\)\. 

**Identifier:** CODEPIPELINE\_DEPLOYMENT\_COUNT\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Hong Kong\), Asia Pacific \(Osaka\), Europe \(Milan\), Europe \(Stockholm\), Middle East \(Bahrain\), Africa \(Cape Town\) Region

**Parameters:**

deploymentLimit \(Optional\)Type: int  
The maximum number of deployments each stage can perform\.

## AWS CloudFormation template<a name="w29aac11c33c17b7c79c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.