# secretsmanager\-rotation\-enabled\-check<a name="secretsmanager-rotation-enabled-check"></a>

Checks whether AWS Secret Manager secret has rotation enabled\. If the `maximumAllowedRotationFrequency` parameter is specified, the rotation frequency of the secret is compared with the maximum allowed frequency\. 

**Identifier:** SECRETSMANAGER\_ROTATION\_ENABLED\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

maximumAllowedRotationFrequency \(Optional\)Type: int  
Maximum allowed rotation frequency of the secret in days\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d325c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.