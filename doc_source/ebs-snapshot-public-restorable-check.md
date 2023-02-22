# ebs\-snapshot\-public\-restorable\-check<a name="ebs-snapshot-public-restorable-check"></a>

Checks whether Amazon Elastic Block Store \(Amazon EBS\) snapshots are not publicly restorable\. The rule is NON\_COMPLIANT if one or more snapshots with RestorableByUserIds field are set to all, that is, Amazon EBS snapshots are public\. 

**Identifier:** EBS\_SNAPSHOT\_PUBLIC\_RESTORABLE\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d179c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.