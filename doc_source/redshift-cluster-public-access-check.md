# redshift\-cluster\-public\-access\-check<a name="redshift-cluster-public-access-check"></a>

Checks if Amazon Redshift clusters are not publicly accessible\. The rule is NON\_COMPLIANT if the `publiclyAccessible` field is true in the cluster configuration item\.

**Identifier:** REDSHIFT\_CLUSTER\_PUBLIC\_ACCESS\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w85aac12c32c17b9d455c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.