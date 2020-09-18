# ebs\-snapshot\-public\-restorable\-check<a name="ebs-snapshot-public-restorable-check"></a>

Checks whether Amazon Elastic Block Store snapshots are not publicly restorable\. The rule is NON\_COMPLIANT if one or more snapshots with the `RestorableByUserIds` field is set to `all`\. If this field is set to `all`, then Amazon EBS snapshots are public\.

**Identifier:** EBS\_SNAPSHOT\_PUBLIC\_RESTORABLE\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions except Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

 None  

## AWS CloudFormation template<a name="w22aac11c29c17d113c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.