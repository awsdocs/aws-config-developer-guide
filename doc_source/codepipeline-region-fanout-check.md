# codepipeline\-region\-fanout\-check<a name="codepipeline-region-fanout-check"></a>

Checks whether each stage in the AWS CodePipeline deploys to more than N times the number of the regions the AWS CodePipeline has deployed in all the previous combined stages, where N is the region fanout number\. The first deployment stage can deploy to a maximum of one region and the second deployment stage can deploy to a maximum number specified in the `regionFanoutFactor`\. If you do not provide a `regionFanoutFactor`, by default the value is three\. For example: If 1st deployment stage deploys to one region and 2nd deployment stage deploys to three regions, 3rd deployment stage can deploy to 12 regions, that is, sum of previous stages multiplied by the region fanout \(three\) number\. The rule is NON\_COMPLIANT if the deployment is in more than one region in 1st stage or three regions in 2nd stage or 12 regions in 3rd stage\.

**Identifier:** CODEPIPELINE\_REGION\_FANOUT\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Hong Kong\), Europe \(Stockholm\), Middle East \(Bahrain\), Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

 regionFanoutFactor  
 The number of regions the AWS CodePipeline has deployed to in all previous stages is the acceptable number of regions any stage can deploy to\.

## AWS CloudFormation template<a name="w22aac11c29c17c79c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.