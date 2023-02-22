# ecs\-containers\-nonprivileged<a name="ecs-containers-nonprivileged"></a>

Checks if the privileged parameter in the container definition of ECSTaskDefinitions is set to ‘true’\. The rule is NON\_COMPLIANT if the privileged parameter is ‘true’\. 

**Identifier:** ECS\_CONTAINERS\_NONPRIVILEGED

**Resource Types:** AWS::ECS::TaskDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d237c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.