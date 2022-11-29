# ecs\-task\-definition\-log\-configuration<a name="ecs-task-definition-log-configuration"></a>

Checks if logConfiguration is set on active ECS Task Definitions\. This rule is NON\_COMPLIANT if an active ECSTaskDefinition does not have the logConfiguration resource defined or the value for logConfiguration is null in at least one container definition\. 

**Identifier:** ECS\_TASK\_DEFINITION\_LOG\_CONFIGURATION

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Osaka\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c31c27b9d239c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.