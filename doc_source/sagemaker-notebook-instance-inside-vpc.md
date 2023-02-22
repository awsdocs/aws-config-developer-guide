# sagemaker\-notebook\-instance\-inside\-vpc<a name="sagemaker-notebook-instance-inside-vpc"></a>

Checks if an Amazon SageMaker notebook instance is launched within a VPC or within a list of approved subnets\. The rule is NON\_COMPLIANT if a notebook instance is not launched within a VPC or if its subnet ID is not included in the parameter list\. 

**Identifier:** SAGEMAKER\_NOTEBOOK\_INSTANCE\_INSIDE\_VPC

**Resource Types:** AWS::SageMaker::NotebookInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

SubnetIds \(Optional\)Type: CSV  
Comma\-separated list of subnet IDs that notebook instances can be launched in\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d527c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.