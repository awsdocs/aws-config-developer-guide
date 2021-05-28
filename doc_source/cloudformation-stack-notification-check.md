# cloudformation\-stack\-notification\-check<a name="cloudformation-stack-notification-check"></a>

Checks whether your CloudFormation stacks are sending event notifications to an SNS topic\. Optionally checks whether specified SNS topics are used\. 

**Identifier:** CLOUDFORMATION\_STACK\_NOTIFICATION\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Hong Kong\), Asia Pacific \(Osaka\), Europe \(Milan\), Europe \(Paris\), Europe \(Stockholm\), Middle East \(Bahrain\), Africa \(Cape Town\) Region

**Parameters:**

snsTopic1 \(Optional\)Type: String  
SNS Topic ARN\.

snsTopic2 \(Optional\)Type: String  
SNS Topic ARN\.

snsTopic3 \(Optional\)Type: String  
SNS Topic ARN\.

snsTopic4 \(Optional\)Type: String  
SNS Topic ARN\.

snsTopic5 \(Optional\)Type: String  
SNS Topic ARN\.

## AWS CloudFormation template<a name="w29aac11c33c17b7c37c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.