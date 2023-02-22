# emr\-master\-no\-public\-ip<a name="emr-master-no-public-ip"></a>

Checks if Amazon Elastic MapReduce \(EMR\) clusters' master nodes have public IPs\. The rule is NON\_COMPLIANT if the master node has a public IP\.

**Note**  
This rule checks clusters that are in RUNNING or WAITING state\.

**Identifier:** EMR\_MASTER\_NO\_PUBLIC\_IP

**Resource Types:** AWS::EMR::Cluster

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d313c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.