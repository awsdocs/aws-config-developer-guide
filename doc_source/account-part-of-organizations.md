# account\-part\-of\-organizations<a name="account-part-of-organizations"></a>

Checks if an AWS account is part of AWS Organizations\. The rule is NON\_COMPLIANT if an AWS account is not part of AWS Organizations or AWS Organizations master account ID does not match rule parameter `MasterAccountId`\.

**Identifier:** ACCOUNT\_PART\_OF\_ORGANIZATIONS

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

MasterAccountId \(Optional\)Type: String  
The master account ID for an AWS account\.

## AWS CloudFormation template<a name="w2aac12c33c15b9b3c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.