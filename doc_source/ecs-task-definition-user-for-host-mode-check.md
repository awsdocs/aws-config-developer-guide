# ecs\-task\-definition\-user\-for\-host\-mode\-check<a name="ecs-task-definition-user-for-host-mode-check"></a>

Checks if an Amazon Elastic Container Service \(Amazon ECS\) task definition with host networking mode has 'privileged' or 'user' container definitions\. The rule is NON\_COMPLIANT for task definitions with host network mode and container definitions of privileged=false or empty and user=root or empty\.

**Identifier:** ECS\_TASK\_DEFINITION\_USER\_FOR\_HOST\_MODE\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East \(UAE\), Asia Pacific \(Osaka\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

SkipInactiveTaskDefinitions \(Optional\)Type: boolean  
Boolean flag to not check INACTIVE Amazon EC2 task definitions\. If set to 'true', the rule won't evaluate INACTIVE Amazon EC2 task definitions\. If set to 'false', the rule will evaluate the latest revision of INACTIVE Amazon EC2 task definitions\.

## AWS CloudFormation template<a name="w2aac12c31c27b9d247c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.