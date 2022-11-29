# clb\-desync\-mode\-check<a name="clb-desync-mode-check"></a>

Checks if Classic Load Balancers \(CLB\) are configured with a user defined Desync mitigation mode\. The rule is NON\_COMPLIANT if CLB Desync mitigation mode does not match with user defined Desync mitigation mode\. 

**Identifier:** CLB\_DESYNC\_MODE\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

desyncModeType: CSV  
Comma\-separated list of values\. You can select a max of two\. Valid values include 'Defensive', 'Strictest', and 'Monitor'\.

## AWS CloudFormation template<a name="w2aac12c31c27b9c63c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.