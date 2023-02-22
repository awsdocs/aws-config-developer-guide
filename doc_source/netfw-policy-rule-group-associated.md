# netfw\-policy\-rule\-group\-associated<a name="netfw-policy-rule-group-associated"></a>

Check AWS Network Firewall policy is associated with stateful OR stateless rule groups\. This rule is NON\_COMPLIANT if no stateful or stateless rule groups are associated with the Network Firewall policy else COMPLIANT if any one of the rule group exists\. 

**Identifier:** NETFW\_POLICY\_RULE\_GROUP\_ASSOCIATED

**Resource Types:** AWS::NetworkFirewall::FirewallPolicy

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d393c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.