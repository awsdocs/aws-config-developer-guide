# secretsmanager\-scheduled\-rotation\-success\-check<a name="secretsmanager-scheduled-rotation-success-check"></a>

Checks if AWS Secrets Manager secrets rotated successfully according to the rotation schedule\. Secrets Manager calculates the date the rotation should happen\. The rule is NON\_COMPLIANT if the date passes and the secret isn't rotated\.

**Note**  
The rule returns NOT\_APPLICABLE for secrets without rotation\.

**Identifier:** SECRETSMANAGER\_SCHEDULED\_ROTATION\_SUCCESS\_CHECK

**Resource Types:** AWS::SecretsManager::Secret

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d567c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.