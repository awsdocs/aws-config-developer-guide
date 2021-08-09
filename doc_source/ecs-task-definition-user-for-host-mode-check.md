# ecs\-task\-definition\-user\-for\-host\-mode\-check<a name="ecs-task-definition-user-for-host-mode-check"></a>

Checks if an Amazon Elastic Container Service \(Amazon ECS\) task definition with host networking mode has 'privileged' or 'user' container definitions\. The rule is NON\_COMPLIANT for task definitions with host network mode and container definitions of privileged=false or empty and user=root or empty\.

**Identifier:** ECS\_TASK\_DEFINITION\_USER\_FOR\_HOST\_MODE\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Osaka\) Region

**Parameters:**

SkipInactiveTaskDefinitions \(Optional\)Type: boolean  
This rule will evaluate all Amazon ECS Task Definitions if the value is 'false'\. The rule does not evaluate INACTIVE ECS Task Definitions if the value is 'true'\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d149c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.