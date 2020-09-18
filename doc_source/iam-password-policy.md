# iam\-password\-policy<a name="iam-password-policy"></a>

Checks whether the account password policy for IAM users meets the specified requirements\.

**Identifier:** IAM\_PASSWORD\_POLICY

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions

**Parameters:**

 RequireUppercaseCharacters   
 Require at least one uppercase character in password\. 

 RequireLowercaseCharacters   
 Require at least one lowercase character in password\. 

 RequireSymbols   
 Require at least one symbol in password\. 

 RequireNumbers   
 Require at least one number in password\. 

 MinimumPasswordLength   
 Password minimum length\. 

 PasswordReusePrevention   
 Number of passwords before allowing reuse\. 

 MaxPasswordAge   
 Number of days before password expiration\. 

## AWS CloudFormation template<a name="w22aac11c29c17d199c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.