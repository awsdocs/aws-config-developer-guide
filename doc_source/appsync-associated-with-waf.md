# appsync\-associated\-with\-waf<a name="appsync-associated-with-waf"></a>

Checks if AWS AppSync APIs are associated with AWS WAFv2 web access control lists \(ACLs\)\. The rule is NON\_COMPLIANT for an AWS AppSync API if it is not associated with a web ACL\. 

**Identifier:** APPSYNC\_ASSOCIATED\_WITH\_WAF

**Resource Types:** AWS::AppSync::GraphQLApi

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

wafWebAclARNs \(Optional\)Type: CSV  
Comma\-separated list of Amazon Resource Names \(ARNs\) for authorized web ACLs\.

## AWS CloudFormation template<a name="w2aac12c33c15b9c37c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.