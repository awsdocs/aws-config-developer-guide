# emr\-kerberos\-enabled<a name="emr-kerberos-enabled"></a>

Checks if Amazon EMR clusters have Kerberos enabled\. The rule is NON\_COMPLIANT if a security configuration is not attached to the cluster or the security configuration does not satisfy the specified rule parameters\.

**Identifier:** EMR\_KERBEROS\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

TicketLifetimeInHours \(Optional\)Type: int  
Period for which Kerberos ticket issued by cluster's KDC is valid\.

Realm \(Optional\)Type: String  
Kereberos realm name of the other realm in the trust relationship\.

Domain \(Optional\)Type: String  
Domain name of the other realm in the trust relationship\.

AdminServer \(Optional\)Type: String  
Fully qualified domain of the admin server in the other realm of the trust relationship\.

KdcServer \(Optional\)Type: String  
Fully qualified domain of the KDC server in the other realm of the trust relationship\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d337c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.