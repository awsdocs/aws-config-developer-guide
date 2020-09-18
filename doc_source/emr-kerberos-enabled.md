# emr\-kerberos\-enabled<a name="emr-kerberos-enabled"></a>

Checks that Amazon EMR clusters have Kerberos enabled\. The rule is NON\_COMPLIANT if a security configuration is not attached to the cluster or the security configuration does not satisfy the specified rule parameters\.

**Identifier:** EMR\_KERBEROS\_ENABLED

**Trigger type:** Periodic 

**AWS Region:** All supported AWS Regions

**Parameters:**

 ticketLifetimeInHours \(optional\)   
Period for which Kerberos ticket issued by cluster's KDC is valid\.

 realm \(optional\)   
Kereberos realm name of the other realm in the trust relationship\. 

 domain \(optional\)   
Domain name of the other realm in the trust relationship\.

 adminServer \(optional\)   
Fully qualified domain of the admin server in the other realm of the trust relationship\.

 kdcServer \(optional\)   
Fully qualified domain of the KDC server in the other realm of the trust relationship\.

## AWS CloudFormation template<a name="w22aac11c29c17d173c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.