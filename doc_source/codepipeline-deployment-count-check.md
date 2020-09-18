# codepipeline\-deployment\-count\-check<a name="codepipeline-deployment-count-check"></a>

Checks whether the first deployment stage of the AWS CodePipeline performs more than one deployment\. Optionally, checks if each of the subsequent remaining stages deploy to more than the specified number of deployments \(deploymentLimit\)\. The rule is NON\_COMPLIANT if the first stage in the AWS CodePipeline deploys to more than one region and the AWS CodePipeline deploys to more than the number specified in the `deploymentLimit`\. 

**Identifier:** CODEPIPELINE\_DEPLOYMENT\_COUNT\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Hong Kong\), Europe \(Stockholm\), Middle East \(Bahrain\), Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

 deploymentLimit  
The maximum number of deployments each stage can perform\.

## AWS CloudFormation template<a name="w22aac11c29c17c77c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.