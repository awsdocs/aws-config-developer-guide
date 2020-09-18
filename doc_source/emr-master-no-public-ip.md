# emr\-master\-no\-public\-ip<a name="emr-master-no-public-ip"></a>

Checks whether Amazon Elastic MapReduce \(EMR\) clusters' master nodes have public IPs\. The rule is NON\_COMPLIANT if the master node has a public IP\.

**Note**  
This rule checks clusters that are in RUNNING or WAITING state\.

**Identifier:** EMR\_MASTER\_NO\_PUBLIC\_IP

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions except Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

None  

## AWS CloudFormation template<a name="w22aac11c29c17d175c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.