# efs\-access\-point\-enforce\-user\-identity<a name="efs-access-point-enforce-user-identity"></a>

Checks if Amazon Elastic File System \(Amazon EFS\) access points are configured to enforce a user identity\. The rule is NON\_COMPLIANT if 'PosixUser' is not defined or if parameters are provided and there is no match in the corresponding parameter\. 

**Identifier:** EFS\_ACCESS\_POINT\_ENFORCE\_USER\_IDENTITY

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\) Region

**Parameters:**

approvedUids \(Optional\)Type: CSV  
Comma\-separated list of POSIX user ID that are approved for EFS access point user enforcement\.

approvedGids \(Optional\)Type: CSV  
Comma\-separated list of POSIX group IDs that are approved for EFS access point user enforcement\.

## AWS CloudFormation template<a name="w85aac12c32c17b9d251c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.