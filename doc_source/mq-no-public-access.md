# mq\-no\-public\-access<a name="mq-no-public-access"></a>

Checks if Amazon MQ brokers are not publicly accessible\. The rule is NON\_COMPLIANT if the 'PubliclyAccessible' field is set to true for an Amazon MQ broker\. 

**Identifier:** MQ\_NO\_PUBLIC\_ACCESS

**Resource Types:** AWS::AmazonMQ::Broker

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d411c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.