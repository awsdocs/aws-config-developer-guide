# netfw\-policy\-default\-action\-full\-packets<a name="netfw-policy-default-action-full-packets"></a>

Checks if an AWS Network Firewall policy is configured with a user defined default stateless action for full packets\. This rule is NON\_COMPLIANT if default stateless action for full packets does not match with user defined default stateless action\. 

**Identifier:** NETFW\_POLICY\_DEFAULT\_ACTION\_FULL\_PACKETS

**Resource Types:** AWS::NetworkFirewall::FirewallPolicy

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

statelessDefaultActionsType: CSV  
Comma\-separated list of values\. You can select a max of two\. Valid values include 'aws:pass', 'aws:drop', and 'aws:forward\_to\_sfe'\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d391c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.