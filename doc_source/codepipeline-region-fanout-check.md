# codepipeline\-region\-fanout\-check<a name="codepipeline-region-fanout-check"></a>

Checks whether each stage in the AWS CodePipeline deploys to more regions than N times the number of regions the pipeline has deployed to in all previous stages, where N is `regionFanoutFactor`\. The first deployment stage can deploy to only one region\. 

**Identifier:** CODEPIPELINE\_REGION\_FANOUT\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Hong Kong\), Europe \(Milan\), Europe \(Stockholm\), Middle East \(Bahrain\), Africa \(Cape Town\) Region

**Parameters:**

regionFanoutFactor \(Optional\)Type: intDefault: 3  
regionFanoutFactor \* the number of regions the AWS CodePipeline has deployed to in all previous stages is the maximum number of regions any stage can deploy to\.

## AWS CloudFormation template<a name="w24aac11c29c17b7c79c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.