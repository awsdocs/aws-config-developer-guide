# secretsmanager\-scheduled\-rotation\-success\-check<a name="secretsmanager-scheduled-rotation-success-check"></a>

Checks and verifies whether AWS Secrets Manager secret rotation has rotated successfully as per the rotation schedule\. The rule is NON\_COMPLIANT if `RotationOccurringAsScheduled` is false\. 

**Note**  
The rule marks secrets without rotation NOT\_APPLICABLE\.

**Identifier:** SECRETSMANAGER\_SCHEDULED\_ROTATION\_SUCCESS\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions except Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

 None  

## AWS CloudFormation template<a name="w22aac11c29c17d317c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.