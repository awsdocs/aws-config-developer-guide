# secretsmanager\-rotation\-enabled\-check<a name="secretsmanager-rotation-enabled-check"></a>

Checks if AWS Secrets Manager secret has rotation enabled\. The rule also checks an optional `maximumAllowedRotationFrequency` parameter\. If the parameter is specified, the rotation frequency of the secret is compared with the maximum allowed frequency\. The rule is NON\_COMPLIANT if the secret is not scheduled for rotation\. The rule is also NON\_COMPLIANT if the rotation frequency is higher than the number specified in the maximumAllowedRotationFrequency parameter\.

**Note**  
Re\-evaluating this rule within 4 hours of the first evaluation will have no effect on the results\. 

**Identifier:** SECRETSMANAGER\_ROTATION\_ENABLED\_CHECK

**Resource Types:** AWS::SecretsManager::Secret

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

maximumAllowedRotationFrequency \(Optional\)Type: int  
Maximum allowed rotation frequency of the secret in days\.

maximumAllowedRotationFrequencyInHours \(Optional\)Type: int  
Maximum allowed rotation frequency of the secret in hours\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d565c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.