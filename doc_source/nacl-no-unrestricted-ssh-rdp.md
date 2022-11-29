# nacl\-no\-unrestricted\-ssh\-rdp<a name="nacl-no-unrestricted-ssh-rdp"></a>

Checks if default ports for SSH/RDP ingress traffic for network access control lists \(NACLs\) is unrestricted\. The rule is NON\_COMPLIANT if a NACL inbound entry allows a source TCP or UDP CIDR block for ports 22 or 3389\. 

**Identifier:** NACL\_NO\_UNRESTRICTED\_SSH\_RDP

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Middle East \(UAE\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c31c27b9d377c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.