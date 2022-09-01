# iam\-password\-policy<a name="iam-password-policy"></a>

Checks if the account password policy for IAM users meets the specified requirements indicated in the parameters\. This rule is NON\_COMPLIANT if the account password policy does not meet the specified requirements\.

**Note**  
The rule is marked as NON\-COMPLIANT when default IAM password policy is used\.

**Important**  
The `true` and `false` values for the rule parameters are case\-sensitive\. If `true` is not provided in lowercase, it will be treated as `false.`

**Identifier:** IAM\_PASSWORD\_POLICY

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

RequireUppercaseCharacters \(Optional\)Type: booleanDefault: true  
Require at least one uppercase character in password\.

RequireLowercaseCharacters \(Optional\)Type: booleanDefault: true  
Require at least one lowercase character in password\.

RequireSymbols \(Optional\)Type: booleanDefault: true  
Require at least one symbol in password\.

RequireNumbers \(Optional\)Type: booleanDefault: true  
Require at least one number in password\.

MinimumPasswordLength \(Optional\)Type: intDefault: 14  
Password minimum length\.

PasswordReusePrevention \(Optional\)Type: intDefault: 24  
Number of passwords before allowing reuse\.

MaxPasswordAge \(Optional\)Type: intDefault: 90  
Number of days before password expiration\.

## AWS CloudFormation template<a name="w85aac12c32c17b9d329c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.