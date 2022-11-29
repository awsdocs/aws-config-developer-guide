# redshift\-cluster\-public\-access\-check<a name="redshift-cluster-public-access-check"></a>

Checks whether Amazon Redshift clusters are not publicly accessible\. The rule is NON\_COMPLIANT if the publiclyAccessible field is true in the cluster configuration item\. 

**Identifier:** REDSHIFT\_CLUSTER\_PUBLIC\_ACCESS\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c31c27b9d455c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.