# secretsmanager\-scheduled\-rotation\-success\-check<a name="secretsmanager-scheduled-rotation-success-check"></a>

Checks whether AWS Secrets Manager secret rotation has triggered/started successfully as per the rotation schedule\. The rule returns NON\_COMPLIANT if `RotationOccurringAsScheduled` is false\. 

**Note**  
The rule returns NOT\_APPLICABLE for secrets without rotation\.

**Identifier:** SECRETSMANAGER\_SCHEDULED\_ROTATION\_SUCCESS\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w76aac11c31c17b7d471c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.